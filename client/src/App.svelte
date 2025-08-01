<script>
  import { onMount } from "svelte";
  import { checkAuth, isAuthenticated } from "./lib/stores/auth";
  import { Router, createRouter } from '@roxi/routify'
  import routes from '../.routify/routes.default.js'
  import Header from "./components/Header.svelte";
  import Footer from "./components/Footer.svelte";

  export const router = createRouter({ routes })

  onMount(async () => {
    await checkAuth();
    console.log(`user auth: ${$isAuthenticated}`);
  });
</script>

<Header />
<main>
  <Router {router}/>
</main>
<Footer />

<style>
  main {
    flex: 1;
    width: 100%;
    padding: 8% 0 0 0;
    display: flex;
    align-items: center;
    justify-content: space-between;
    flex-direction: column;
    min-height: 1000px;
  }
</style>