import { defineConfig } from "vite";
import vue from "@vitejs/plugin-vue";
import commonjs from "@rollup/plugin-commonjs"; // Add this line

export default defineConfig({
    base: '/',
    plugins: [vue(), commonjs()], // Include commonjs plugin
});
