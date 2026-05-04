<script setup>
import { ref, onMounted } from 'vue'
import * as d3 from 'd3'

const emit = defineEmits(['open'])
const svgRef = ref(null)
const loading = ref(true)

async function buildGraph() {
  const res = await fetch('/api/graph')
  const { nodes, links } = await res.json()

  const width = svgRef.value.clientWidth
  const height = svgRef.value.clientHeight

  const svg = d3.select(svgRef.value)
  svg.selectAll('*').remove()

  // 缩放容器
  const g = svg.append('g')
  svg.call(d3.zoom().scaleExtent([0.2, 4]).on('zoom', e => g.attr('transform', e.transform)))

  const sim = d3.forceSimulation(nodes)
    .force('link', d3.forceLink(links).id(d => d.id).distance(80))
    .force('charge', d3.forceManyBody().strength(-120))
    .force('center', d3.forceCenter(width / 2, height / 2))
    .force('collision', d3.forceCollide(20))

  // 边
  const link = g.append('g')
    .selectAll('line')
    .data(links)
    .join('line')
    .attr('stroke', '#CBD5E1')
    .attr('stroke-width', 1)

  // 节点
  const node = g.append('g')
    .selectAll('g')
    .data(nodes)
    .join('g')
    .attr('cursor', 'pointer')
    .call(d3.drag()
      .on('start', (e, d) => { if (!e.active) sim.alphaTarget(0.3).restart(); d.fx = d.x; d.fy = d.y })
      .on('drag',  (e, d) => { d.fx = e.x; d.fy = e.y })
      .on('end',   (e, d) => { if (!e.active) sim.alphaTarget(0); d.fx = null; d.fy = null })
    )
    .on('click', (_, d) => { if (d.group === 'article') emit('open', d.id) })

  node.append('circle')
    .attr('r', d => d.group === 'article' ? 8 : 5)
    .attr('fill', d => d.group === 'article' ? '#3B82F6' : '#10B981')
    .attr('stroke', '#fff')
    .attr('stroke-width', 1.5)

  node.append('text')
    .text(d => d.label.slice(0, 12))
    .attr('x', 10)
    .attr('y', 4)
    .attr('font-size', '10px')
    .attr('fill', '#475569')

  sim.on('tick', () => {
    link
      .attr('x1', d => d.source.x).attr('y1', d => d.source.y)
      .attr('x2', d => d.target.x).attr('y2', d => d.target.y)
    node.attr('transform', d => `translate(${d.x},${d.y})`)
  })

  loading.value = false
}

onMounted(buildGraph)
</script>

<template>
  <div class="flex flex-col h-full">
    <div class="px-6 py-4 border-b border-slate-200 bg-white">
      <h1 class="text-xl font-bold text-slate-800">知识图谱</h1>
      <p class="text-sm text-slate-500 mt-0.5">蓝色节点 = 文章，绿色节点 = 实体。点击文章节点可查看详情。</p>
    </div>
    <div class="flex-1 relative">
      <div v-if="loading" class="absolute inset-0 flex items-center justify-center text-slate-400">
        加载图谱中...
      </div>
      <svg ref="svgRef" class="w-full h-full"></svg>
    </div>
  </div>
</template>
