// src/router/index.js
import { createRouter, createWebHistory } from "vue-router";
import Home from "@/views/Home.vue";
import NotFound from "@/views/NotFound.vue";
import Admin from "@/views/modules/Admin.vue";

const routes = [
  { path: "/", name: "Home", component: Home },
  { path: "/admin", name: "Admin", component: Admin },
  { path: "/:catchAll", name: "NotFound", component: NotFound },
];

const router = createRouter({
  base: '/hermes',  // Base URL of your app
  history: createWebHistory(),
  routes,
});

export default router;
