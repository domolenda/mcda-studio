import { createRouter, createWebHistory } from 'vue-router'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: () => import('@/views/HomeView.vue'),
      meta: { title: 'Home', showInMenu: true },
    },
    {
      path: '/data',
      name: 'data',
      component: () => import('@/views/DataView.vue'),
      meta: { title: 'Data', showInMenu: true },
    },
    {
      path: '/configure',
      name: 'configure',
      component: () => import('@/views/ConfigureView.vue'),
      meta: { title: 'Configure', showInMenu: true },
    },
    {
      path: '/results',
      name: 'results',
      component: () => import('@/views/ResultsView.vue'),
      meta: { title: 'Results', showInMenu: true },
    },
    // {
    //   path: '/how-to-use',
    //   name: 'how-to-use',
    //   component: () => import('@/views/HowToView.vue'),
    //   meta: { title: 'How to Use', showInMenu: true },
    // },
    // {
    //   path: '/about',
    //   name: 'about',
    //   component: () => import('@/views/AboutView.vue'),
    //   meta: { title: 'About', showInMenu: true },
    // },
  ],
})

export default router
