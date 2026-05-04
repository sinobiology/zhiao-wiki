/**
 * server.js — 知奥ZHAO 知识库后端
 * 启动: node --env-file=.env server.js
 */
import express from 'express'
import cors from 'cors'
import fs from 'fs'
import path from 'path'
import { fileURLToPath } from 'url'
import Anthropic from '@anthropic-ai/sdk'

const __dirname = path.dirname(fileURLToPath(import.meta.url))
const DATA_DIR  = path.join(__dirname, 'public', 'data')
const PAGES_DIR = path.join(DATA_DIR, 'pages')

const app = express()
app.use(cors())
app.use(express.json())

const client = new Anthropic({
  apiKey:  process.env.ANTHROPIC_API_KEY,
  ...(process.env.ANTHROPIC_BASE_URL ? { baseURL: process.env.ANTHROPIC_BASE_URL } : {}),
})
const MODEL    = process.env.ANTHROPIC_MODEL || 'claude-opus-4-6'
const PASSWORD = process.env.ACCESS_PASSWORD || 'zhiao2026'

// ── 启动时预加载数据 ──────────────────────────────────────────────────────────
let wikiIndex = []
let graphData  = { nodes: [], edges: [] }
let neighbors  = {}   // slug → Set<slug>
let indexByTitle = {} // title → slug

function loadData() {
  try {
    wikiIndex   = JSON.parse(fs.readFileSync(path.join(DATA_DIR, 'wiki-index.json'), 'utf-8'))
    graphData   = JSON.parse(fs.readFileSync(path.join(DATA_DIR, 'graph.json'), 'utf-8'))
    // 构建邻接表
    neighbors = {}
    for (const e of graphData.edges) {
      if (!neighbors[e.source]) neighbors[e.source] = new Set()
      if (!neighbors[e.target]) neighbors[e.target] = new Set()
      neighbors[e.source].add(e.target)
      neighbors[e.target].add(e.source)
    }
    // 构建 title 索引
    indexByTitle = {}
    for (const p of wikiIndex) {
      indexByTitle[p.title] = p.slug
    }
    console.log(`预加载: ${wikiIndex.length} 页面, ${graphData.nodes.length} 节点, ${graphData.edges.length} 边`)
  } catch (e) {
    console.error('数据加载失败:', e.message)
  }
}
loadData()

// ── 两阶段检索 ────────────────────────────────────────────────────────────────
function ngrams(text, min = 2, max = 4) {
  const tokens = new Set()
  for (let n = min; n <= max; n++) {
    for (let i = 0; i <= text.length - n; i++) tokens.add(text.slice(i, i + n))
  }
  for (const w of text.split(/\s+/)) {
    if (w.length >= 2) tokens.add(w.toLowerCase())
  }
  return tokens
}

function retrieve(query, topN = 6) {
  const qTokens = ngrams(query)
  const qLower  = query.toLowerCase()
  const scored = wikiIndex.map(p => {
    let score = 0
    const titleLower = p.title.toLowerCase()
    if (titleLower.includes(qLower))  score += 50
    if (qLower.includes(titleLower))  score += 40
    for (const t of qTokens) {
      if (p.title.includes(t))   score += 8
      if (p.excerpt.includes(t)) score += 3
    }
    for (const link of (p.links || [])) {
      if (query.includes(link) || link.includes(query.slice(0, 4))) score += 6
    }
    return { ...p, score }
  }).filter(p => p.score > 0).sort((a, b) => b.score - a.score)

  const direct = scored.slice(0, 4)
  const directSlugs = new Set(direct.map(p => p.slug))
  const candidates  = new Map()
  for (const p of direct) {
    for (const nb of (neighbors[p.slug] || [])) {
      if (directSlugs.has(nb) || nb.startsWith('entity:')) continue
      const nbPage = wikiIndex.find(x => x.slug === nb)
      if (!nbPage) continue
      let nbScore = 0
      for (const t of qTokens) {
        if (nbPage.title.includes(t))   nbScore += 4
        if (nbPage.excerpt.includes(t)) nbScore += 1
      }
      if (nbScore > 0) candidates.set(nb, { page: nbPage, score: nbScore })
    }
  }
  const extra = [...candidates.values()]
    .sort((a, b) => b.score - a.score).slice(0, 2).map(x => x.page)
  return [...direct, ...extra].slice(0, topN)
}

function loadPageContent(slug) {
  const fp = path.join(PAGES_DIR, `${slug}.md`)
  if (!fs.existsSync(fp)) return ''
  return fs.readFileSync(fp, 'utf-8').slice(0, 3000)
}

// ── API 路由 ──────────────────────────────────────────────────────────────────

// 密码验证
app.post('/api/verify-password', (req, res) => {
  const { password } = req.body
  if (password === PASSWORD) {
    res.json({ ok: true })
  } else {
    res.status(401).json({ ok: false, error: '密码错误' })
  }
})

// AI 知奥对话（SSE 流式）
app.post('/api/chat', async (req, res) => {
  const { message, history = [], password } = req.body
  if (password !== PASSWORD) return res.status(401).json({ error: '未授权' })
  if (!message) return res.status(400).json({ error: 'message 不能为空' })

  // 检索相关页面
  const hits = retrieve(message)
  let context = ''
  if (hits.length > 0) {
    context = '【相关知识库内容】\n'
    for (const h of hits) {
      const content = loadPageContent(h.slug)
      if (content) context += `\n### ${h.title}\n${content}\n`
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
- 直接给出判断，不说废话
- 如果知识库中没有相关内容，直接说明
- 回答要有逻辑骨架：结论 → 依据 → 延伸

${context}`

  const messages = [
    ...history.slice(-6),
    { role: 'user', content: message },
  ]

  // SSE 响应头
  res.setHeader('Content-Type', 'text/event-stream')
  res.setHeader('Cache-Control', 'no-cache')
  res.setHeader('Connection', 'keep-alive')

  try {
    const stream = client.messages.stream({
      model: MODEL,
      max_tokens: 1024,
      system: systemPrompt,
      messages,
    })

    for await (const chunk of stream) {
      if (chunk.type === 'content_block_delta' && chunk.delta?.text) {
        res.write(`data: ${JSON.stringify({ text: chunk.delta.text })}\n\n`)
      }
    }

    const sources = hits.map(h => ({ slug: h.slug, title: h.title }))
    res.write(`data: ${JSON.stringify({ done: true, sources })}\n\n`)
  } catch (err) {
    res.write(`data: ${JSON.stringify({ error: err.message })}\n\n`)
  } finally {
    res.end()
  }
})

// ── 生产环境托管前端静态文件 ──────────────────────────────────────────────────
if (process.env.NODE_ENV === 'production') {
  const distDir = path.join(__dirname, 'dist')
  // 托管 public/data（wiki JSON + md 页面文件）
  app.use('/data', express.static(path.join(__dirname, 'public', 'data')))
  // 托管前端构建产物
  app.use(express.static(distDir))
  // SPA fallback
  app.get('*', (req, res) => {
    res.sendFile(path.join(distDir, 'index.html'))
  })
}

const PORT = process.env.PORT || 3001
app.listen(PORT, () => console.log(`知奥后端运行在 http://localhost:${PORT}`))
