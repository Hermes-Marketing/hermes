import { defineConfig } from 'vite';
import vue from '@vitejs/plugin-vue';
import path from 'path';

export default defineConfig(({ mode }) => {
  const isProduction = mode === 'production';

  return {
    plugins: [vue()],
    server: {
      host: isProduction ? '0.0.0.0' : 'localhost', // Use 'localhost' for local dev, and '0.0.0.0' for production if needed
      port: process.env.HERMES_FE_PORT || (isProduction ? 443 : 8080), // Use 443 in prod and 8080 locally
      watch: {
        usePolling: false,
      },
      hmr: {
        protocol: isProduction ? 'wss' : 'ws', // Use 'ws' locally and 'wss' in production
        host: isProduction ? 'hermes.xavrema.com' : 'localhost',
        port: isProduction ? 443 : (process.env.HERMES_FE_PORT || 8080), // Match the port with your server setup
      }
    },
    resolve: {
      alias: {
        "@": path.resolve(__dirname, "src"),
      },
    },
  };
});
