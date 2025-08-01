<script>
  import { onMount } from "svelte";
  import { checkAuth, isAuthenticated } from "./lib/stores/auth";
  import Router from "svelte-spa-router";
  // import ApiTest from "./lib/ApiTest.svelte";
  import Header from "./lib/components/Header.svelte";
  import Footer from "./lib/components/Footer.svelte";
  import Home from "./lib/pages/Home.svelte";
  import Signup from './lib/pages/Signup.svelte';

  onMount(async () => {
    await checkAuth();
    console.log(`user auth: ${$isAuthenticated}`)
  });

  const routes={
    '/': Home,
    '/signup': Signup,
  };

  // onMount(() => {
  //   const updateTheme = () => {
  //     const prefersDark = window.matchMedia(
  //       "(prefers-color-scheme: dark)"
  //     ).matches;
  //     const root = document.documentElement;
  //     if (prefersDark) {
  //       root.classList.remove("light");
  //     } else {
  //       root.classList.add("light");
  //     }
  //   };
  //   updateTheme();

  //   const mediaQuery = window.matchMedia("(prefers-color-scheme: dark)");
  //   mediaQuery.addEventListener("change", updateTheme);

  //   return () => {
  //     mediaQuery.removeEventListener("change", updateTheme);
  //   };
  // });
</script>

<Header />
<main>
  <Router {routes}/>
  <!-- If you want to test the endpoints and the connection with
   the backend, uncomment the component ApiTest-->
  <!-- <ApiTest /> -->
</main>
<Footer />

<style>
  main {
    /* outline: 1px solid blue; */
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
