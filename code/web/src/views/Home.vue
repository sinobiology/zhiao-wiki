<script setup>
import { ref, computed, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import * as d3 from 'd3'

const router = useRouter()
const wikiIndex  = ref([])
const graphData  = ref({ nodes: [], edges: [] })
const searchQ    = ref('')
const miniSvg    = ref(null)
const searchWrap = ref(null)

function searchEntity(name) {
  searchQ.value = name
  searchWrap.value?.scrollIntoView({ behavior: 'smooth', block: 'center' })
}

const TYPE_COLORS = {
  '技术': '#3B7DD8', '行业': '#47956A', '管理': '#7E5FAD', '感悟': '#C5961B', '产品': '#C2604A'
}
const STAT_COLORS = ['#C2604A', '#3B7DD8', '#47956A', '#7E5FAD']

const stats = computed(() => {
  const total = wikiIndex.value.length
  const counts = {}
  for (const a of wikiIndex.value) counts[a.type] = (counts[a.type] || 0) + 1
  return [
    { icon: '📄', num: total,              label: '文章总数',   color: STAT_COLORS[0], type: null },
    { icon: '🔬', num: counts['技术'] || 0, label: '技术与发酵', color: STAT_COLORS[1], type: '技术' },
    { icon: '📊', num: counts['行业'] || 0, label: '行业分析',   color: STAT_COLORS[2], type: '行业' },
    { icon: '💭', num: counts['感悟'] || 0, label: '个人感悟',   color: STAT_COLORS[3], type: '感悟' },
  ]
})

// TOP 15 实体（按引用次数）
const topEntities = computed(() => {
  const refCount = {}
  for (const a of wikiIndex.value) {
    for (const link of (a.links || [])) {
      refCount[link] = (refCount[link] || 0) + 1
    }
  }
  return Object.entries(refCount)
    .sort((a, b) => b[1] - a[1])
    .slice(0, 15)
    .map(([name, count]) => ({ name, count }))
})

// TOP 15 行业公司（实体中的公司类）
const topCompanies = computed(() => {
  const companyKeywords = ['生物', '集团', '公司', '科技', '发酵', '化工', '农业', '食品']
  return topEntities.value
    .filter(e => companyKeywords.some(k => e.name.includes(k)))
    .slice(0, 15)
})

// 搜索结果
const searchResults = computed(() => {
  if (!searchQ.value.trim()) return []
  const q = searchQ.value.toLowerCase()
  return wikiIndex.value
    .filter(a => a.title.toLowerCase().includes(q) || a.excerpt.toLowerCase().includes(q) || a.tags.some(t => t.includes(q)))
    .slice(0, 8)
})

// 时间线数据
const timelineItems = computed(() => {
  return wikiIndex.value
    .filter(a => a.created)
    .map(a => ({ ...a, year: parseInt(a.created.slice(0, 4)) }))
    .filter(a => a.year >= 2024)
    .sort((a, b) => a.created.localeCompare(b.created))
})

async function loadData() {
  const [idx, graph] = await Promise.all([
    fetch('/data/wiki-index.json').then(r => r.json()),
    fetch('/data/graph.json').then(r => r.json()),
  ])
  wikiIndex.value = idx
  graphData.value = graph
  buildMiniGraph()
}

function buildMiniGraph() {
  if (!miniSvg.value) return
  const W = 240, H = 150
  const svg = d3.select(miniSvg.value).attr('width', W).attr('height', H)
  svg.selectAll('*').remove()

  // 取前 40 个节点做迷你图
  const nodes = graphData.value.nodes.slice(0, 40).map(n => ({ ...n }))
  const nodeIds = new Set(nodes.map(n => n.id))
  const links = graphData.value.edges
    .filter(e => nodeIds.has(e.source) && nodeIds.has(e.target))
    .slice(0, 60)
    .map(e => ({ ...e }))

  const sim = d3.forceSimulation(nodes)
    .force('link', d3.forceLink(links).id(d => d.id).distance(20))
    .force('charge', d3.forceManyBody().strength(-30))
    .force('center', d3.forceCenter(W / 2, H / 2))

  const g = svg.append('g')
  const line = g.append('g').selectAll('line').data(links).join('line')
    .attr('stroke', 'rgba(255,255,255,0.2)').attr('stroke-width', 0.5)

  const node = g.append('g').selectAll('circle').data(nodes).join('circle')
    .attr('r', 3)
    .attr('fill', d => TYPE_COLORS[d.group] || '#568DE5')
    .attr('stroke', 'rgba(255,255,255,0.4)').attr('stroke-width', 0.5)

  let tick = 0
  sim.on('tick', () => {
    tick++
    if (tick > 80) sim.stop()
    line.attr('x1', d => d.source.x).attr('y1', d => d.source.y)
        .attr('x2', d => d.target.x).attr('y2', d => d.target.y)
    node.attr('cx', d => d.x).attr('cy', d => d.y)
  })
}

onMounted(loadData)
</script>

<template>
  <div>
    <!-- Hero -->
    <div class="hero" style="display:flex;align-items:center;justify-content:space-between">
      <div>
        <h1>知奥ZHAO：工业生物技术数字大脑</h1>
        <p>基于 Karpathy LLM Wiki 模式 · {{ wikiIndex.length }} 篇文章预编译为结构化知识</p>
        <div style="display:flex;gap:12px;margin-top:18px">
          <button @click="router.push('/chat')"
            style="background:#C5961B;color:#fff;border:none;padding:9px 20px;border-radius:22px;font-size:14px;font-weight:600;cursor:pointer">
            🤖 问 AI 知奥
          </button>
          <button @click="router.push('/graph')"
            style="background:rgba(255,255,255,0.12);color:#fff;border:1px solid rgba(255,255,255,0.3);padding:9px 20px;border-radius:22px;font-size:14px;cursor:pointer">
            🕸️ 探索知识图谱
          </button>
        </div>
      </div>
      <svg ref="miniSvg" style="flex-shrink:0;opacity:0.85"></svg>
    </div>

    <!-- 统计卡片 -->
    <div class="stats-grid">
      <div v-for="s in stats" :key="s.label" class="stat-card"
        :style="{ '--bar-color': s.color }"
        style="--bar-color: var(--bar-color)"
        @click="s.type && router.push('/category/' + s.type)">
        <div style="position:absolute;top:0;left:0;right:0;height:3px" :style="{ background: s.color }"></div>
        <div class="stat-row">
          <span class="stat-icon">{{ s.icon }}</span>
          <span class="stat-num">{{ s.num }}</span>
        </div>
        <div class="stat-label">{{ s.label }}</div>
      </div>
    </div>

    <!-- 搜索 -->
    <div class="search-wrap" ref="searchWrap">
      <div class="search-box">
        <span>🔍</span>
        <input v-model="searchQ" placeholder="搜索文章、实体、标签..." />
      </div>
      <div v-if="searchResults.length" style="margin-top:8px;background:#fff;border-radius:12px;border:1px solid var(--border-light);overflow:hidden">
        <div v-for="r in searchResults" :key="r.slug"
          class="page-list-item" @click="router.push('/page/' + r.slug)">
          <div>
            <span :style="{ color: TYPE_COLORS[r.type] }" style="font-size:12px;font-weight:600;margin-right:8px">{{ r.type }}</span>
            <span style="font-size:14px;font-weight:500">{{ r.title }}</span>
          </div>
          <span style="font-size:12px;color:var(--text-tertiary)">{{ r.created }}</span>
        </div>
      </div>
    </div>

    <!-- TOP 15 核心实体 -->
    <div class="section">
      <div class="section-block concept-block">
        <div class="section-header">
          <span class="section-title gold">核心实体</span>
          <span class="section-sub">TOP 15</span>
        </div>
        <div class="chips">
          <div v-for="e in topEntities" :key="e.name" class="chip" @click="searchEntity(e.name)">
            {{ e.name }}
            <span class="chip-badge gold">{{ e.count }}</span>
          </div>
        </div>
      </div>
    </div>

    <!-- TOP 15 行业公司 -->
    <div class="section" v-if="topCompanies.length">
      <div class="section-block company-block">
        <div class="section-header">
          <span class="section-title green">行业公司</span>
          <span class="section-sub">TOP {{ topCompanies.length }}</span>
        </div>
        <div class="chips">
          <div v-for="e in topCompanies" :key="e.name" class="chip" @click="searchEntity(e.name)">
            {{ e.name }}
            <span class="chip-badge green">{{ e.count }}</span>
          </div>
        </div>
      </div>
    </div>

    <!-- 时间线 -->
    <div class="section">
      <div class="card" style="padding:24px 28px">
        <div style="font-size:16px;font-weight:700;margin-bottom:16px">文章时间线</div>
        <div class="timeline-wrap">
          <div class="timeline-line"></div>
          <div v-for="(item, i) in timelineItems" :key="item.slug"
            class="timeline-dot"
            :style="{
              left: (i / Math.max(timelineItems.length - 1, 1) * 100) + '%',
              background: TYPE_COLORS[item.type] || '#999'
            }"
            :title="item.title"
            @click="router.push('/page/' + item.slug)"
          ></div>
        </div>
        <div style="display:flex;gap:16px;margin-top:12px;flex-wrap:wrap">
          <span v-for="(color, type) in TYPE_COLORS" :key="type"
            style="display:flex;align-items:center;gap:4px;font-size:12px;color:var(--text-secondary)">
            <span :style="{ background: color }" style="width:8px;height:8px;border-radius:50%;display:inline-block"></span>
            {{ type }}
          </span>
        </div>
      </div>
    </div>

    <!-- 快速导航 -->
    <div class="section">
      <div class="card" style="padding:24px 28px">
        <div style="font-size:16px;font-weight:700;margin-bottom:16px">快速导航</div>
        <div style="display:grid;grid-template-columns:repeat(3,1fr);gap:10px">
          <button v-for="t in [['🔬','技术与发酵','技术'],['📊','行业分析','行业'],['💼','管理逻辑','管理'],['💭','个人感悟','感悟'],['🧪','产品专题','产品'],['🕸️','知识图谱',null]]"
            :key="t[1]"
            @click="t[2] ? router.push('/category/'+t[2]) : router.push('/graph')"
            style="display:flex;align-items:center;gap:8px;padding:12px 14px;background:var(--bg-secondary);border:1px solid var(--border-light);border-radius:var(--radius-md);cursor:pointer;font-size:14px;transition:all 0.2s ease"
            onmouseover="this.style.borderColor='var(--accent)';this.style.transform='translateY(-2px)'"
            onmouseout="this.style.borderColor='var(--border-light)';this.style.transform=''"
          >
            {{ t[0] }} {{ t[1] }}
          </button>
        </div>
      </div>
    </div>
  </div>
</template>
