import { createApp } from "vue";
import PrimeVue from "primevue/config";
import App from "./App.vue";
import router from "./router";
import store from "./store"; // Import the store
import "./assets/tailwind.css"; // Import Tailwind CSS
import "leaflet/dist/leaflet.css"; // Import Leaflet CSS

const app = createApp(App);

app.use(PrimeVue, { unstyled: true });
app.use(router);
app.use(store); // Use the store

app.mount("#app");
