import { createRouter, createWebHistory } from "vue-router";
import Home from "../components/Home.vue";
import City from "../components/City.vue";
import Places from "../components/Places.vue"; // Import the Places component
// import PlanRoute from "../components/PlanRoute.vue"; // Import the Plan component

const routes = [
    { path: "/", component: Home },
    { path: "/city/:name", component: City, props: true },
    { path: "/places", component: Places }, // Add the new route
    // { path: "/plan", component: PlanRoute }, // Add the new route
];

const router = createRouter({
    history: createWebHistory(),
    routes,
});

export default router;
