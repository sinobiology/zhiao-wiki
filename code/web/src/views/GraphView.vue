<script setup>
import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import * as d3 from 'd3'

const router = useRouter()
const svgRef = ref(null)
const stats  = ref({ nodes: 0, edges: 0 })
const loading = ref(true)

const TYPE_COLORS = {
  '技术': '#3B7DD8', '行业': '#47956A', '管理': '#7E5FAD', '感悟': '#C5961B', '产品': '#C2604A',
  '公司': '#5B8C6E', '人物': '#B07A3C', 'entity': '#7C8FA6'
}

async function buildGraph() {
  const data = await fetch('/data/graph.json').then(r => r.json())
  stats.value = { nodes: data.nodes.length, edges: data.edges.length }

  const W = svgRef.value.clientWidth
  const H = svgRef.value.clientHeight

  const svg = d3.select(svgRef.value)
  svg.selectAll('*').remove()

  const g = svg.append('g')
  svg.call(d3.zoom().scaleExtent([0.2, 5]).on('zoom', e => g.attr('transform', e.transform)))

  // build-data.py 已保证节点顺序是「文章在前、实体按引用次数降序」，
  // 所以这里截断时优先保留文章与高频实体。上限 900 可容纳
  // 「365 篇文章 + 全部 ≥3 次引用的实体」。
  const MAX_NODES = 900
  const nodes = data.nodes.slice(0, MAX_NODES).map(n => ({ ...n }))
  const nodeIds = new Set(nodes.map(n => n.id))
  const links = data.edges
    .filter(e => nodeIds.has(e.source) && nodeIds.has(e.target))
    .slice(0, 3000)
    .map(e => ({ ...e }))

  const sim = d3.forceSimulation(nodes)
    .force('link', d3.forceLink(links).id(d => d.id).distance(60))
    .force('charge', d3.forceManyBody().strength(-80))
    .force('center', d3.forceCenter(W / 2, H / 2))
    .force('collision', d3.forceCollide(12))

  const link = g.append('g').selectAll('line').data(links).join('line')
    .attr('stroke', '#E5E5EA').attr('stroke-width', 0.5)

  const node = g.append('g').selectAll('g').data(nodes).join('g')
    .attr('cursor', 'pointer')
    .call(d3.drag()
      .on('start', (e, d) => { if (!e.active) sim.alphaTarget(0.3).restart(); d.fx = d.x; d.fy = d.y })
      .on('drag',  (e, d) => { d.fx = e.x; d.fy = e.y })
      .on('end',   (e, d) => { if (!e.active) sim.alphaTarget(0); d.fx = null; d.fy = null })
    )
    .on('click', (_, d) => {
      if (d.type === 'article') {
        router.push('/page/' + d.id)
      } else if (d.hasPage) {
        // 实体节点 id 形如 entity:赖氨酸，实体页文件名就是「赖氨酸.md」
        router.push('/page/' + encodeURIComponent(d.id.replace(/^entity:/, '')))
      }
    })

  node.append('circle')
    .attr('r', d => d.type === 'article' ? 6 : (d.hasPage ? 4 : 2.5))
    .attr('fill', d => d.type === 'entity'
      ? (d.hasPage ? '#7C8FA6' : '#CBD5E1')
      : (TYPE_COLORS[d.group] || '#94A3B8'))
    .attr('stroke', '#fff').attr('stroke-width', 1.5)

  node.filter(d => d.type === 'article').append('text')
    .text(d => d.label.slice(0, 10))
    .attr('x', 8).attr('y', 4)
    .attr('font-size', '9px').attr('fill', '#6B6B6B')

  sim.on('tick', () => {
    link.attr('x1', d => d.source.x).attr('y1', d => d.source.y)
        .attr('x2', d => d.target.x).attr('y2', d => d.target.y)
    node.attr('transform', d => `translate(${d.x},${d.y})`)
  })

  loading.value = false
}

onMounted(buildGraph)
</script>

<template>
  <div style="display:flex;flex-direction:column;height:100%;width:100%;overflow:hidden">
    <div class="page-hero" style="padding:20px 36px;flex-shrink:0">
      <h1 style="font-size:20px">知识图谱</h1>
      <p style="font-size:13px;color:rgba(255,255,255,0.5);margin-top:4px">
        {{ stats.nodes }} 节点 · {{ stats.edges }} 条边 · 点击文章或实体节点查看详情
      </p>
    </div>

    <!-- 图例 -->
    <div style="padding:12px 36px;background:var(--bg-primary);border-bottom:1px solid var(--border-light);display:flex;gap:20px;flex-wrap:wrap;flex-shrink:0">
      <span v-for="(color, type) in { '技术':'#3B7DD8','行业':'#47956A','管理':'#7E5FAD','感悟':'#C5961B','产品':'#C2604A','实体(可打开)':'#7C8FA6','实体(无页)':'#CBD5E1' }" :key="type"
        style="display:flex;align-items:center;gap:5px;font-size:12px;color:var(--text-secondary)">
        <span :style="{ background: color }" style="width:8px;height:8px;border-radius:50%;display:inline-block"></span>
        {{ type }}
      </span>
    </div>

    <div style="flex:1;position:relative;background:var(--bg-primary);min-height:0">
      <div v-if="loading" style="position:absolute;inset:0;display:flex;align-items:center;justify-content:center;color:var(--text-tertiary)">
        加载图谱中...
      </div>
      <svg ref="svgRef" style="width:100%;height:100%;display:block"></svg>
    </div>
  </div>
</template>
