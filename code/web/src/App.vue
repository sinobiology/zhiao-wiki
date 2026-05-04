<script setup>
import { useRouter, useRoute } from 'vue-router'
const router = useRouter()
const route  = useRoute()

const types = [
  { key: '技术', icon: '🔬', label: '技术与发酵' },
  { key: '行业', icon: '📊', label: '行业分析' },
  { key: '管理', icon: '💼', label: '管理逻辑' },
  { key: '感悟', icon: '💭', label: '个人感悟' },
  { key: '产品', icon: '🧪', label: '产品专题' },
]

const isActive = (path) => route.path === path || route.path.startsWith(path + '/')
</script>

<template>
  <div id="app">
    <!-- 侧边栏 -->
    <aside class="sidebar">
      <div class="sidebar-logo" @click="router.push('/')">
        知奥ZHAO 知识库
        <span>工业生物技术数字大脑</span>
      </div>

      <a class="nav-item" :class="{ active: route.path === '/' }" @click.prevent="router.push('/')">
        🏠 知识库首页
      </a>

      <div class="nav-label">分类</div>
      <a
        v-for="t in types" :key="t.key"
        class="nav-item"
        :class="{ active: route.path === '/category/' + t.key }"
        @click.prevent="router.push('/category/' + t.key)"
      >
        {{ t.icon }} {{ t.label }}
      </a>

      <div class="nav-label">工具</div>
      <a class="nav-item" :class="{ active: route.path === '/graph' }" @click.prevent="router.push('/graph')">
        🕸️ 知识图谱
      </a>

      <div class="sidebar-footer">
        <a class="ai-btn" @click.prevent="router.push('/chat')">
          🤖 AI 知奥
          <span class="new-badge">NEW</span>
        </a>
      </div>
    </aside>

    <!-- 主内容 -->
    <div class="main-content">
      <router-view style="flex:1;min-height:0" />
    </div>
  </div>
</template>
