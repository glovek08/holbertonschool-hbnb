<script>
  import { onMount } from "svelte";
  // import ApiTest from "./lib/ApiTest.svelte";
  import Header from "./lib/components/Header.svelte";
  import Footer from "./lib/components/Footer.svelte";

  onMount(() => {
    const updateTheme = () => {
      const prefersDark = window.matchMedia(
        "(prefers-color-scheme: dark)"
      ).matches;
      const root = document.documentElement;
      if (prefersDark) {
        root.classList.remove("light");
      } else {
        root.classList.add("light");
      }
    };
    updateTheme();

    const mediaQuery = window.matchMedia("(prefers-color-scheme: dark)");
    mediaQuery.addEventListener("change", updateTheme);

    return () => {
      mediaQuery.removeEventListener("change", updateTheme);
    };
  });
</script>

<Header />
<main>
  <!-- If you want to test the endpoints and the connection with
   the backend, uncomment the component ApiTest-->
  <!-- <ApiTest /> -->
</main>
<Footer />

<style>
  main {
    min-height: 900px;
    width: 100%;
    max-width: 100dvw;
    margin-top: 10px;
    padding: 2rem 3rem;
    display: flex;
    align-items: center;
    justify-content: space-between;
    flex-direction: column;
    outline: 1px solid blue;
  }
</style>
