import { createRouter, createWebHistory } from 'vue-router';
import CompanyList from '../components/CompanyList.vue'; // Ensure the correct path to your component
import PlanRoute from '../components/PlanRoute.vue';

const routes = [
  { path: '/', component: CompanyList }, // Route for '/'
  { path: '/plan-route', component: PlanRoute }
];

const router = createRouter({
  history: createWebHistory(),
  routes
});

export default router;
