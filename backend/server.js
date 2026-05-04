/**
 * server.js — 知奥ZHAO 知识库后端
 *
 * 提供两个 API：
 *   GET  /api/articles          返回所有文章摘要的元数据列表
 *   GET  /api/articles/:slug    返回单篇摘要的完整内容
 *   POST /api/chat              AI 知奥对话接口
 */

import express from "express";
import cors from "cors";
import fs from "fs";
import path from "path";
import { fileURLToPath } from "url";
import matter from "gray-matter";
import Anthropic from "@anthropic-ai/sdk";

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const WIKI_DIR = path.join(__dirname, "../wiki/summaries");

const app = express();
app.use(cors());
app.use(express.json());

const client = new Anthropic({
  apiKey: process.env.ANTHROPIC_API_KEY,
  ...(process.env.ANTHROPIC_BASE_URL ? { baseURL: process.env.ANTHROPIC_BASE_URL } : {}),
});

// ── 工具函数 ──────────────────────────────────────────────────────────────────

/** 读取所有摘要文件，返回元数据数组 */
function loadAllSummaries() {
  if (!fs.existsSync(WIKI_DIR)) return [];
  return fs
    .readdirSync(WIKI_DIR)
    .filter((f) => f.endsWith(".md"))
    .map((filename) => {
      const raw = fs.readFileSync(path.join(WIKI_DIR, filename), "utf-8");
      const { data, content } = matter(raw);
      return {
        slug: filename.replace(".md", ""),
        title: data.title || filename.replace(".md", ""),
        type: data.type || "未分类",
        tags: data.tags || [],
        entities: data.entities || [],
        created: data.created || "",
        excerpt: content.slice(0, 200).replace(/#+\s/g, "").trim(),
      };
    });
}

/** 根据用户问题，从摘要库中检索最相关的 N 篇 */
function retrieveRelevant(query, summaries, topN = 5) {
  const q = query.toLowerCase();
  const scored = summaries.map((s) => {
    let score = 0;
    // 标题命中
    if (s.title.toLowerCase().includes(q)) score += 10;
    // 标签命中
    s.tags.forEach((t) => { if (t.toLowerCase().includes(q)) score += 5; });
    // 实体命中
    s.entities.forEach((e) => { if (e.toLowerCase().includes(q)) score += 3; });
    // 摘要命中
    if (s.excerpt.toLowerCase().includes(q)) score += 2;
    return { ...s, score };
  });
  return scored
    .filter((s) => s.score > 0)
    .sort((a, b) => b.score - a.score)
    .slice(0, topN);
}

/** 读取摘要文件完整内容 */
function loadSummaryContent(slug) {
  const filePath = path.join(WIKI_DIR, `${slug}.md`);
  if (!fs.existsSync(filePath)) return null;
  return fs.readFileSync(filePath, "utf-8");
}

// ── API 路由 ──────────────────────────────────────────────────────────────────

// 文章列表
app.get("/api/articles", (req, res) => {
  const summaries = loadAllSummaries();
  res.json({ total: summaries.length, articles: summaries });
});

// 单篇文章
app.get("/api/articles/:slug", (req, res) => {
  const content = loadSummaryContent(req.params.slug);
  if (!content) return res.status(404).json({ error: "文章不存在" });
  const { data, content: body } = matter(content);
  res.json({ meta: data, content: body });
});

// AI 知奥对话
app.post("/api/chat", async (req, res) => {
  const { message, history = [] } = req.body;
  if (!message) return res.status(400).json({ error: "message 不能为空" });

  const summaries = loadAllSummaries();
  const relevant = retrieveRelevant(message, summaries);

  // 构建知识上下文
  let context = "";
  if (relevant.length > 0) {
    context = "【相关知识库内容】\n";
    for (const s of relevant) {
      const full = loadSummaryContent(s.slug);
      if (full) {
        const { content } = matter(full);
        context += `\n### ${s.title}\n${content.slice(0, 1500)}\n`;
      }
    }
  }

  const systemPrompt = `你是「AI 知奥」，知奥ZHAO公众号作者赵忠光的数字分身。

【身份背景】
- 拥有 20 年工业生物发酵行业经验的 R&D 总监
- 深耕氨基酸（赖氨酸、苏氨酸、色氨酸、缬氨酸）、味精、合成生物学领域
- 擅长从成本逻辑、规模效应、系统性降本角度分析问题
- 偶尔用跑步、农耕、军事的比喻来解释复杂概念

【回答原则】
- 必须基于知识库中的文章观点，不臆造数据
- 直接给出判断，不说"这是个好问题"之类的废话
- 如果知识库中没有相关内容，直接说"这个问题超出了我目前的知识范围"
- 回答要有逻辑骨架：结论 → 依据 → 延伸

${context}`;

  // 构建对话历史
  const messages = [
    ...history.slice(-6), // 保留最近 3 轮
    { role: "user", content: message },
  ];

  try {
    const response = await client.messages.create({
      model: "claude-opus-4-6",
      max_tokens: 1024,
      system: systemPrompt,
      messages,
    });

    res.json({
      reply: response.content[0].text,
      sources: relevant.map((s) => ({ slug: s.slug, title: s.title })),
    });
  } catch (err) {
    console.error(err);
    res.status(500).json({ error: "API 调用失败：" + err.message });
  }
});

// 知识图谱数据（节点 + 边）
app.get("/api/graph", (req, res) => {
  const summaries = loadAllSummaries();
  const nodes = [];
  const links = [];
  const entityMap = new Map();

  // 文章节点
  summaries.forEach((s) => {
    nodes.push({ id: s.slug, label: s.title, type: s.type, group: "article" });
    // 实体节点 + 连线
    s.entities.forEach((e) => {
      if (!entityMap.has(e)) {
        entityMap.set(e, true);
        nodes.push({ id: `entity:${e}`, label: e, group: "entity" });
      }
      links.push({ source: s.slug, target: `entity:${e}` });
    });
  });

  res.json({ nodes, links });
});

const PORT = process.env.PORT || 3001;
app.listen(PORT, () => {
  console.log(`知奥后端运行在 http://localhost:${PORT}`);
});
