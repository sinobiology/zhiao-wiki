<script setup>
import { ref, watch } from 'vue'

const props = defineProps({ slug: String })
const emit = defineEmits(['back', 'open'])

const article = ref(null)
const loading = ref(false)

async function load(slug) {
  if (!slug) return
  loading.value = true
  try {
    const res = await fetch(`/api/articles/${encodeURIComponent(slug)}`)
    article.value = await res.json()
  } finally {
    loading.value = false
  }
}

// 将 [[链接]] 转为可点击的 span
function renderWikiLinks(text) {
  return text.replace(/\[\[([^\]]+)\]\]/g, (_, name) =>
    `<span class="wiki-link" data-entity="${name}">[[${name}]]</span>`
  )
}

function handleClick(e) {
  const el = e.target.closest('[data-entity]')
  if (el) {
    // 未来可跳转到实体页
    console.log('entity:', el.dataset.entity)
  }
}

watch(() => props.slug, load, { immediate: true })
</script>

<template>
  <div class="max-w-3xl mx-auto p-6">
    <!-- 返回 -->
    <button
      @click="emit('back')"
      class="flex items-center gap-2 text-sm text-slate-500 hover:text-blue-600 mb-6 transition-colors"
    >
      ← 返回文章列表
    </button>

    <div v-if="loading" class="text-center py-20 text-slate-400">加载中...</div>

    <div v-else-if="article">
      <!-- 元数据 -->
      <div class="mb-6">
        <div class="flex items-center gap-2 mb-2">
          <span class="text-xs bg-blue-100 text-blue-700 px-2 py-0.5 rounded-full font-medium">
            {{ article.meta?.type || '未分类' }}
          </span>
          <span class="text-xs text-slate-400">{{ article.meta?.created }}</span>
        </div>
        <h1 class="text-2xl font-bold text-slate-800">{{ article.meta?.title }}</h1>
        <div class="flex flex-wrap gap-1 mt-3">
          <span
            v-for="tag in (article.meta?.tags || [])"
            :key="tag"
            class="text-xs bg-slate-100 text-slate-500 px-2 py-0.5 rounded"
          ># {{ tag }}</span>
        </div>
      </div>

      <!-- 正文（Wiki 内容） -->
      <div
        class="prose-wiki bg-white rounded-xl p-6 border border-slate-100 shadow-sm"
        @click="handleClick"
        v-html="renderWikiLinks(article.content || '')"
      ></div>

      <!-- 关联实体 -->
      <div v-if="article.meta?.entities?.length" class="mt-4 p-4 bg-slate-50 rounded-xl border border-slate-100">
        <div class="text-xs font-semibold text-slate-500 mb-2">关联实体</div>
        <div class="flex flex-wrap gap-2">
          <span
            v-for="e in article.meta.entities"
            :key="e"
            class="text-xs bg-white border border-slate-200 text-slate-600 px-2 py-1 rounded-lg hover:border-blue-300 cursor-pointer"
          >{{ e }}</span>
        </div>
      </div>
    </div>
  </div>
</template>
