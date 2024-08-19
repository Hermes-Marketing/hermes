import { defineConfig } from "vite";
import vue from "@vitejs/plugin-vue";
import path from "path";

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [vue()],
  server: {
    host: true,
    port: process.env.HERMES_FE_PORT, // This is the port which we will use in docker
    watch: {
      usePolling: false,
    },
    hmr:{
      protocol: 'wss',
      host: 'hermes.xavrema.com',
      port: 443, // or the port your server is using for wss
    }
  },
  resolve: {
    alias: {
      "@": path.resolve(__dirname, "src"),
    },
  },
});
