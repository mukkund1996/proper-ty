import { createRouter, createWebHistory } from 'vue-router';
import LoginViewVue from '@/views/LoginView.vue';
import { DASHBOARD_ROUTE } from './routes.constant';

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'login',
      component: LoginViewVue,
    },
    {
      path: DASHBOARD_ROUTE,
      name: 'dashboard',
      component: () => import('../views/DashboardView.vue'),
    },
  ],
});

export default router;
