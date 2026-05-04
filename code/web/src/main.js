import { createApp } from 'vue'
import { createRouter, createWebHistory } from 'vue-router'
import App from './App.vue'
import './style.css'

import Home         from './views/Home.vue'
import PageView     from './views/PageView.vue'
import CategoryView from './views/CategoryView.vue'
import GraphView    from './views/GraphView.vue'
import ChatView     from './views/ChatView.vue'

const router = createRouter({
  history: createWebHistory(),
  routes: [
    { path: '/',                        component: Home },
    { path: '/page/:slug',              component: PageView },
    { path: '/category/:type',          component: CategoryView },
    { path: '/graph',                   component: GraphView },
    { path: '/chat',                    component: ChatView },
  ]
})

createApp(App).use(router).mount('#app')
