<script>
  // import ApiTest from "./lib/ApiTest.svelte";
  import Header from "./lib/components/Header.svelte";
  import Footer from "./lib/components/Footer.svelte";
</script>
<Header />
<main>
  <h1>HBnB - Test</h1>
  <!-- If you want to test the endpoints and the connection with
   the backend, uncomment the component ApiTest-->
  <!-- <ApiTest /> -->
</main>
<Footer />

<style>
  h1 {
    margin: 0;
    padding: 10px;
  }
</style>
