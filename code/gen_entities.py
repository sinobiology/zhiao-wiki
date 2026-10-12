#!/usr/bin/env python3
"""
gen_entities.py — 为高频实体补建 wiki/entities/<实体名>.md

背景：摘要正文里的 [[实体]] 链接有 2400+ 个，实体页只有 41 个 →
图谱里绝大多数实体是断链，点开是空页。本脚本对「被引用 ≥ MIN_REFS 次」
且尚无页面的实体，用 DeepSeek 生成实体页，风格对齐已有页面与 wiki/SCHEMA.md。

幂等：已有实体页的自动跳过；单篇失败不中断整批。

用法：
    python code/gen_entities.py                     # 全部缺页实体（≥MIN_REFS 次）
    python code/gen_entities.py --limit 1           # 只跑引用最多的一篇（试跑）
    python code/gen_entities.py --entity 合成生物学   # 只跑指定实体
    python code/gen_entities.py --rebuild           # 连已有页面一起重写（慎用）
"""
import argparse
import datetime
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import ingest  # 复用 call_llm / API_KEY：同一套 DeepSeek 配置与「静默零字」保护

BASE     = Path(__file__).parent.parent          # 知奥知识库/
SUMMARY  = BASE / "wiki" / "summaries"
ENTITIES = BASE / "wiki" / "entities"
ENTITIES.mkdir(parents=True, exist_ok=True)

MIN_REFS = 3      # 最低被引用次数（与 build-data.py 的 MIN_ENTITY_REFS 一致）
MAX_ARTS = 12     # 单个实体最多取多少篇材料
SNIPPET  = 900    # 每篇材料截断长度

SYSTEM = """你是「知奥ZHAO」公众号知识库的实体页撰写者。
根据某实体在若干篇文章摘要中的出现情况，为它撰写一页实体页。

【输出格式】严格照此，不要添加任何额外说明，不要用代码块包裹：
---
title: "实体名"
type: "技术 | 行业 | 管理 | 感悟 | 人物 | 公司 | 产品"
tags: ["标签1", "标签2", "标签3"]
created: "{today}"
entities: ["相关实体1", "相关实体2"]
---

# 实体名

## 定义
（2-3 句，说清它是什么、属于哪个领域）

## 在知奥体系中的位置
（2-4 段，说明它与库中其他概念 / 公司 / 产品 / 文章的关系，用 [[双向链接]] 关联）

## 关键数据
（从材料里提取的具体数字、时间、事实，逐条列出；材料里确实没有就写「暂无」）

## 关联实体
（用 [[ ]] 列出最相关的 3-8 个实体）

【规则】
- type 只能取：技术、行业、管理、感悟、人物、公司、产品
- 只写材料能支撑的内容，绝对不要编造数据、年份、人名、事件
- 实体可以是：产品名、公司名、人名、核心概念
- 双向链接必须用 [[实体名]] 格式
- 不要写「## 相关文章」章节，系统会自动追加
- 直接输出页面本身，不要任何前后缀"""


def parse_fm(text: str):
    if not text.startswith("---"):
        return {}, text
    parts = text.split("---", 2)
    if len(parts) < 3:
        return {}, text
    fm = {}
    for line in parts[1].splitlines():
        if ":" not in line:
            continue
        k, _, v = line.partition(":")
        k, v = k.strip(), v.strip().strip('"\'')
        if v.startswith("[") and v.endswith("]"):
            fm[k] = [x.strip().strip('"\'') for x in v[1:-1].split(",") if x.strip()]
        else:
            fm[k] = v
    return fm, parts[2]


def safe_name(entity: str) -> str:
    """实体页文件名必须与 [[实体名]] 完全一致，否则前端按名找不到页。"""
    return entity.replace("/", "-").replace("\\", "-")


def build_material(entity: str, slugs: list, arts: dict) -> list:
    """每篇材料 = 摘要正文前 SNIPPET 字 + 命中该实体的行（保留上下文）。"""
    out = []
    for s in slugs[:MAX_ARTS]:
        a = arts[s]
        body = a["body"]
        lines = [l.strip() for l in body.splitlines() if l.strip()]
        hit = [l for l in lines if entity in l]
        seg = body.strip()[:SNIPPET]
        if hit:
            extra = "\n".join(hit[:6])
            if extra not in seg:
                seg = seg + "\n\n【直接提到该实体的句子】\n" + extra
        out.append((a["title"], seg))
    return out


def build_user(entity: str, chunks: list, total: int) -> str:
    lines = [f"实体：{entity}",
             f"它在 {total} 篇文章摘要中被提及。下面是其中 {len(chunks)} 篇的材料。", ""]
    for i, (title, seg) in enumerate(chunks, 1):
        lines.append(f"### 材料{i}：《{title}》")
        lines.append(seg)
        lines.append("")
    lines.append("请按系统提示的格式，输出这个实体的实体页。")
    return "\n".join(lines)


def gen_one(entity: str, slugs: list, arts: dict) -> str:
    chunks = build_material(entity, sorted(slugs), arts)
    user = build_user(entity, chunks, len(slugs))
    today = datetime.date.today().isoformat()
    raw = ingest.call_llm(SYSTEM.replace("{today}", today), user)

    # 去掉模型可能带的前导空行，保证以 --- 开头（否则前端解析不到 frontmatter）
    raw = raw.lstrip("\r\n \t")
    if not raw.startswith("---"):
        raise RuntimeError(f"输出未以 frontmatter 开头：{raw[:80]}")

    # 「相关文章」由脚本用真实引用列表追加，避免模型编造文章名
    related = "\n".join(f"[[{s}]]" for s in sorted(slugs)[:40])
    more = f"\n\n（另有 {len(slugs) - 40} 篇未列出）" if len(slugs) > 40 else ""
    return raw.rstrip() + f"\n\n## 相关文章\n{related}{more}\n"


def main():
    ap = argparse.ArgumentParser(description="为高频实体补建实体页（DeepSeek）")
    ap.add_argument("--limit", type=int, default=0, help="只处理前 N 个（试跑用）")
    ap.add_argument("--entity", default="", help="只处理指定实体")
    ap.add_argument("--rebuild", action="store_true", help="连已有页面一起重写")
    ap.add_argument("--min-refs", type=int, default=MIN_REFS)
    args = ap.parse_args()

    if not ingest.API_KEY:
        print("错误：未找到 API Key —— DEEPSEEK_API_KEY 为空", file=sys.stderr)
        print("  本地：确认 ~/.hermes/.env 里有 DEEPSEEK_API_KEY", file=sys.stderr)
        sys.exit(1)

    arts, refs = {}, {}
    for p in sorted(SUMMARY.glob("*.md")):
        fm, body = parse_fm(p.read_text(encoding="utf-8"))
        if not fm.get("title"):
            continue
        arts[p.stem] = {"title": fm["title"], "body": body}
        for x in set(re.findall(r'\[\[([^\]|]+)\]', body)):
            refs.setdefault(x.strip(), set()).add(p.stem)

    existing = {p.stem for p in ENTITIES.glob("*.md")}
    todo = [(e, sorted(s)) for e, s in refs.items()
            if len(s) >= args.min_refs and (args.rebuild or e not in existing)]
    todo.sort(key=lambda x: -len(x[1]))
    if args.entity:
        todo = [x for x in todo if x[0] == args.entity]
    if args.limit:
        todo = todo[:args.limit]

    print(f"模型：{ingest.MODEL} | 现有实体页 {len(existing)} 个 | "
          f"本次待生成 {len(todo)} 个（≥{args.min_refs} 次引用）\n")

    made, failed, skipped = 0, [], 0
    for i, (entity, slugs) in enumerate(todo, 1):
        if entity != safe_name(entity):
            print(f"  [{i}/{len(todo)}] [跳过] {entity}（名称含路径分隔符，无法作文件名）")
            skipped += 1
            continue
        out = ENTITIES / f"{entity}.md"
        print(f"  [{i}/{len(todo)}] [处理] {entity}（{len(slugs)} 篇引用）...")
        try:
            page = gen_one(entity, slugs, arts)
            out.write_text(page, encoding="utf-8")
            made += 1
            print(f"        [完成] → wiki/entities/{entity}.md（{len(page)} 字）")
        except Exception as e:
            print(f"        [失败] {e}")
            failed.append((entity, str(e)))

    ingest.update_index()

    print(f"\n本次生成：{made} 个 | 失败 {len(failed)} 个 | 跳过 {skipped} 个 | "
          f"实体页总数：{len(list(ENTITIES.glob('*.md')))}")
    if failed:
        print("失败清单：")
        for n, e in failed:
            print(f"  - {n} → {e[:120]}")


if __name__ == "__main__":
    main()
