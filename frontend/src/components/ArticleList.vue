<script setup>
import { ref, computed } from 'vue'

const props = defineProps({ articles: Array })
const emit = defineEmits(['open'])

const search = ref('')
const activeType = ref('全部')

const types = computed(() => {
  const set = new Set(props.articles.map(a => a.type))
  return ['全部', ...set]
})

const filtered = computed(() => {
  let list = props.articles
  if (activeType.value !== '全部') {
    list = list.filter(a => a.type === activeType.value)
  }
  if (search.value.trim()) {
    const q = search.value.toLowerCase()
    list = list.filter(a =>
      a.title.toLowerCase().includes(q) ||
      a.tags.some(t => t.toLowerCase().includes(q)) ||
      a.excerpt.toLowerCase().includes(q)
    )
  }
  return list
})

const typeColors = {
  '技术': 'bg-emerald-100 text-emerald-700',
  '行业': 'bg-blue-100 text-blue-700',
  '管理': 'bg-purple-100 text-purple-700',
  '感悟': 'bg-amber-100 text-amber-700',
  '产品': 'bg-rose-100 text-rose-700',
}
</script>

<template>
  <div class="p-6">
    <!-- 标题栏 -->
    <div class="mb-6">
      <h1 class="text-2xl font-bold text-slate-800">文章知识库</h1>
      <p class="text-slate-500 text-sm mt-1">{{ articles.length }} 篇文章，AI 提炼的结构化摘要</p>
    </div>

    <!-- 搜索 -->
    <div class="relative mb-4">
      <input
        v-model="search"
        type="text"
        placeholder="搜索文章、标签、实体..."
        class="w-full pl-10 pr-4 py-2.5 rounded-xl border border-slate-200 bg-white text-sm focus:outline-none focus:ring-2 focus:ring-blue-400"
      />
      <span class="absolute left-3 top-2.5 text-slate-400">🔍</span>
    </div>

    <!-- 类型筛选 -->
    <div class="flex gap-2 flex-wrap mb-6">
      <button
        v-for="t in types"
        :key="t"
        @click="activeType = t"
        :class="[
          'px-3 py-1 rounded-full text-xs font-medium transition-colors',
          activeType === t
            ? 'bg-blue-600 text-white'
            : 'bg-white text-slate-600 border border-slate-200 hover:border-blue-300'
        ]"
      >{{ t }}</button>
    </div>

    <!-- 空状态 -->
    <div v-if="articles.length === 0" class="text-center py-20 text-slate-400">
      <div class="text-4xl mb-3">📭</div>
      <p class="text-sm">知识库尚未生成</p>
      <p class="text-xs mt-1">请先运行 <code class="bg-slate-100 px-1 rounded">python code/ingest.py</code></p>
    </div>

    <!-- 文章网格 -->
    <div v-else class="grid grid-cols-1 md:grid-cols-2 xl:grid-cols-3 gap-4">
      <div
        v-for="article in filtered"
        :key="article.slug"
        @click="emit('open', article.slug)"
        class="bg-white rounded-xl p-4 border border-slate-100 hover:border-blue-300 hover:shadow-md cursor-pointer transition-all"
      >
        <!-- 类型标签 -->
        <span
          :class="['text-xs px-2 py-0.5 rounded-full font-medium', typeColors[article.type] || 'bg-slate-100 text-slate-600']"
        >{{ article.type }}</span>

        <!-- 标题 -->
        <h3 class="mt-2 font-semibold text-slate-800 text-sm leading-snug line-clamp-2">
          {{ article.title }}
        </h3>

        <!-- 摘要 -->
        <p class="mt-2 text-xs text-slate-500 line-clamp-3 leading-relaxed">
          {{ article.excerpt }}
        </p>

        <!-- 标签 -->
        <div class="mt-3 flex flex-wrap gap-1">
          <span
            v-for="tag in article.tags.slice(0, 3)"
            :key="tag"
            class="text-xs bg-slate-50 text-slate-500 px-2 py-0.5 rounded border border-slate-100"
          ># {{ tag }}</span>
        </div>
      </div>
    </div>
  </div>
</template>
