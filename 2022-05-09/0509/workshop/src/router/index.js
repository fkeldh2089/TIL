import Vue from 'vue'
import VueRouter from 'vue-router'
import HomeView from '../views/HomeView.vue'
import LottoView from '../views/LottoView.vue'
import LunchView from '../views/LunchView.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/lunch',
    name: 'Lunch',
    component: LunchView,
  },
  {
    path:'/lotto/:lottoNum',
    name: 'Lotto',
    component: LottoView,
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
