<script>
  import { onMount } from "svelte";
  import { checkAuth, isAuthenticated } from "./lib/stores/auth";
  import { Router, createRouter } from "@roxi/routify";
  import routes from "../.routify/routes.default.js";
  import Header from "./components/Header.svelte";
  import Footer from "./components/Footer.svelte";

  export const router = createRouter({ routes });

  onMount(async () => {
    if ((await checkAuth()).msg) {
      console.log(`User authenticated`);
    } else {
      console.warn(`User not authenticated`);
    }
  });
</script>

<Header />
<main>
  <Router {router} />
</main>
<Footer />

<style>
  main {
    flex: 1;
    width: 100%;
    padding: 2% 0 0 0;
    display: flex;
    align-items: center;
    justify-content: flex-start;
    flex-direction: column;
    min-height: 1000px;
  }
</style>
