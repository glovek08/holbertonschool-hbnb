<script>
  import { isAuthenticated } from "../lib/stores/auth";
  import { showSidebar } from "../lib/stores/sidebar";
  import { get } from "svelte/store";
</script>

{#if $isAuthenticated}
  <slot />
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