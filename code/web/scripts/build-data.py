"""
build-data.py — 从 wiki/summaries/ 生成前端所需的 JSON 数据文件
"""
import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

import json, re, shutil, pathlib

BASE   = pathlib.Path(__file__).parent.parent.parent.parent  # 知奥知识库/
WIKI   = BASE / "wiki" / "summaries"
ENTITIES = BASE / "wiki" / "entities"
OUT    = pathlib.Path(__file__).parent.parent / "public" / "data"
PAGES  = OUT / "pages"

OUT.mkdir(parents=True, exist_ok=True)
PAGES.mkdir(parents=True, exist_ok=True)

TYPE_COLOR = {
    "技术": "concept",
    "行业": "company",
    "管理": "interview",
    "感悟": "person",
    "产品": "letter",
}

# 图谱中实体节点的最低引用次数。只被 1 篇引用的实体只连 1 条边，是纯噪音；
# 历史上这里漏判（注释写了 ≥2 但代码只判重），导致 1600+ 个孤立节点进图。
MIN_ENTITY_REFS = 3

def parse_frontmatter(text):
    """字符串 split 解析 YAML frontmatter，不依赖 gray-matter。"""
    if not text.startswith("---"):
        return {}, text
    parts = text.split("---", 2)
    if len(parts) < 3:
        return {}, text
    fm_raw, body = parts[1], parts[2].lstrip("\n")
    meta = {}
    for line in fm_raw.splitlines():
        if ":" not in line:
            continue
        k, _, v = line.partition(":")
        k = k.strip()
        v = v.strip().strip('"\'')
        if v.startswith("[") and v.endswith("]"):
            inner = v[1:-1]
            meta[k] = [x.strip().strip('"\'') for x in inner.split(",") if x.strip()]
        else:
            meta[k] = v
    return meta, body

def extract_wikilinks(text):
    return re.findall(r'\[\[([^\]]+)\]\]', text)

def make_excerpt(body, n=200):
    text = re.sub(r'#+\s', '', body)
    text = re.sub(r'\[\[([^\]]+)\]\]', r'\1', text)
    text = re.sub(r'\*+', '', text)
    text = re.sub(r'`[^`]*`', '', text)
    text = text.replace('\r', '').replace('\n', ' ').strip()
    return text[:n]

# ── 扫描所有摘要 ──────────────────────────────────────────────────────────────
wiki_index = []
entity_refs = {}   # entity_name → count
article_links = {} # slug → [entity_names]

files = sorted(WIKI.glob("*.md"))
print(f"扫描 {len(files)} 个摘要文件...")

for f in files:
    content = f.read_text(encoding="utf-8")
    meta, body = parse_frontmatter(content)
    if not meta.get("title"):
        continue

    slug = f.stem
    links = extract_wikilinks(body)
    article_links[slug] = links

    # 统计口径是「被多少篇引用」而非「出现多少次」，必须与 gen_entities.py
    # 的建页门槛一致，否则会出现「图谱里有实体节点、点开却没有页」。
    for e in set(links):
        entity_refs[e] = entity_refs.get(e, 0) + 1

    wiki_index.append({
        "slug":     slug,
        "title":    meta.get("title", slug),
        "type":     meta.get("type", "感悟"),
        "category": meta.get("type", "感悟"),
        "tags":     meta.get("tags", []),
        "entities": meta.get("entities", []),
        "created":  meta.get("created", ""),
        "excerpt":  make_excerpt(body),
        "links":    links,
        "path":     f"pages/{slug}.md",
    })

    # 复制页面到 public/data/pages/
    shutil.copy2(f, PAGES / f.name)

print(f"  → {len(wiki_index)} 篇文章，{len(entity_refs)} 个实体")

# ── 复制实体页到 public/data/pages/ ───────────────────────────────────────────
# 前端 PageView 统一按 /data/pages/<slug>.md 取页；实体页与摘要共用同一命名空间，
# 因此实体页也必须复制过去，否则图谱里的实体节点点开只会显示「暂无对应页面」。
entity_files = sorted(ENTITIES.glob("*.md")) if ENTITIES.exists() else []
for f in entity_files:
    shutil.copy2(f, PAGES / f.name)
print(f"  ✓ 已复制 {len(entity_files)} 个实体页到 pages/")

# ── 生成 wiki-index.json ──────────────────────────────────────────────────────
(OUT / "wiki-index.json").write_text(
    json.dumps(wiki_index, ensure_ascii=False, indent=2), encoding="utf-8"
)
print("  ✓ wiki-index.json")

# ── 生成 graph.json ───────────────────────────────────────────────────────────
nodes = []
node_ids = set()

# 文章节点
for item in wiki_index:
    nodes.append({
        "id":    item["slug"],
        "label": item["title"][:20],
        "group": item["type"],
        "type":  "article",
    })
    node_ids.add(item["slug"])

# 实体节点：只保留被引用 ≥MIN_ENTITY_REFS 次的；按 refs 降序排列，
# 保证前端截断渲染时优先保留高频实体。
has_page = {f.stem for f in entity_files}
ent_nodes = []
for entity, count in entity_refs.items():
    if count < MIN_ENTITY_REFS:
        continue
    eid = f"entity:{entity}"
    if eid in node_ids:
        continue
    ent_nodes.append({
        "id":      eid,
        "label":   entity,
        "group":   "entity",
        "type":    "entity",
        "refs":    count,
        "hasPage": entity in has_page,
    })
    node_ids.add(eid)
ent_nodes.sort(key=lambda n: -n["refs"])
nodes.extend(ent_nodes)

# 边
edges = []
for slug, links in article_links.items():
    for entity in set(links):
        eid = f"entity:{entity}"
        if eid in node_ids:
            edges.append({"source": slug, "target": eid})

(OUT / "graph.json").write_text(
    json.dumps({"nodes": nodes, "edges": edges}, ensure_ascii=False, indent=2),
    encoding="utf-8"
)
print(f"  ✓ graph.json ({len(nodes)} 节点, {len(edges)} 边)")

# ── 生成 entity-index.json（实体页清单，供前端判断 wikilink 能否打开）────────
entity_index = []
for f in entity_files:
    meta, _ = parse_frontmatter(f.read_text(encoding="utf-8"))
    entity_index.append({
        "slug":  f.stem,
        "title": meta.get("title", f.stem),
        "type":  meta.get("type", ""),
        "refs":  entity_refs.get(f.stem, 0),
    })
entity_index.sort(key=lambda x: -x["refs"])
(OUT / "entity-index.json").write_text(
    json.dumps(entity_index, ensure_ascii=False, indent=2), encoding="utf-8"
)
print(f"  ✓ entity-index.json（{len(entity_index)} 个实体页）")

# ── 生成 search-index.json ────────────────────────────────────────────────────
search_index = [
    {"slug": x["slug"], "title": x["title"], "type": x["type"],
     "tags": x["tags"], "excerpt": x["excerpt"]}
    for x in wiki_index
]
(OUT / "search-index.json").write_text(
    json.dumps(search_index, ensure_ascii=False, indent=2), encoding="utf-8"
)
print("  ✓ search-index.json")

# ── 统计摘要 ──────────────────────────────────────────────────────────────────
type_counts = {}
for x in wiki_index:
    type_counts[x["type"]] = type_counts.get(x["type"], 0) + 1

print("\n文章类型分布：")
for t, c in sorted(type_counts.items(), key=lambda x: -x[1]):
    print(f"  {t}: {c}")

top_entities = sorted(entity_refs.items(), key=lambda x: -x[1])[:15]
print("\nTOP 15 实体：")
for e, c in top_entities:
    print(f"  {e}: {c}")

print("\n✅ 数据生成完成！")

