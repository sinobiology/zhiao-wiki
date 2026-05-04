<script setup>
import { ref, onMounted } from 'vue'
import Sidebar from './components/Sidebar.vue'
import ArticleList from './components/ArticleList.vue'
import ArticleDetail from './components/ArticleDetail.vue'
import KnowledgeGraph from './components/KnowledgeGraph.vue'
import AiChat from './components/AiChat.vue'

const currentView = ref('articles')  // articles | graph | chat
const selectedSlug = ref(null)
const articles = ref([])
const stats = ref({ total: 0 })

async function fetchArticles() {
  try {
    const res = await fetch('/api/articles')
    const data = await res.json()
    articles.value = data.articles
    stats.value = { total: data.total }
  } catch {
    // 后端未启动时显示空状态
  }
}

function openArticle(slug) {
  selectedSlug.value = slug
  currentView.value = 'detail'
}

function goBack() {
  selectedSlug.value = null
  currentView.value = 'articles'
}

onMounted(fetchArticles)
</script>

<template>
  <div class="flex h-screen overflow-hidden bg-[#F4F7FA]">
    <!-- 侧边栏 -->
    <Sidebar
      :current-view="currentView"
      :stats="stats"
      @navigate="v => { currentView = v; selectedSlug = null }"
    />

    <!-- 主内容区 -->
    <main class="flex-1 overflow-y-auto">
      <ArticleList
        v-if="currentView === 'articles'"
        :articles="articles"
        @open="openArticle"
      />
      <ArticleDetail
        v-else-if="currentView === 'detail'"
        :slug="selectedSlug"
        @back="goBack"
        @open="openArticle"
      />
      <KnowledgeGraph
        v-else-if="currentView === 'graph'"
        @open="openArticle"
      />
      <AiChat
        v-else-if="currentView === 'chat'"
        @open="openArticle"
      />
    </main>
  </div>
</template>
