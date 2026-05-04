<script setup>
import { ref } from 'vue'
import MarkdownIt from 'markdown-it'

const md = new MarkdownIt({ breaks: true, linkify: true })

const verified  = ref(false)
const password  = ref('')
const pwdError  = ref('')
const messages  = ref([])
const input     = ref('')
const loading   = ref(false)

const EXAMPLES = ['赖氨酸行业格局如何？', '发酵成本如何系统性降低？', '规模效应在氨基酸行业怎么体现？']

async function verifyPassword() {
  pwdError.value = ''
  const res = await fetch('/api/verify-password', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ password: password.value }),
  })
  if (res.ok) {
    verified.value = true
  } else {
    pwdError.value = '密码错误，请重试'
  }
}

async function send(msg) {
  const text = (msg || input.value).trim()
  if (!text || loading.value) return
  input.value = ''
  loading.value = true

  messages.value.push({ role: 'user', content: text })
  const idx = messages.value.length
  messages.value.push({ role: 'assistant', content: '', sources: [], thinking: true })

  try {
    const res = await fetch('/api/chat', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        message: text,
        password: password.value,
        history: messages.value.slice(-6, -1).map(m => ({ role: m.role, content: m.content })),
      }),
    })

    const reader = res.body.getReader()
    const decoder = new TextDecoder()
    let buf = ''

    while (true) {
      const { done, value } = await reader.read()
      if (done) break
      buf += decoder.decode(value, { stream: true })
      const lines = buf.split('\n')
      buf = lines.pop()
      for (const line of lines) {
        if (!line.startsWith('data: ')) continue
        const data = JSON.parse(line.slice(6))
        if (data.text) {
          messages.value[idx].thinking = false
          messages.value[idx].content += data.text
          messages.value = [...messages.value]
        }
        if (data.done) {
          messages.value[idx].sources = data.sources || []
          messages.value = [...messages.value]
        }
        if (data.error) {
          messages.value[idx].content = '错误：' + data.error
          messages.value = [...messages.value]
        }
      }
    }
  } catch (e) {
    messages.value[idx].content = '连接失败，请确认后端服务已启动。'
    messages.value = [...messages.value]
  } finally {
    loading.value = false
  }
}

function onKeydown(e) {
  if (e.key === 'Enter' && !e.shiftKey) { e.preventDefault(); send() }
}
</script>

<template>
  <div style="display:flex;flex-direction:column;height:100vh;width:100%">

    <!-- 密码验证 -->
    <div v-if="!verified" style="flex:1;display:flex;align-items:center;justify-content:center;background:var(--bg-primary)">
      <div class="card" style="width:360px;padding:40px;text-align:center">
        <div style="font-size:40px;margin-bottom:16px">🔐</div>
        <div style="font-size:18px;font-weight:700;margin-bottom:6px">访问密码</div>
        <div style="font-size:13px;color:var(--text-secondary);margin-bottom:24px">请输入密码以访问 AI 知奥</div>
        <input
          v-model="password"
          type="password"
          placeholder="请输入密码"
          @keydown.enter="verifyPassword"
          style="width:100%;padding:10px 16px;border:1px solid var(--border);border-radius:var(--radius-md);font-size:15px;letter-spacing:2px;text-align:center;outline:none;margin-bottom:8px"
        />
        <div v-if="pwdError" style="color:#C2604A;font-size:13px;margin-bottom:12px">{{ pwdError }}</div>
        <button @click="verifyPassword"
          style="width:100%;padding:10px;background:var(--accent);color:#fff;border:none;border-radius:var(--radius-md);font-size:14px;font-weight:600;cursor:pointer">
          确认进入
        </button>
      </div>
    </div>

    <!-- 对话界面 -->
    <template v-else>
      <div class="page-hero" style="padding:20px 36px">
        <h1 style="font-size:20px">🤖 AI 知奥</h1>
        <p style="font-size:13px;color:rgba(255,255,255,0.5);margin-top:4px">基于知识库的数字分身 · 20 年发酵行业 R&D 总监视角</p>
      </div>

      <!-- 消息区 -->
      <div style="flex:1;overflow-y:auto;padding:24px 36px;display:flex;flex-direction:column;gap:16px;background:var(--bg-primary)">

        <!-- 空态 -->
        <div v-if="messages.length === 0" style="text-align:center;padding:60px 0">
          <div style="font-size:48px;margin-bottom:12px">🧬</div>
          <div style="font-size:16px;font-weight:600;color:var(--text-primary)">你好，我是 AI 知奥</div>
          <div style="font-size:13px;color:var(--text-secondary);margin-top:6px">可以问我关于氨基酸行业、发酵工程、管理逻辑的任何问题</div>
          <div style="display:flex;flex-wrap:wrap;gap:8px;justify-content:center;margin-top:20px">
            <button v-for="q in EXAMPLES" :key="q" @click="send(q)"
              style="font-size:13px;background:#fff;border:1px solid var(--border);padding:8px 16px;border-radius:var(--radius-pill);cursor:pointer;color:var(--accent);transition:all 0.2s"
              onmouseover="this.style.borderColor='var(--accent)'"
              onmouseout="this.style.borderColor='var(--border)'">
              {{ q }}
            </button>
          </div>
        </div>

        <!-- 消息列表 -->
        <div v-for="(msg, i) in messages" :key="i"
          :style="{ display:'flex', justifyContent: msg.role === 'user' ? 'flex-end' : 'flex-start', gap:'10px', alignItems:'flex-start' }">

          <div v-if="msg.role === 'assistant'" style="width:32px;height:32px;border-radius:50%;background:var(--accent-light);display:flex;align-items:center;justify-content:center;flex-shrink:0;font-size:16px">🎩</div>

          <div style="max-width:75%">
            <div :class="msg.role === 'user' ? 'chat-bubble-user' : 'chat-bubble-ai'"
              style="padding:12px 16px;font-size:14px;line-height:1.7">
              <div v-if="msg.thinking" style="color:var(--text-tertiary);font-style:italic">思考中...</div>
              <div v-else v-html="md.render(msg.content)"></div>
            </div>
            <!-- 来源 -->
            <div v-if="msg.sources?.length" style="margin-top:6px;display:flex;flex-wrap:wrap;gap:6px">
              <span style="font-size:11px;color:var(--text-tertiary)">参考：</span>
              <a v-for="s in msg.sources" :key="s.slug"
                @click.prevent="$router.push('/page/' + s.slug)"
                style="font-size:11px;color:var(--accent);cursor:pointer;text-decoration:underline">
                {{ s.title }}
              </a>
            </div>
          </div>

          <div v-if="msg.role === 'user'" style="width:32px;height:32px;border-radius:50%;background:var(--accent);display:flex;align-items:center;justify-content:center;flex-shrink:0;font-size:16px">👤</div>
        </div>
      </div>

      <!-- 输入区 -->
      <div style="padding:16px 36px;border-top:1px solid var(--border-light);background:var(--bg-tertiary);display:flex;gap:12px;align-items:flex-end">
        <textarea v-model="input" @keydown="onKeydown" rows="2"
          placeholder="输入问题，Enter 发送，Shift+Enter 换行..."
          style="flex:1;resize:none;border:1px solid var(--border);border-radius:22px;padding:10px 18px;font-size:14px;outline:none;font-family:inherit;transition:border-color 0.2s"
          onfocus="this.style.borderColor='var(--accent)'"
          onblur="this.style.borderColor='var(--border)'"
        ></textarea>
        <button @click="send()" :disabled="loading || !input.trim()"
          style="padding:10px 20px;background:var(--accent);color:#fff;border:none;border-radius:22px;font-size:14px;font-weight:600;cursor:pointer;transition:all 0.2s;white-space:nowrap"
          :style="{ opacity: (loading || !input.trim()) ? 0.4 : 1 }">
          发送
        </button>
      </div>
    </template>
  </div>
</template>
