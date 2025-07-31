import { defineConfig } from "vite";
import { svelte } from "@sveltejs/vite-plugin-svelte";

// https://vite.dev/config/
export default defineConfig({
  plugins: [svelte()],
  server: {
    host: "0.0.0.0", // Allow external access
    port: 5173,
    proxy: {
      "/api": "http://localhost:5000",
    },
  },
});
