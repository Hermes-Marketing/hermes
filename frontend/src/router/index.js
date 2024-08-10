// src/router/index.js
import { createRouter, createWebHistory } from "vue-router";
import Home from "@/views/Home.vue";
import NotFound from "@/views/NotFound.vue";
import Admin from "@/views/modules/Admin.vue";
import CardView from "@/views/modules/CardView.vue";

const routes = [
  { path: "/", name: "Home", component: Home },
  { path: "/admin", name: "Admin", component: Admin },
  {
    path: "/card/:id",
    name: "CardView",
    component: CardView,
    props: (route) => ({
      id: route.params.id,
      cards: route.params.cards, // Ensure cards is passed in the route params
    }),
  },
  { path: "/:catchAll(.*)", name: "NotFound", component: NotFound },  // Adjusted to correctly match all routes
];

const router = createRouter({
  history: createWebHistory('/hermes'),  // Pass the base path to createWebHistory
  routes,
});

export default router;
