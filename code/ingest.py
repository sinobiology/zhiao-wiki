"""
ingest.py — 知奥ZHAO 知识库生成脚本（DeepSeek 版）

功能：
  1. 扫描 raw/articles/ 下的 Markdown 文件
  2. 调用 DeepSeek（OpenAI 兼容接口）按 SCHEMA.md 规范生成摘要
  3. 将摘要保存到 wiki/summaries/
  4. 更新 wiki/index.md

用法：
  python code/ingest.py                    # 处理所有未处理文章
  python code/ingest.py --file 文章名.md   # 处理单篇（强制重做）
  python code/ingest.py --rebuild          # 强制重建所有摘要

环境变量（全部可选，默认值见下）：
  DEEPSEEK_API_KEY / LLM_API_KEY   必填，取 ~/.hermes/.env 里的 DEEPSEEK_API_KEY
  LLM_BASE_URL     default: https://api.deepseek.com/v1
  LLM_MODEL        default: deepseek-v4-pro   （可选 deepseek-flash，更快更省）
  LLM_THINKING     default: disabled          （enabled 会走思考链，与正文共享 max_tokens）
  LLM_MAX_TOKENS   default: 4096
  LLM_TIMEOUT      default: 180

仅用标准库，无需 pip 安装任何依赖。
"""

import os
import re
import sys
import json
import time
import argparse
import datetime
import urllib.request
import urllib.error
from pathlib import Path

# ── 路径配置 ──────────────────────────────────────────────────────────────────
BASE_DIR    = Path(__file__).parent.parent          # 知奥知识库/
RAW_DIR     = BASE_DIR / "raw" / "articles"
WIKI_DIR    = BASE_DIR / "wiki"
SUMMARY_DIR = WIKI_DIR / "summaries"
INDEX_FILE  = WIKI_DIR / "index.md"

SUMMARY_DIR.mkdir(parents=True, exist_ok=True)

# ── 模型配置 ──────────────────────────────────────────────────────────────────
def _load_key() -> str | None:
    """按优先级取 key：环境变量 → ~/.hermes/.env 的 DEEPSEEK_API_KEY。"""
    for env in ("DEEPSEEK_API_KEY", "LLM_API_KEY"):
        if os.environ.get(env):
            return os.environ[env].strip()
    hermes_env = Path.home() / ".hermes" / ".env"
    if hermes_env.exists():
        for line in hermes_env.read_text(encoding="utf-8", errors="ignore").splitlines():
            if line.startswith("DEEPSEEK_API_KEY="):
                return line.split("=", 1)[1].strip().strip('"').strip("'")
    return None

BASE_URL    = os.environ.get("LLM_BASE_URL", "https://api.deepseek.com/v1").rstrip("/")
MODEL       = os.environ.get("LLM_MODEL", "deepseek-v4-pro")
THINKING    = os.environ.get("LLM_THINKING", "disabled").lower()
MAX_TOKENS  = int(os.environ.get("LLM_MAX_TOKENS", "4096"))
TIMEOUT     = int(os.environ.get("LLM_TIMEOUT", "180"))
API_KEY     = _load_key()

# 回环/内网地址绕开代理；公网地址跟随系统代理（本机有全局代理，端口会变）
_OPENER = urllib.request.build_opener()

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
- type 只能取这五个值之一：技术、行业、管理、感悟、产品
- 摘要要保留原文的逻辑骨架，不要泛泛而谈
- 金句必须是原文原话，不要改写
- 直接输出摘要页本身，不要用代码块包裹，不要添加任何额外说明
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


# ── LLM 调用 ──────────────────────────────────────────────────────────────────
def _strip_code_fence(text: str) -> str:
    """模型偶尔会用 ```markdown 包裹，剥掉。"""
    t = text.strip()
    m = re.match(r"^```[a-zA-Z]*\s*\n(.*?)\n?```$", t, re.S)
    return m.group(1).strip() if m else t


def call_llm(system: str, user: str, retries: int = 3) -> str:
    """
    调用 OpenAI 兼容的 /chat/completions。

    ⚠️ deepseek-v4-pro / deepseek-flash 都是推理模型：思考链写在 reasoning_content，
    且与正文共享 max_tokens。若思考没被关掉又给少了额度，会出现「HTTP 200、无报错、
    正文零字」的静默失败——所以这里显式关思考，并对该情形单独报错。
    """
    payload = {
        "model": MODEL,
        "max_tokens": MAX_TOKENS,
        "messages": [
            {"role": "system", "content": system},
            {"role": "user", "content": user},
        ],
    }
    if THINKING == "disabled":
        payload["thinking"] = {"type": "disabled"}

    body = json.dumps(payload).encode("utf-8")
    last_err = None

    for attempt in range(1, retries + 1):
        try:
            req = urllib.request.Request(
                f"{BASE_URL}/chat/completions",
                data=body,
                headers={
                    "Authorization": f"Bearer {API_KEY}",
                    "Content-Type": "application/json",
                },
                method="POST",
            )
            with _OPENER.open(req, timeout=TIMEOUT) as r:
                data = json.load(r)

            msg = data["choices"][0]["message"]
            content = (msg.get("content") or "").strip()
            reasoning = (msg.get("reasoning_content") or "").strip()
            finish = data["choices"][0].get("finish_reason")

            if not content:
                # 静默失败：正文空、只有思考链，或额度被思考吃光
                detail = "思考链吃光了 max_tokens" if reasoning or finish == "length" else "模型返回空正文"
                raise RuntimeError(
                    f"{detail}（finish_reason={finish}, "
                    f"reasoning_content={len(reasoning)} 字, usage={data.get('usage')}）"
                )

            if len(content) < 200:
                raise RuntimeError(f"正文过短（{len(content)} 字），疑似截断：{content[:120]}")

            return _strip_code_fence(content)

        except (urllib.error.HTTPError, urllib.error.URLError, RuntimeError, KeyError,
                json.JSONDecodeError) as e:
            last_err = e
            code = getattr(e, "code", None)
            if code in (401, 403):      # 鉴权失败，重试无意义
                raise
            if attempt < retries:
                wait = 2 * attempt
                print(f"    [重试 {attempt}/{retries - 1}] {e} — {wait}s 后再来")
                time.sleep(wait)

    raise RuntimeError(f"调用失败（已重试 {retries} 次）：{last_err}")


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

    content = md_path.read_text(encoding="utf-8", errors="ignore")

    if len(content.strip()) < 100:
        print(f"  [跳过] {md_path.name}（内容过短）")
        return None

    print(f"  [处理] {md_path.name} ...")
    article_type = classify_article(content)

    wiki_content = call_llm(
        SYSTEM_PROMPT,
        build_user_prompt(md_path.name, content, article_type),
    )

    out_path.write_text(wiki_content.rstrip() + "\n", encoding="utf-8")
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
    parser = argparse.ArgumentParser(description="知奥ZHAO 知识库生成脚本（DeepSeek）")
    parser.add_argument("--file", help="只处理指定文件名（相对于 raw/articles/）")
    parser.add_argument("--rebuild", action="store_true", help="强制重建所有摘要")
    args = parser.parse_args()

    if not API_KEY:
        # 必须以非零码退出：否则 CI 里 key 缺失会让整条流水线「绿灯空转」，
        # 表面成功、实际一篇摘要都不会生成，极难察觉。
        print("错误：未找到 API Key —— DEEPSEEK_API_KEY 为空", file=sys.stderr)
        print("  本地：export DEEPSEEK_API_KEY=... 或确认 ~/.hermes/.env 已配置", file=sys.stderr)
        print("  CI：仓库 Settings → Secrets and variables → Actions 添加 DEEPSEEK_API_KEY", file=sys.stderr)
        sys.exit(1)

    print(f"模型：{MODEL} @ {BASE_URL} | 思考：{THINKING} | max_tokens：{MAX_TOKENS}\n")

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
        processed, failed = 0, []
        for md in md_files:
            try:
                if process_article(md, force=args.rebuild):
                    processed += 1
            except Exception as e:
                print(f"  [失败] {md.name} → {e}")
                failed.append((md.name, str(e)))

        print(f"\n本次处理：{processed} 篇 | 总计：{len(list(SUMMARY_DIR.glob('*.md')))} 篇")
        if failed:
            print(f"失败 {len(failed)} 篇：")
            for name, err in failed:
                print(f"  - {name} → {err[:120]}")

    update_index()


if __name__ == "__main__":
    main()
