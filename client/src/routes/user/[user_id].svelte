<script>
  import { onMount } from "svelte";
  import api from "../../lib/api";
  import { userName } from "../../lib/stores/auth";
  import { params } from "@roxi/routify";
  import AuthBox from "../../components/AuthBox.svelte";
  import UserReserves from "../../components/UserReserves.svelte";
  import UserReviews from "../../components/UserReviews.svelte";
  import UserPlaces from "../../components/UserPlaces.svelte";

  let currentUser;
  let loading = false;
  let selectedItem = "reserves";
  let tokenExpired = false;
  let errorMsg = "";
  let userReviews = ["empty"];

  async function fetchUserReviews(userId) {
    // TODO: Store review list in cache, only fetch if: review_list not in cache OR review_author not current user id.
    // Although if we need to check if the local storage has already a review list by another author, it's broken.
    // remember to clear local storage. Or find better way to do it.
    if (!userReviews.includes("empty")) {
      console.log("userReviews already fetched, Aborting...");
      return;
    }
    loading = true;
    tokenExpired = false;
    errorMsg = "";
    try {
      userReviews = await api.getUserReviews(userId);
      console.log(
        "User reviews fetched!: " + JSON.stringify(userReviews, null, 2)
      );
    } catch (error) {
      if (error.message && error.message.includes("Token has expired")) {
        tokenExpired = true;
        errorMsg = "Your session has expired. Please log in again.";
        userReviews = [];
      } else {
        errorMsg = error.message || "An error occurred while fetching reviews.";
      }
      console.warn(error);
    }
    loading = false;
  }

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
      <h1 id="user-dashboard-title">Welcome {$userName}</h1>
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
            <li
              class="user-ul-li {selectedItem === 'reserves' ? 'selected' : ''}"
            >
              <button
                type="button"
                class="user-button"
                aria-label="My Reserves"
                title="My Reserves"
                on:click={() => (selectedItem = "reserves")}>My Reserves</button
              >
            </li>
            <li
              class="user-ul-li {selectedItem === 'reviews' ? 'selected' : ''}"
            >
              <button
                type="button"
                class="user-button"
                aria-label="My Reviews"
                title="My Reviews"
                on:click={() => {
                  selectedItem = "reviews";
                  fetchUserReviews($params.user_id);
                }}>My Reviews</button
              >
            </li>
            <li
              class="user-ul-li {selectedItem === 'places' ? 'selected' : ''}"
            >
              <button
                type="button"
                class="user-button"
                aria-label="My Places"
                title="My Places"
                on:click={() => (selectedItem = "places")}>My Places</button
              >
            </li>
          </ul>
        </aside>
        <div id="user-menu-deployer" class="user-menu-item">
          {#if selectedItem === "reserves"}
            {#if tokenExpired}
              <div class="warning">
                {errorMsg}
              </div>
            {:else if errorMsg}
              <div class="warning">{errorMsg}</div>
            {/if}
            <h2 class="deployer-title">My Reviews</h2>
            <UserReserves />
          {/if}
          {#if selectedItem === "reviews"}
            <UserReviews userReviews={userReviews} />
          {/if}
          {#if selectedItem === "places"}
            <UserPlaces />
          {/if}
        </div>
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
    max-width: 2000px;
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
  #user-menu-deployer {
    display: flex;
    align-items: center;
    justify-content: center;
    flex-direction: column;
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
  }
  .user-ul-li.selected {
    background: var(--selected);
  }
  .user-button {
    background: none;
    color: var(--font-primary);
    font-size: 1.3rem;
    border: none;
    cursor: pointer;
    width: 100%;
    padding: 20px;
    transition:
      300ms color ease-in-out,
      300ms background ease-in-out;
  }
  .user-button:hover {
    color: var(--font-secondary);
    background: var(--accent);
  }
  #user-profile-picture {
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
  @media (max-width: 800px) {
    #user-profile-picture {
      display: none;
    }
    #user-menu {
      flex-direction: column;
      align-items: stretch;
      gap: 0;
      border: none;
    }
    #user-anchors-container {
      width: 100%;
      min-height: unset;
      flex-direction: row;
      align-items: flex-start;
      justify-content: flex-start;
      border-right: none;
      border-bottom: 2px solid var(--gray);
      padding: 0 0 10px 0;
      overflow-x: auto;
      overflow-y: hidden;
    }
    #user-menu-deployer {
      min-height: 50dvh;
    }
    .user-ul {
      display: flex;
      flex-direction: row;
      width: 100%;
      margin: 0;
      padding: 0;
      overflow-x: auto;
      overflow-y: hidden;
      gap: 0;
    }

    .user-ul-li {
      min-width: 140px;
      flex: 0 0 auto;
    }

    .user-button {
      padding: 10px;
      font-size: 1rem;
    }
    .user-menu-item {
      min-height: unset;
      width: 100%;
    }
  }
</style>
