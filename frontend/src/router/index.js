import { createRouter, createWebHistory } from 'vue-router'
import SingIn from '@/components/SingIn.vue';

const routes = [
  {
    path: '/',
    component: SingIn
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
