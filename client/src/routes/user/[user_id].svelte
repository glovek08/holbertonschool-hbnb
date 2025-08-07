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
    <div id="user-dashboard">
      <h1 id="user-dashboard-title">Welcome {currentUser.first_name}</h1>
      <hr />
      <div id="user-menu">
        <aside id="user-anchors-container">
          <img
            src="/no_pfp.png"
            alt="You"
            title="You"
            id="user-profile-picture"
            width="150"
            height="150"
          />
          <ul class="user-ul">
            <li class="user-ul-li">
              <a
                href="/users/reserves"
                class="user-anchor"
                aria-label="My Reserves"
                title="My Reserves">My Reserves</a
              >
            </li>
            <li class="user-ul-li">
              <a
                href="/users/reviews"
                class="user-anchor"
                aria-label="My Reviews"
                title="My Reviews">My Reviews</a
              >
            </li>
            <li class="user-ul-li">
              <a
                href="/users/places"
                class="user-anchor"
                aria-label="My Places"
                title="My Places">My Places</a
              >
            </li>
          </ul>
        </aside>
        <div class="user-menu-item"></div>
      </div>
    </div>
  {:else if loading}
    <h1>Loading user...</h1>
  {:else}
    <h1>User not found.</h1>
  {/if}
</AuthBox>

<style>
  #user-dashboard {
    /* outline: 1px solid red; */
    background: var(--background-primary);
    width: 90%;
    min-height: 800px;
    display: flex;
    align-items: center;
    justify-content: flex-start;
    flex-direction: column;
    box-shadow: 10px 10px 50px var(--shadow-primary);
  }
  #user-menu {
    /* outline: 1px solid red; */
    width: 90%;
    height: 100%;
    padding: 20px;
    margin-top: 10px;
    display: flex;
    align-items: center;
    justify-content: flex-start;
    flex-direction: row;
    gap: 20px;
  }
  #user-dashboard-title {
    font-size: 2rem;
    padding: 10px;
    margin: 40px 30px 20px 50px;
    align-self: flex-start;
  }
  #user-dashboard hr {
    border-color: var(--gray);
    border: 1px solid var(--gray);
    margin: 0 auto;
    width: 90%;
  }
  #user-anchors-container {
    /* outline: 1px solid blue; */
    align-self: flex-start;
    min-height: 500px;
    width: 30%;
    display: flex;
    align-items: center;
    justify-content: flex-start;
    flex-direction: column;
    border-right: 2px solid var(--gray);
  }
  .user-ul {
    /* outline: 1px solid blue; */
    width: 100%;
    text-align: center;
    margin: 20px 10px;
    padding: 10px;
  }
  .user-ul-li {
    margin: 15px 0;
    font-size: 1.3rem;
  }
  #user-profile-picture {
    width: 80%;
    height: 10%;
    max-width: 300px;
    max-height: 300px;
    aspect-ratio: 1 / 1;
    border: 2px solid var(--background-secondary);
    border-radius: 50%;
    box-shadow: 5px 5px 10px var(--shadow-primary);
  }

  .user-menu-item {
    /* outline: 1px solid green; */
    min-height: 500px;
    width: 100%;
  }
</style>
