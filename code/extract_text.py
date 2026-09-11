"""
extract_text.py — 剥离公众号导出 Markdown 的 HTML/CSS/SVG 噪声，输出干净正文。

用法：
  python3 code/extract_text.py "文章名"           # 单篇
  python3 code/extract_text.py --list             # 列出缺摘要的文章
  python3 code/extract_text.py --batch 0 3        # 输出第 0..2 篇缺摘要文章的正文
"""
import re
import sys
from pathlib import Path

BASE = Path(__file__).parent.parent
RAW = BASE / "raw" / "articles"
SUMM = BASE / "wiki" / "summaries"
LIMIT = 9000  # 单篇正文输出上限（字符）


def missing():
    """返回缺摘要的文章路径，按名称排序。"""
    done = {p.stem for p in SUMM.glob("*.md")}
    return sorted((p for p in RAW.glob("*.md") if p.stem not in done), key=lambda p: p.stem)


def clean(text: str) -> str:
    """剥离导出噪声，保留正文段落。"""
    # 内联 CSS（导出时挤在首行）与 SVG data-uri
    text = re.sub(r"data:image/svg\+xml[^)\s]*", "", text)
    text = re.sub(r"\.[_a-zA-Z][-_a-zA-Z0-9]*\s*\{[^}]*\}", "", text)
    text = re.sub(r"(?:body|img|a|blockquote[^{]*)\s*\{[^}]*\}", "", text)
    # 图片、HTML 标签、多余转义
    text = re.sub(r"!\[[^\]]*\]\([^)]*\)", "", text)
    text = re.sub(r"<[^>]{1,400}>", "", text)
    text = text.replace("\\*", "*").replace("\\_", "_")

    keep = []
    for line in text.splitlines():
        s = line.strip()
        if not s:
            continue
        # 明显的样式/图标残留
        if len(s) > 500 and ("{" in s or "%3" in s or "xmlns" in s):
            continue
        if re.fullmatch(r"图\d+", s):
            continue
        if s in {"END", "QUOTE", "留言", "赞", "分享", "推荐", "阅读", "推荐阅读", "本文看点"}:
            continue
        # 纯装饰性分节标记（01 / 02 / SOCIAL HABIT 之类）
        if re.fullmatch(r"\d{2}", s) or re.fullmatch(r"[A-Z][A-Z\s&-]{2,30}", s):
            continue
        # 文末的历史文章推荐链接
        if re.fullmatch(r"[•·]", s):
            continue
        if re.fullmatch(r"\[.*\]\(https://mp\.weixin\.qq\.com[^)]*\)", s):
            continue
        # 目录式链接行（"12. [标题](url)"）——月度总结里成片出现，只留标题
        m = re.fullmatch(r"(\d+)[.、]\s*\[(.+?)\]\(https://mp\.weixin\.qq\.com[^)]*\)", s)
        if m:
            keep.append(f"{m.group(1)}. {m.group(2)}")
            continue
        # 正文内联的历史文章链接：保留文字，去掉 URL
        s = re.sub(r"\[(.+?)\]\(https://mp\.weixin\.qq\.com[^)]*\)", r"《\1》", s)
        keep.append(s)

    out = "\n".join(keep)
    out = re.sub(r"\n{3,}", "\n\n", out)
    return out.strip()


def emit(path: Path):
    body = clean(path.read_text(encoding="utf-8", errors="ignore"))
    truncated = len(body) > LIMIT
    print(f"\n{'='*70}\nFILE: {path.name}\n{'='*70}")
    print(body[:LIMIT])
    if truncated:
        print(f"\n[...正文已截断，原长 {len(body)} 字符]")


def main():
    args = sys.argv[1:]
    if not args:
        print(__doc__)
        return
    if args[0] == "--list":
        for i, p in enumerate(missing()):
            print(f"{i:>3} {p.stem}")
        return
    if args[0] == "--batch":
        start, count = int(args[1]), int(args[2])
        for p in missing()[start:start + count]:
            emit(p)
        return
    target = RAW / (args[0] if args[0].endswith(".md") else args[0] + ".md")
    if not target.exists():
        print(f"找不到：{target}")
        return
    emit(target)


if __name__ == "__main__":
    main()
