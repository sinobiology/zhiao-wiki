<script setup>
import { ref, watch } from 'vue'
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

// 窄屏抽屉：宽屏下这份状态无效（侧栏由 CSS 常驻显示）
const drawerOpen = ref(false)
function go(path) {
  drawerOpen.value = false
  router.push(path)
}
// 兜底：任何来源的跳转（含正文里的内链）都自动收起抽屉
watch(() => route.path, () => { drawerOpen.value = false })
</script>

<template>
  <div id="app">
    <!-- 窄屏顶栏（宽屏由媒体查询隐藏） -->
    <header class="mobile-topbar">
      <button class="nav-toggle" aria-label="打开导航" @click="drawerOpen = true">
        <span></span><span></span><span></span>
      </button>
      <div class="mobile-title" @click="go('/')">
        知奥ZHAO 知识库
        <span>工业生物技术数字大脑</span>
      </div>
    </header>

    <!-- 抽屉遮罩 -->
    <div class="sidebar-backdrop" :class="{ show: drawerOpen }" @click="drawerOpen = false"></div>

    <!-- 侧边栏：宽屏常驻，窄屏为抽屉 -->
    <aside class="sidebar" :class="{ open: drawerOpen }">
      <button class="sidebar-close" aria-label="收起导航" @click="drawerOpen = false">×</button>

      <div class="sidebar-logo" @click="go('/')">
        知奥ZHAO 知识库
        <span>工业生物技术数字大脑</span>
      </div>

      <a class="nav-item" :class="{ active: route.path === '/' }" @click.prevent="go('/')">
        🏠 知识库首页
      </a>

      <div class="nav-label">分类</div>
      <a
        v-for="t in types" :key="t.key"
        class="nav-item"
        :class="{ active: route.path === '/category/' + t.key }"
        @click.prevent="go('/category/' + t.key)"
      >
        {{ t.icon }} {{ t.label }}
      </a>

      <div class="nav-label">工具</div>
      <a class="nav-item" :class="{ active: route.path === '/graph' }" @click.prevent="go('/graph')">
        🕸️ 知识图谱
      </a>

      <div class="sidebar-footer">
        <a class="ai-btn" @click.prevent="go('/chat')">
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
