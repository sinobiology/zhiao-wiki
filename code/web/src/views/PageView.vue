<script setup>
import { ref, computed, onMounted, watch } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import MarkdownIt from 'markdown-it'

const route  = useRoute()
const router = useRouter()
const md = new MarkdownIt({ html: false, linkify: true, breaks: true })

const meta      = ref({})
const content   = ref('')
const loading   = ref(true)
const wikiIndex = ref([])

const TYPE_COLORS = {
  '技术': '#3B7DD8', '行业': '#47956A', '管理': '#7E5FAD', '感悟': '#C5961B', '产品': '#C2604A'
}

onMounted(async () => {
  try {
    wikiIndex.value = await fetch('/data/wiki-index.json').then(r => r.json())
  } catch { /* 加载失败时忽略，导航降级为 alert */ }
})

function parseFrontmatter(text) {
  if (!text.startsWith('---')) return { meta: {}, body: text }
  const parts = text.split('---')
  if (parts.length < 3) return { meta: {}, body: text }
  const fm = {}
  for (const line of parts[1].split('\n')) {
    if (!line.includes(':')) continue
    const [k, ...rest] = line.split(':')
    let v = rest.join(':').trim().replace(/^["']|["']$/g, '')
    if (v.startsWith('[') && v.endsWith(']')) {
      v = v.slice(1, -1).split(',').map(x => x.trim().replace(/^["']|["']$/g, ''))
    }
    fm[k.trim()] = v
  }
  return { meta: fm, body: parts.slice(2).join('---').trim() }
}

function renderWikiLinks(html) {
  return html.replace(/\[\[([^\]]+)\]\]/g, (_, name) =>
    `<a class="wiki-link" data-entity="${encodeURIComponent(name)}">${name}</a>`
  )
}

// 根据实体名查找对应文章 slug
function findSlugByName(name) {
  if (!wikiIndex.value.length) return null
  const lower = name.toLowerCase()
  // 1. 精确 slug 匹配
  let hit = wikiIndex.value.find(a => a.slug === name)
  if (hit) return hit.slug
  // 2. 精确标题匹配
  hit = wikiIndex.value.find(a => a.title === name)
  if (hit) return hit.slug
  // 3. 标题包含匹配
  hit = wikiIndex.value.find(a => a.title && a.title.toLowerCase().includes(lower))
  if (hit) return hit.slug
  // 4. slug 包含匹配
  hit = wikiIndex.value.find(a => a.slug && a.slug.toLowerCase().includes(lower))
  if (hit) return hit.slug
  return null
}

function navigateToEntity(name) {
  const slug = findSlugByName(name)
  if (slug) {
    router.push('/page/' + slug)
  } else {
    alert(`未找到与"${name}"相关的文章`)
  }
}

function handleClick(e) {
  const el = e.target.closest('[data-entity]')
  if (el) {
    const name = decodeURIComponent(el.dataset.entity)
    navigateToEntity(name)
  }
}

const renderedHtml = computed(() => {
  const html = md.render(content.value)
  return renderWikiLinks(html)
})

const typeBadgeColor = computed(() => TYPE_COLORS[meta.value.type] || '#999')

const categoryName = computed(() => {
  const map = { '技术': '技术与发酵', '行业': '行业分析', '管理': '管理逻辑', '感悟': '个人感悟', '产品': '产品专题' }
  return map[meta.value.type] || meta.value.type || '文章'
})

async function load(slug) {
  loading.value = true
  content.value = ''
  meta.value = {}
  try {
    const res = await fetch(`/data/pages/${encodeURIComponent(slug)}.md`)
    const text = await res.text()
    // 检测是否返回了 HTML（Vite fallback index.html）
    if (text.trimStart().startsWith('<!') || text.trimStart().toLowerCase().startsWith('<html')) {
      content.value = `未找到页面：**${slug}**\n\n该实体暂无对应的知识库页面。`
      meta.value = { title: slug }
    } else {
      const parsed = parseFrontmatter(text)
      meta.value    = parsed.meta
      content.value = parsed.body
    }
  } catch {
    content.value = '页面加载失败，请检查网络连接。'
  } finally {
    loading.value = false
  }
}

watch(() => route.params.slug, s => s && load(s), { immediate: true })
</script>

<template>
  <div>
    <!-- 面包屑 -->
    <div class="breadcrumb">
      <a @click.prevent="router.push('/')">首页</a>
      <span>/</span>
      <a v-if="meta.type" @click.prevent="router.push('/category/' + meta.type)">{{ categoryName }}</a>
      <span v-if="meta.type">/</span>
      <span>{{ meta.title || route.params.slug }}</span>
    </div>

    <!-- 页面 Hero -->
    <div class="page-hero">
      <span class="type-badge" :style="{ background: typeBadgeColor }">{{ meta.type || '文章' }}</span>
      <h1>{{ meta.title || route.params.slug }}</h1>
      <div class="date">{{ meta.created }}</div>
      <div v-if="meta.tags?.length" style="display:flex;flex-wrap:wrap;gap:6px;margin-top:10px">
        <span v-for="tag in (Array.isArray(meta.tags) ? meta.tags : [meta.tags])" :key="tag"
          style="font-size:11px;background:rgba(255,255,255,0.12);color:rgba(255,255,255,0.7);padding:2px 8px;border-radius:10px">
          # {{ tag }}
        </span>
      </div>
    </div>

    <div style="padding:24px 36px">
      <div v-if="loading" style="text-align:center;padding:60px;color:var(--text-tertiary)">加载中...</div>

      <div v-else>
        <!-- 正文 -->
        <div class="card">
          <div class="prose" @click="handleClick" v-html="renderedHtml"></div>
        </div>

        <!-- 关联实体 -->
        <div v-if="meta.entities?.length" class="card" style="margin-top:16px;padding:20px 24px">
          <div style="font-size:13px;font-weight:600;color:var(--text-secondary);margin-bottom:10px">关联实体</div>
          <div style="display:flex;flex-wrap:wrap;gap:8px">
            <span v-for="e in (Array.isArray(meta.entities) ? meta.entities : [meta.entities])" :key="e"
              style="font-size:13px;background:var(--bg-secondary);border:1px solid var(--border);padding:4px 12px;border-radius:var(--radius-pill);cursor:pointer;transition:all 0.2s"
              @click="navigateToEntity(e)">
              {{ e }}
            </span>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
