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
            <li class="user-ul-li selected">
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
  :root {
    --selected: rgb(72, 73, 75);
  }
  :root.light {
    --selected: rgb(164, 172, 183);
  }
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

    margin-top: 10px 10px 20px 10px;
    display: flex;
    align-items: center;
    justify-content: flex-start;
    flex-direction: row;
    gap: 20px;
    border: 2px solid var(--gray);
    border-radius: 10px;
  }
  #user-dashboard-title {
    font-size: 2rem;
    padding: 10px;
    margin: 40px 30px 20px 50px;
    align-self: flex-start;
  }
  #user-anchors-container {
    /* outline: 1px solid blue; */
    align-self: flex-start;
    min-height: 600px;
    width: 30%;
    padding: 20px;
    display: flex;
    align-items: center;
    justify-content: flex-start;
    flex-direction: column;
    border-right: 2px solid var(--gray);
    overflow-y: auto;
    overflow-x: hidden;
  }
  .user-ul {
    /* outline: 1px solid blue; */
    width: 100%;
    text-align: center;
    margin: 20px 10px;
    padding: 0;
  }
  .user-ul-li {
    margin: 0 0;
    font-size: 1.3rem;
    padding: 20px;
  }
  .user-ul-li.selected {
    background: var(--selected);
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
    min-height: 600px;
    width: 100%;
  }
</style>
