<script>
  import { onDestroy, onMount } from "svelte";
  import {
    userName,
    isAuthenticated,
    currentUserId,
    login,
    logout,
  } from "../lib/stores/auth";
  import Checkbox from "./Checkbox.svelte";
  import { showSidebar } from "../lib/stores/sidebar"; 

  // The sidebar is being mounter in the header.
  // ********************** SIDEBAR *********************************
  let isClosing = false;

  const handleClose = () => {
    isClosing = true;
    setTimeout(() => {
      showSidebar.set(false);
      isClosing = false;
    }, 290);
  };
  export { handleClose as requestClose };
  // *********************** LOGIN FUNCTION **************************
  let stayLoggedIn = false;
  let errorMessage = "";
  let email = "";
  let password = "";

  async function handleLogin(event) {
    event.preventDefault();
    let logged = await login(email, password, stayLoggedIn);
    if (!logged.success) {
      errorMessage = logged.error;
    } else {
      console.log("Logging in: "+logged.msg);
    }
  }
  /* ************************* LOG OUT *****************************/
  async function handleLogout(event) {
    event.preventDefault();
    const logout_msg = await logout();
    if (logout_msg.success) {
      console.log(logout_msg.msg);
    } else {
      console.warn(logout_msg.error);
    }
  }
</script>

{#if $showSidebar}
  <button
    type="button"
    class="sidebar-backdrop"
    class:closing={isClosing}
    on:click={handleClose}
    on:keydown={(e) => {
      if (e.key === "Enter" || e.key === " ") handleClose();
    }}
    aria-label={$showSidebar ? "Close sidebar" : "Open sidebar"}
    tabindex="0"
    style="border:none;background:rgba(0,0,0,0);padding:0;position:fixed;inset:0;z-index:9;"
  ></button>
  <aside class="sidebar" class:closing={isClosing}>
    {#if !$isAuthenticated}
      <div class="login-div">
        <h3 id="login-div-heading">Welcome!</h3>
        <p>Please log in to access your account</p>
        <form id="user-login-form" on:submit={handleLogin}>
          <input
            type="email"
            class="login-input"
            name="login-email"
            id="login-email"
            placeholder="email"
            aria-label="email"
            maxlength="254"
            required
            bind:value={email}
          />
          <input
            type="password"
            class="login-input"
            name="login-password"
            id="login-password"
            placeholder="password"
            aria-label="password"
            maxlength="60"
            required
            bind:value={password}
          />
          <div id="stay-logged-checkbox-div">
            <Checkbox bind:checked={stayLoggedIn} id="stay-logged-checkbox" />
            <label for="stay-logged-checkbox">Stay Logged</label>
          </div>
          <div id="error-log-div">{errorMessage}</div>
          <button type="submit" id="login-button" class="function-button"
            >LOG IN</button
          >
        </form>
        <p>
          Don't have an account?
          <a href="/signup" id="create-account-link" style="display: block;"
            >Create account <i class="fa-solid fa-hand-point-left"></i></a
          >
        </p>
      </div>
    {:else}
      <!-- If the user logs in, hide the login form and display this. -->
      <div class="user-section">
        <h3 id="sidebar-title">Hello {$userName}</h3>
        <!-- maybe use a rune to display Hello {user.name}! -->
        <ul class="user-menu">
          <li><a href="/user/{$currentUserId}">My Account</a></li>
          <li><a href="/asdaks">Another option</a></li>
          <li><a href="/support">Support</a></li>
          <li>
            <button class="logout-btn function-button" on:click={handleLogout}
              >Logout</button
            >
          </li>
        </ul>
      </div>
    {/if}
  </aside>
{/if}

<style>
  aside.sidebar {
    /* outline: 1px solid red; */
    position: fixed;
    height: 100%;
    right: 0;
    top: 0;
    background: var(--header-background);
    padding: 30px 30px 30px 30px;
    display: flex;
    align-items: center;
    justify-content: center;
    flex-direction: column;
    z-index: 10;
    box-shadow: 0 0 50px rgba(0, 0, 0, 0.329);
    width: 20%;
    min-width: 300px;
    animation: slideInFromRight 400ms cubic-bezier(0.25, 0.46, 0.45, 0.94);
    transform: translateX(0);
    transition: background-color 300ms ease-in-out;
    overflow-y: auto;
  }
  .sidebar-backdrop {
    position: fixed;
    inset: 0;
    z-index: 9;
    background: rgba(0, 0, 0, 0);
    backdrop-filter: blur(2px);
    animation: backdropFadeIn 300ms ease-out;
  }

  .sidebar-backdrop.closing {
    animation: backdropFadeOut 300ms ease-out;
  }
  .login-div {
    /* outline: 1px solid yellow; */
    padding: 20px;
    text-align: center;
    width: 100%;
    margin-top: 100px;
  }

  #user-login-form {
    /* outline: 1px solid red; */
    display: flex;
    align-items: center;
    justify-content: center;
    flex-direction: column;
    gap: 20px;
    padding: 20px 10px;
  }
  .login-input {
    padding: 7px 15px;
    width: 200px;
  }
  #stay-logged-checkbox-div {
    display: flex;
    align-items: center;
    gap: 0.5em;
  }
  label[for="stay-logged-checkbox"] {
    display: inline;
    font-size: 1rem;
    color: var(--primary-font);
    cursor: pointer;
    margin-right: 0.5em;
    user-select: none;
    transition: color 0.2s ease;
  }
  #login-button {
    background-color: var(--green);
  }
  #error-log-div {
    color: var(--red);
    font-weight: bolder;
  }

  #login-div-heading {
    font-size: 1.5rem;
  }
  .user-section {
    /* outline: 1px solid red; */
    width: 100%;
    display: flex;
    align-items: center;
    justify-content: center;
    flex-direction: column;
  }
  .user-menu {
    /* outline: 1px solid yellow; */
    padding: 5px;
  }
  .user-menu li {
    /* outline: 1px solid blue; */
    padding: 10px;
  }
  #sidebar-title {
    align-self:flex-start;
    margin-left: 20px;
  }
  .logout-btn {
    width: 100%;
    background-color: var(--red);
    padding: 10px 30px;
  }
  .logout-btn:hover {
    filter: brightness(0.9);
  }
  .logout-btn:active {
    filter: brightness(0.5);
  }
  aside.sidebar.closing {
    animation: slideOutToRight 300ms cubic-bezier(0.55, 0.06, 0.68, 0.19);
  }
  @keyframes slideInFromRight {
    from {
      transform: translateX(100%);
      opacity: 0;
    }
    to {
      transform: translateX(0);
      opacity: 1;
    }
  }
  @keyframes slideOutToRight {
    from {
      transform: translateX(0);
      opacity: 1;
    }
    to {
      transform: translateX(100%);
      opacity: 0;
    }
  }
  @keyframes backdropFadeIn {
    from {
      opacity: 0;
    }
    to {
      opacity: 1;
    }
  }
  @keyframes backdropFadeOut {
    from {
      opacity: 1;
    }
    to {
      opacity: 0;
    }
  }
  @media (max-width: 768px) {
    aside.sidebar {
      width: 100vw;
    }
  }
  @media (max-width: 550px) {
    aside.sidebar {
      padding-top: 200px;
    }
  }
</style>
