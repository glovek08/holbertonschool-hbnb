<script>
  import PlaceCard from "../components/PlaceCard.svelte";
  import { isAuthenticated } from "../lib/stores/auth";
  import { showSidebar } from "../lib/stores/sidebar";
  import Button_2  from "../components/Button-2.svelte";
  import Sidebar from "../components/Sidebar.svelte";
</script>

{#if $isAuthenticated}
  <p>HELLO USER!</p>
{:else}
  <section id="places-user-not-logged-section">
    <h2>You must log in to see this page!</h2>
    <button class="places-login-btn function-button" on:click={() => showSidebar.set(true)}>Log In</button>
    Don't have an account?
    <a href="/signup" id="create-account-link" style="display: block;"
      >Create account <i class="fa-solid fa-hand-point-left"></i>
    </a>
  </section>
{/if}

<style>
  section {
    display: flex;
    align-items: center;
    justify-content: center;
    flex-direction: column;
  }
  .places-login-btn {
    background-color: var(--green);
    margin-top: 10px;
    margin-bottom: 30px;
  }
</style>
