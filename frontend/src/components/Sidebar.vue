<script setup>
defineProps({ currentView: String, stats: Object })
const emit = defineEmits(['navigate'])

const navItems = [
  { id: 'articles', icon: '📄', label: '文章库' },
  { id: 'graph',    icon: '🕸️', label: '知识图谱' },
  { id: 'chat',     icon: '🤖', label: 'AI 知奥' },
]
</script>

<template>
  <aside class="w-56 flex-shrink-0 bg-[#0F172A] text-slate-300 flex flex-col h-full">
    <!-- Logo -->
    <div class="px-5 py-6 border-b border-slate-700">
      <div class="text-white font-bold text-lg leading-tight">知奥ZHAO</div>
      <div class="text-slate-400 text-xs mt-1">工业生物技术知识库</div>
    </div>

    <!-- 统计 -->
    <div class="px-5 py-4 border-b border-slate-700">
      <div class="flex items-center gap-2 text-xs text-slate-400">
        <span class="w-2 h-2 rounded-full bg-emerald-400 inline-block"></span>
        {{ stats.total || 0 }} 篇文章已收录
      </div>
    </div>

    <!-- 导航 -->
    <nav class="flex-1 px-3 py-4 space-y-1">
      <button
        v-for="item in navItems"
        :key="item.id"
        @click="emit('navigate', item.id)"
        :class="[
          'w-full flex items-center gap-3 px-3 py-2.5 rounded-lg text-sm transition-colors text-left',
          currentView === item.id
            ? 'bg-blue-600 text-white'
            : 'text-slate-300 hover:bg-slate-700 hover:text-white'
        ]"
      >
        <span>{{ item.icon }}</span>
        <span>{{ item.label }}</span>
      </button>
    </nav>

    <!-- 底部 -->
    <div class="px-5 py-4 border-t border-slate-700 text-xs text-slate-500">
      基于 Karpathy LLM Wiki 模式
    </div>
  </aside>
</template>
