<script>
  import { onMount } from "svelte";
  import api from "../../lib/api";
  import { currentUserId } from "../../lib/stores/auth";
  import { params } from "@roxi/routify";
  import AuthBox from "../../components/AuthBox.svelte";

  let currentUser;
  let loading = false;

  async function getCurrentUser(userId) {
    loading = true;
    // console.log($params.user_id);
    try {
      currentUser = await api.getUser(userId);
    } catch (error) {
      console.warn("Couldn't fetch user: " + currentUser);
    }
    loading = false;
  }
  $: if ($params.user_id) {
    getCurrentUser($params.user_id);
  }
</script>

<AuthBox>
  {#if currentUser}
    <h1>Welcome {currentUser.first_name}</h1>
  {:else if loading}
    <h1>Loading user...</h1>
  {:else}
    <h1>User not found.</h1>
  {/if}
</AuthBox>

<style>
</style>
