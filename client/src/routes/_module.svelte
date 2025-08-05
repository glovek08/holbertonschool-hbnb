<script>
  import { onMount } from "svelte";
  import { checkAuth } from "../lib/stores/auth";
  import Header from "../components/Header.svelte";
  import Footer from "../components/Footer.svelte";

  onMount(async () => {
    try {
      await checkAuth();
    } catch (error) {
      // console.warn(error);
    }
  });
</script>

<Header />
<main>
  <slot />
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
