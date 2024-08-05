import { createRouter, createWebHistory } from 'vue-router';
import Home from '@/views/Home.vue';
import NotFound from '@/views/NotFound.vue';
import Admin from '@/views/modules/Admin.vue';

const routes = [
  { path: '/', name: 'Home', component: Home },
  { path: '/admin', name: 'Admin', component: Admin },
  { path: '/:catchAll(.*)', name: 'NotFound', component: NotFound },  // Adjusted to correctly match all routes
];

const router = createRouter({
  history: createWebHistory('/hermes'),  // Pass the base path to createWebHistory
  routes,
});

export default router;
