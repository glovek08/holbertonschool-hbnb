import { defineConfig } from "vite";
import { svelte } from "@sveltejs/vite-plugin-svelte";
import routify from '@roxi/routify/vite-plugin' // Correct import path for Routify 3

export default defineConfig({
  plugins: [svelte(), routify()],
  server: {
    host: "0.0.0.0", // Allow external access
    port: 5173,
    proxy: {
      "/api": "http://localhost:5000",
    },
  },
});