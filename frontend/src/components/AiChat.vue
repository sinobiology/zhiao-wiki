<script setup>
import { ref } from 'vue'

const emit = defineEmits(['open'])

const input = ref('')
const loading = ref(false)
const history = ref([])  // { role: 'user'|'assistant', content, sources? }

async function send() {
  const msg = input.value.trim()
  if (!msg || loading.value) return

  history.value.push({ role: 'user', content: msg })
  input.value = ''
  loading.value = true

  try {
    const res = await fetch('/api/chat', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        message: msg,
        history: history.value
          .slice(-6)
          .map(h => ({ role: h.role, content: h.content })),
      }),
    })
    const data = await res.json()
    history.value.push({
      role: 'assistant',
      content: data.reply || data.error,
      sources: data.sources || [],
    })
  } catch (e) {
    history.value.push({ role: 'assistant', content: '连接后端失败，请确认后端服务已启动。' })
  } finally {
    loading.value = false
  }
}

function onKeydown(e) {
  if (e.key === 'Enter' && !e.shiftKey) {
    e.preventDefault()
    send()
  }
}
</script>

<template>
  <div class="flex flex-col h-full">
    <!-- 顶部 -->
    <div class="px-6 py-4 border-b border-slate-200 bg-white">
      <h1 class="text-xl font-bold text-slate-800">AI 知奥</h1>
      <p class="text-sm text-slate-500 mt-0.5">基于知识库的数字分身 · 20 年发酵行业 R&D 总监视角</p>
    </div>

    <!-- 对话区 -->
    <div class="flex-1 overflow-y-auto px-6 py-4 space-y-4">
      <!-- 欢迎语 -->
      <div v-if="history.length === 0" class="text-center py-16 text-slate-400">
        <div class="text-5xl mb-4">🧬</div>
        <p class="font-medium text-slate-600">你好，我是 AI 知奥</p>
        <p class="text-sm mt-2">可以问我关于氨基酸行业、发酵工程、管理逻辑的任何问题</p>
        <div class="mt-6 flex flex-wrap gap-2 justify-center">
          <button
            v-for="q in ['赖氨酸行业格局如何？', '发酵成本如何系统性降低？', '凯赛生物的核心竞争力是什么？']"
            :key="q"
            @click="input = q; send()"
            class="text-xs bg-blue-50 text-blue-600 border border-blue-200 px-3 py-1.5 rounded-full hover:bg-blue-100 transition-colors"
          >{{ q }}</button>
        </div>
      </div>

      <!-- 消息列表 -->
      <div
        v-for="(msg, i) in history"
        :key="i"
        :class="['flex', msg.role === 'user' ? 'justify-end' : 'justify-start']"
      >
        <div :class="[
          'max-w-[75%] rounded-2xl px-4 py-3 text-sm leading-relaxed',
          msg.role === 'user'
            ? 'bg-blue-600 text-white rounded-br-sm'
            : 'bg-white border border-slate-100 text-slate-700 rounded-bl-sm shadow-sm'
        ]">
          <div class="whitespace-pre-wrap">{{ msg.content }}</div>
          <!-- 来源 -->
          <div v-if="msg.sources?.length" class="mt-2 pt-2 border-t border-slate-100">
            <div class="text-xs text-slate-400 mb-1">参考来源：</div>
            <div class="flex flex-wrap gap-1">
              <button
                v-for="s in msg.sources"
                :key="s.slug"
                @click="emit('open', s.slug)"
                class="text-xs text-blue-500 hover:underline"
              >{{ s.title }}</button>
            </div>
          </div>
        </div>
      </div>

      <!-- 加载中 -->
      <div v-if="loading" class="flex justify-start">
        <div class="bg-white border border-slate-100 rounded-2xl rounded-bl-sm px-4 py-3 shadow-sm">
          <div class="flex gap-1 items-center">
            <span class="w-2 h-2 bg-slate-300 rounded-full animate-bounce" style="animation-delay:0ms"></span>
            <span class="w-2 h-2 bg-slate-300 rounded-full animate-bounce" style="animation-delay:150ms"></span>
            <span class="w-2 h-2 bg-slate-300 rounded-full animate-bounce" style="animation-delay:300ms"></span>
          </div>
        </div>
      </div>
    </div>

    <!-- 输入框 -->
    <div class="px-6 py-4 border-t border-slate-200 bg-white">
      <div class="flex gap-3 items-end">
        <textarea
          v-model="input"
          @keydown="onKeydown"
          placeholder="输入问题，Enter 发送，Shift+Enter 换行..."
          rows="2"
          class="flex-1 resize-none rounded-xl border border-slate-200 px-4 py-2.5 text-sm focus:outline-none focus:ring-2 focus:ring-blue-400"
        ></textarea>
        <button
          @click="send"
          :disabled="loading || !input.trim()"
          class="px-4 py-2.5 bg-blue-600 text-white rounded-xl text-sm font-medium hover:bg-blue-700 disabled:opacity-40 disabled:cursor-not-allowed transition-colors"
        >发送</button>
      </div>
    </div>
  </div>
</template>
