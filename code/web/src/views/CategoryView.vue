<script setup>
import { ref, computed, onMounted, watch } from 'vue'
import { useRoute, useRouter } from 'vue-router'

const route  = useRoute()
const router = useRouter()
const all    = ref([])
const searchQ = ref('')

const TYPE_LABELS = { '技术': '技术与发酵', '行业': '行业分析', '管理': '管理逻辑', '感悟': '个人感悟', '产品': '产品专题' }
const TYPE_COLORS = { '技术': '#3B7DD8', '行业': '#47956A', '管理': '#7E5FAD', '感悟': '#C5961B', '产品': '#C2604A' }

const currentType = computed(() => route.params.type)
const label = computed(() => TYPE_LABELS[currentType.value] || currentType.value)
const color = computed(() => TYPE_COLORS[currentType.value] || '#999')

const filtered = computed(() => {
  let list = all.value.filter(a => a.type === currentType.value)
  if (searchQ.value.trim()) {
    const q = searchQ.value.toLowerCase()
    list = list.filter(a => a.title.toLowerCase().includes(q) || a.excerpt.toLowerCase().includes(q))
  }
  return list.sort((a, b) => b.created.localeCompare(a.created))
})

async function loadIndex() {
  all.value = await fetch('/data/wiki-index.json').then(r => r.json())
}

watch(() => route.params.type, loadIndex, { immediate: true })
</script>

<template>
  <div>
    <div class="page-hero" style="padding:24px 36px">
      <div style="font-size:12px;color:rgba(255,255,255,0.5);margin-bottom:6px">分类</div>
      <h1 style="font-size:24px">{{ label }}</h1>
      <div style="font-size:13px;color:rgba(255,255,255,0.5);margin-top:4px">{{ filtered.length }} 篇文章</div>
    </div>

    <div style="padding:24px 36px">
      <!-- 搜索 -->
      <div class="search-wrap" style="padding:0 0 16px">
        <div class="search-box">
          <span>🔍</span>
          <input v-model="searchQ" placeholder="在此分类中搜索..." />
        </div>
      </div>

      <!-- 列表 -->
      <div class="card">
        <div v-if="filtered.length === 0" style="padding:40px;text-align:center;color:var(--text-tertiary)">
          暂无文章
        </div>
        <div v-for="item in filtered" :key="item.slug"
          class="page-list-item"
          @click="router.push('/page/' + item.slug)">
          <div>
            <div style="font-size:14px;font-weight:500;color:var(--text-primary)">{{ item.title }}</div>
            <div style="font-size:12px;color:var(--text-tertiary);margin-top:3px;max-width:600px;overflow:hidden;text-overflow:ellipsis;white-space:nowrap">
              {{ item.excerpt }}
            </div>
          </div>
          <div style="text-align:right;flex-shrink:0;margin-left:16px">
            <div style="font-size:12px;color:var(--text-tertiary)">{{ item.created }}</div>
            <div style="display:flex;gap:4px;margin-top:4px;justify-content:flex-end">
              <span v-for="tag in item.tags.slice(0,2)" :key="tag"
                style="font-size:11px;background:var(--bg-secondary);padding:1px 6px;border-radius:8px;color:var(--text-secondary)">
                {{ tag }}
              </span>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
