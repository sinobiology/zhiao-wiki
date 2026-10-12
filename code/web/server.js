/**
 * server.js — 知奥ZHAO 知识库后端
 * 启动: node --env-file=.env server.js
 */
import express from 'express'
import cors from 'cors'
import fs from 'fs'
import path from 'path'
import { fileURLToPath } from 'url'

const __dirname = path.dirname(fileURLToPath(import.meta.url))
const DATA_DIR  = path.join(__dirname, 'public', 'data')
const PAGES_DIR = path.join(DATA_DIR, 'pages')

const app = express()
app.use(cors())
app.use(express.json())

// ── 模型配置（DeepSeek，OpenAI 兼容接口）─────────────────────────────────────
// 只用 Node 内置 fetch，不再依赖 @anthropic-ai/sdk
const LLM_BASE_URL = (process.env.LLM_BASE_URL || 'https://api.deepseek.com/v1').replace(/\/+$/, '')
const LLM_API_KEY  = process.env.DEEPSEEK_API_KEY || process.env.LLM_API_KEY
const MODEL        = process.env.LLM_MODEL || 'deepseek-v4-pro'
const THINKING_OFF = (process.env.LLM_THINKING || 'disabled').toLowerCase() === 'disabled'
// deepseek-v4-pro / flash 均为推理模型，思考链与正文共享 max_tokens，给少会「静默返回空正文」
const MAX_TOKENS   = Number(process.env.LLM_MAX_TOKENS || 2048)
const PASSWORD     = process.env.ACCESS_PASSWORD || 'zhiao2026'

if (!LLM_API_KEY) console.warn('⚠️  未配置 DEEPSEEK_API_KEY，/api/chat 将不可用')

// ── 启动时预加载数据 ──────────────────────────────────────────────────────────
let wikiIndex = []
let graphData  = { nodes: [], edges: [] }
let neighbors  = {}   // slug → Set<slug>
let indexByTitle = {} // title → slug
let indexBySlug  = {} // slug → page
let hayCache     = null   // DF 语料缓存（title + excerpt），loadData 后失效重建
const dfCache    = new Map()  // gram → 文档频率

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
    // 构建索引
    indexByTitle = {}
    indexBySlug  = {}
    for (const p of wikiIndex) {
      indexByTitle[p.title] = p.slug
      indexBySlug[p.slug]  = p
    }
    console.log(`预加载: ${wikiIndex.length} 页面, ${graphData.nodes.length} 节点, ${graphData.edges.length} 边`)
    hayCache = null          // 数据换了，DF 语料与缓存必须重建
    dfCache.clear()
  } catch (e) {
    console.error('数据加载失败:', e.message)
  }
}
loadData()

// ── 检索：DF 加权 ngram（两阶段）──────────────────────────────────────────────
// 中文无空格，用 2–4 字滑窗 ngram 匹配，不引入分词库。代价是会造出大量通用
// 碎片（「说的」「他是」），它们在长文里到处命中、把不相关的页顶到前面。
// 但也不能一刀切剪掉 2 字词——「发酵」「赖氨酸」正是 2-3 字，剪掉会漏掉真正
// 相关的页。所以用「文档频率」(DF) 判断区分度：在语料里出现超过 60% 的 gram
// 视为无区分度、弃用。实测本库：「发酵」23%、「赖氨酸」6%、「行业」60%
// 都在阈值内，而被误算成 100% 的只有摘要章节标题（已在 build-data.py 侧剥离）。
const DF_MAX = 0.6
const PUNCT  = /[\s，。？！、；：""''“”‘’（）【】《》,.?!\-—·「」『』…～~:;()\[\]"'`|/\\*=#]+/g

// 停用词：虚词、问句框架词、无区分度的连接词。
// 「怎么做 / 是什么 / 什么关系」这类是每个提问都可能带的框架，不含主题信息，
// 但长度 3 字会被长度加权放大 → 必须显式停用（DF 过滤拦不住它们，实测 DF 仅 1%）。
const STOP = new Set([
  '一个','一直','已经','还是','只是','就是','可以','需要','应该','我们','他们','自己',
  '什么','怎么','如何','哪些','哪个','哪里','多少','为何',
  '这个','那个','一些','这些','那些','这样','那样','时候','没有','不能','不会',
  '因为','所以','但是','如果','那么','为了','对于','关于','通过','进行','以及',
  '怎么做','怎么办','是什么','什么关系','怎么样','有哪些','哪一个','怎么说',
  '什么区别','意味着什么','为什么','不是','而是','以及','并且','而且','然后',
])

// 生成摘要时写入的章节标题，几乎每篇都有，不能参与评分
const BOILER = new Set([
  '核心逻辑','心逻辑','核心逻','行业洞察','业洞察','技术管理','管理要点','金句归纳',
  '句归纳','关联实体','关联实','性要点','术管理',
])

// 问句框架：切 gram 前先从查询里整体剥掉。
// 「量本利的囚徒讲的是什么」若不剥离，会切出「讲的是 / 的是 / 是什」等碎片，
// 任何含「讲的是」「是什么」的页面都会命中并拿到 3 字权重（实测把《百年味之素》
// 这类无关页顶进候选）。剥离后只留实词，碎片消失。
const Q_FRAME = /(讲的是什么|说的是什么|指的是什么|是什么意思|意味着什么|什么是|是什么|什么关系|有什么区别|有何区别|主要内容|到底|究竟|怎么样|怎么办|怎么做|怎么理解|如何理解|如何|为什么|有哪些|哪一个|讲的是|说的是|指的是|吗|呢|吧)/g

function ngrams(text, min = 2, max = 4) {
  const tokens = new Set()
  const clean  = text.toLowerCase().replace(PUNCT, '')
  for (let n = min; n <= max; n++) {
    for (let i = 0; i + n <= clean.length; i++) tokens.add(clean.slice(i, i + n))
  }
  // 英文/数字整词（中文以外）
  for (const w of text.toLowerCase().split(PUNCT)) {
    if (w.length >= 2 && /[a-z0-9]/.test(w)) tokens.add(w)
  }
  return tokens
}

// DF 语料 = 每页的 title + excerpt（与检索打分同一空间）
function buildHay() {
  if (hayCache) return hayCache
  hayCache = wikiIndex.map(p => ((p.title || '') + ' ' + (p.excerpt || '')).toLowerCase())
  return hayCache
}

function docFreq(g) {
  if (dfCache.has(g)) return dfCache.get(g)
  const hay = buildHay()
  let c = 0
  for (const h of hay) if (h.includes(g)) c++
  const r = hay.length ? c / hay.length : 1
  dfCache.set(g, r)
  return r
}

// 该 gram 是否可用于评分：非停用、非样板、具备区分度
function usable(g) {
  if (g.length < 2) return false
  if (STOP.has(g) || BOILER.has(g)) return false
  return docFreq(g) <= DF_MAX
}

/**
 * 返回 { s, strong }。strong = 真的命中了查询，而不是靠某个通用碎片蹭上的。
 * 背景：原来只要任意 1 个 gram 命中就计分，而正文里满是 2 字组合，长问句会
 * 恒定命中大量页面、前排混着不相关的页。改为：命中 ≥3 字 gram、或标题整词
 * 命中、或 ≥2 个不同 2 字词命中，才算 strong。
 */
function scorePage(p, q, grams) {
  let s = 0
  let strong = q.length <= 2        // 2 字查询本身已是最长 gram
  let hit2 = 0
  const title = (p.title || '').toLowerCase()
  const ex    = (p.excerpt || '').toLowerCase()

  if (q.length >= 2 && title.includes(q)) { s += 50; strong = true }
  if (title.length >= 2 && q.includes(title)) { s += 40; strong = true }

  for (const g of grams) {
    if (!usable(g)) continue
    const w = g.length >= 4 ? 3 : (g.length === 3 ? 2 : 1)   // 长度加权
    let hit = false
    if (title.includes(g)) { s += 8 * w; hit = true }
    else if (ex.includes(g)) { s += 3 * w; hit = true }
    if (hit) { if (g.length >= 3) strong = true; else hit2++ }
  }
  if (hit2 >= 2) strong = true

  for (const lk of new Set(p.links || [])) {       // links 已去重，这里再兜一层
    if (lk.length >= 2 && q.includes(lk.toLowerCase())) { s += 6; strong = true }
  }
  return { s, strong }
}

function retrieve(query, topN = 6) {
  const q     = query.toLowerCase()
  // 先剥疑问框架再切 gram；若剥完全是空的（query 本身全是框架词），回退用原串
  const qCore = q.replace(Q_FRAME, '').trim()
  const grams = ngrams(qCore || q)

  const all = []
  for (const p of wikiIndex) {
    const r = scorePage(p, q, grams)
    if (r.s > 0) all.push({ p, s: r.s, strong: r.strong })
  }
  all.sort((a, b) => b.s - a.s)

  // strong 优先；不足 4 篇时用普通命中补齐，但设分数门槛（≥8 分，即至少一个
  // 标题命中或一个正文 3 字命中），避免只蹭到单个碎片的页混进上下文。
  const MIN_FALLBACK = 8
  const picked = all.filter(x => x.strong).slice(0, 4)
  if (picked.length < 4) {
    const seen = new Set(picked.map(x => x.p.slug))
    for (const x of all) {
      if (picked.length >= 4) break
      if (x.s < MIN_FALLBACK || seen.has(x.p.slug)) continue
      picked.push(x); seen.add(x.p.slug)
    }
  }
  const direct = picked.map(x => x.p)
  const directSlugs = new Set(direct.map(p => p.slug))

  // 阶段 2：图谱扩展必须走「文章 → 实体 → 其他文章」二跳：
  // graph 的边是「文章 ↔ 实体」，直接遍历 neighbors[p.slug] 拿到的全是
  // entity:* ，若在此处 continue 掉，这一阶段就永远为空（历史 bug）。
  const candidates = new Map()
  for (const p of direct) {
    for (const ent of (neighbors[p.slug] || [])) {
      if (!ent.startsWith('entity:')) continue
      for (const nb of (neighbors[ent] || [])) {
        if (directSlugs.has(nb) || nb.startsWith('entity:')) continue
        const nbPage = indexBySlug[nb]
        if (!nbPage) continue
        let nbScore = 0
        const nTitle = (nbPage.title || '').toLowerCase()
        const nEx    = (nbPage.excerpt || '').toLowerCase()
        for (const g of grams) {
          if (!usable(g)) continue
          if (nTitle.includes(g))   nbScore += 4
          else if (nEx.includes(g)) nbScore += 1
        }
        if (nbScore >= 4) {                  // 门槛：至少一个有区分度的实词命中
          const prev = candidates.get(nb)
          if (!prev || prev.score < nbScore) candidates.set(nb, { page: nbPage, score: nbScore })
        }
      }
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
    const upstream = await fetch(`${LLM_BASE_URL}/chat/completions`, {
      method: 'POST',
      headers: {
        'Authorization': `Bearer ${LLM_API_KEY}`,
        'Content-Type':  'application/json',
      },
      body: JSON.stringify({
        model: MODEL,
        max_tokens: MAX_TOKENS,
        stream: true,
        ...(THINKING_OFF ? { thinking: { type: 'disabled' } } : {}),
        messages: [{ role: 'system', content: systemPrompt }, ...messages],
      }),
    })

    if (!upstream.ok) {
      const detail = await upstream.text().catch(() => '')
      throw new Error(`上游 ${upstream.status}：${detail.slice(0, 300)}`)
    }

    const reader  = upstream.body.getReader()
    const decoder = new TextDecoder()
    let buffer = ''

    while (true) {
      const { done, value } = await reader.read()
      if (done) break
      buffer += decoder.decode(value, { stream: true })

      const lines = buffer.split('\n')
      buffer = lines.pop()              // 末行可能不完整，留到下一轮
      for (const line of lines) {
        const s = line.trim()
        if (!s.startsWith('data:')) continue
        const payload = s.slice(5).trim()
        if (!payload || payload === '[DONE]') continue
        let chunk
        try { chunk = JSON.parse(payload) } catch { continue }
        // 推理模型的思考链走 reasoning_content，不发给前端
        const text = chunk.choices?.[0]?.delta?.content
        if (text) res.write(`data: ${JSON.stringify({ text })}\n\n`)
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
