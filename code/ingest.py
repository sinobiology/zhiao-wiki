"""
ingest.py — 知奥ZHAO 知识库生成脚本

功能：
  1. 扫描 raw/articles/ 下的 Markdown 文件
  2. 调用 Anthropic API 按 SCHEMA.md 规范生成摘要
  3. 将摘要保存到 wiki/summaries/
  4. 更新 wiki/index.md

用法：
  python code/ingest.py                    # 处理所有未处理文章
  python code/ingest.py --file 文章名.md   # 处理单篇
  python code/ingest.py --rebuild          # 强制重建所有摘要
"""

import os
import re
import json
import argparse
import datetime
from pathlib import Path

import anthropic

# ── 路径配置 ──────────────────────────────────────────────────────────────────
BASE_DIR    = Path(__file__).parent.parent          # 知奥知识库/
RAW_DIR     = BASE_DIR / "raw" / "articles"
WIKI_DIR    = BASE_DIR / "wiki"
SUMMARY_DIR = WIKI_DIR / "summaries"
INDEX_FILE  = WIKI_DIR / "index.md"

SUMMARY_DIR.mkdir(parents=True, exist_ok=True)

# ── Anthropic 客户端 ──────────────────────────────────────────────────────────
# 支持第三方代理（如 aicodewith）：设置 ANTHROPIC_BASE_URL 环境变量即可
_base_url = os.environ.get("ANTHROPIC_BASE_URL")  # 不设置则使用官方地址
client = anthropic.Anthropic(
    api_key=os.environ.get("ANTHROPIC_API_KEY"),
    base_url=_base_url if _base_url else None,
)
MODEL = "claude-opus-4-6"

# ── 文章类型关键词（用于辅助分类） ────────────────────────────────────────────
TYPE_KEYWORDS = {
    "技术": ["发酵", "菌种", "基因", "工艺", "培养基", "传质", "代谢", "酶", "底物", "产率"],
    "行业": ["市场", "格局", "竞争", "产业", "贸易", "反倾销", "专利", "并购", "上市", "年报"],
    "管理": ["管理", "成本", "战略", "组织", "效率", "降本", "规模", "决策", "领导"],
    "感悟": ["人生", "思考", "学习", "成长", "感悟", "跑步", "读书", "情绪", "价值观"],
}

def classify_article(content: str) -> str:
    """根据关键词频率判断文章类型。"""
    scores = {t: 0 for t in TYPE_KEYWORDS}
    for article_type, keywords in TYPE_KEYWORDS.items():
        for kw in keywords:
            scores[article_type] += content.count(kw)
    return max(scores, key=scores.get)


# ── 核心 Prompt ───────────────────────────────────────────────────────────────
SYSTEM_PROMPT = """你是「知奥ZHAO」公众号的知识提炼助手。
你的任务是将一篇公众号文章转化为结构化的 Wiki 摘要页，严格遵循以下规范：

【输出格式】
---
title: "文章标题"
type: "技术 | 行业 | 管理 | 感悟 | 产品"
tags: ["标签1", "标签2", "标签3"]
source_articles: ["原文件名"]
created: "今天日期"
entities: ["实体1", "实体2", "实体3"]
---

# 标题

## 核心逻辑
（文章最核心的1-3个观点，每条一句话，直接、有力）

## 行业洞察
（行业层面的关键发现；若为感悟类文章则写"N/A"）

## 技术/管理要点
（具体的技术细节或管理方法论，用列表呈现）

## 关联实体
（用 [[双向链接]] 格式列出所有相关实体，如 [[赖氨酸]]、[[味之素]]、[[规模效应]]）

## 金句归纳
> "从原文中提取最有价值的1-2句金句"

【规则】
- 双向链接必须用 [[实体名]] 格式
- 实体包括：产品名、公司名、人名、核心概念
- 摘要要保留原文的逻辑骨架，不要泛泛而谈
- 金句必须是原文原话，不要改写
"""

def build_user_prompt(filename: str, content: str, article_type: str) -> str:
    today = datetime.date.today().isoformat()
    return f"""请将以下文章转化为 Wiki 摘要页。

文件名：{filename}
预判类型：{article_type}
今天日期：{today}

---原文开始---
{content[:8000]}
---原文结束---

请严格按照系统提示中的格式输出，不要添加任何额外说明。"""


# ── 处理单篇文章 ──────────────────────────────────────────────────────────────
def process_article(md_path: Path, force: bool = False) -> Path | None:
    """
    处理一篇文章，生成 wiki/summaries/<stem>.md。
    返回生成的文件路径，若跳过则返回 None。
    """
    stem = md_path.stem
    out_path = SUMMARY_DIR / f"{stem}.md"

    if out_path.exists() and not force:
        print(f"  [跳过] {md_path.name}（已存在摘要）")
        return None

    print(f"  [处理] {md_path.name} ...")
    content = md_path.read_text(encoding="utf-8", errors="ignore")

    if len(content.strip()) < 100:
        print(f"  [跳过] {md_path.name}（内容过短）")
        return None

    article_type = classify_article(content)

    message = client.messages.create(
        model=MODEL,
        max_tokens=2048,
        system=SYSTEM_PROMPT,
        messages=[
            {"role": "user", "content": build_user_prompt(md_path.name, content, article_type)}
        ],
    )

    wiki_content = message.content[0].text
    out_path.write_text(wiki_content, encoding="utf-8")
    print(f"  [完成] → {out_path.relative_to(BASE_DIR)}")
    return out_path


# ── 更新 index.md ─────────────────────────────────────────────────────────────
def update_index():
    """扫描 summaries/ 并重建 wiki/index.md。"""
    summaries = sorted(SUMMARY_DIR.glob("*.md"))
    entities_dir = WIKI_DIR / "entities"
    entities = sorted(entities_dir.glob("*.md")) if entities_dir.exists() else []

    lines = [
        "# 知奥ZHAO 知识库全量索引\n",
        "> 自动生成，请勿手动编辑。由 `code/ingest.py` 维护。\n",
        f"\n*最后更新：{datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}*\n",
        "\n## 文章摘要（summaries/）\n",
    ]

    for s in summaries:
        lines.append(f"- [[{s.stem}]]\n")

    lines.append(f"\n## 实体页（entities/）\n")
    for e in entities:
        lines.append(f"- [[{e.stem}]]\n")

    lines.append(f"\n## 统计\n")
    lines.append(f"- 文章摘要总数：{len(summaries)}\n")
    lines.append(f"- 实体页总数：{len(entities)}\n")

    INDEX_FILE.write_text("".join(lines), encoding="utf-8")
    print(f"\n[索引] 已更新 wiki/index.md（{len(summaries)} 篇摘要）")


# ── 主入口 ────────────────────────────────────────────────────────────────────
def main():
    parser = argparse.ArgumentParser(description="知奥ZHAO 知识库生成脚本")
    parser.add_argument("--file", help="只处理指定文件名（相对于 raw/articles/）")
    parser.add_argument("--rebuild", action="store_true", help="强制重建所有摘要")
    args = parser.parse_args()

    if not os.environ.get("ANTHROPIC_API_KEY"):
        print("错误：请先设置环境变量 ANTHROPIC_API_KEY")
        print("  Windows: set ANTHROPIC_API_KEY=sk-ant-...")
        return

    if args.file:
        target = RAW_DIR / args.file
        if not target.exists():
            print(f"错误：找不到文件 {target}")
            return
        process_article(target, force=True)
    else:
        md_files = sorted(RAW_DIR.glob("*.md"))
        if not md_files:
            print(f"raw/articles/ 下没有找到 .md 文件")
            print(f"请将公众号文章复制到：{RAW_DIR}")
            return

        print(f"找到 {len(md_files)} 篇文章，开始处理...\n")
        processed = 0
        for md in md_files:
            result = process_article(md, force=args.rebuild)
            if result:
                processed += 1

        print(f"\n本次处理：{processed} 篇 | 总计：{len(list(SUMMARY_DIR.glob('*.md')))} 篇")

    update_index()


if __name__ == "__main__":
    main()
