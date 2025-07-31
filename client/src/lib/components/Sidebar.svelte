<script>
  import Button_1 from "./Button-1.svelte";
  export let show = false;
  export let userLoggedIn = false;
  export let closeSidebar = () => {};
  export let logout = () => {};
  let isClosing = false;

  function handleClose() {
    isClosing = true;
    setTimeout(() => {
      closeSidebar();
      isClosing = false;
    }, 300);
  }
  export { handleClose as requestClose };
</script>

{#if show}
  <button
    type="button"
    class="sidebar-backdrop"
    class:closing={isClosing}
    on:click={handleClose}
    on:keydown={(e) => {
      if (e.key === "Enter" || e.key === " ") handleClose();
    }}
    aria-label={show ? "Close sidebar" : "Open sidebar"}
    tabindex="0"
    style="border:none;background:rgba(0,0,0,0);padding:0;position:fixed;inset:0;z-index:9;"
  ></button>
  <aside class="sidebar" class:closing={isClosing}>
    {#if !userLoggedIn}
      <div class="login-section">
        <h3 id="sidebar-heading">Welcome!</h3>
        <p>Please log in to access your account</p>
        <!-- login form should be here! -->
        <form id="user-login-form" action="" method="post">
          <input
            type="text"
            class="login-input"
            name="username"
            id="username"
            placeholder="username"
            required
            aria-label="username"
          />
          <input
            type="password"
            class="login-input"
            name="password"
            id="password"
            placeholder="password"
            required
            aria-label="password"
          />
          <Button_1 text="LOGIN" type="submit" />
        </form>
      </div>
    {:else}
      <div class="user-section">
        <h3>Your Account</h3>
        <ul class="user-menu">
          <li><a href="/profile">Profile</a></li>
          <li><a href="/bookings">My Bookings</a></li>
          <li><button on:click={logout}>Logout</button></li>
        </ul>
      </div>
    {/if}
  </aside>
{/if}

<style>

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
  .login-section {
    /* outline: 1px solid yellow; */
    padding: 20px;
    text-align: center;
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
  }

  /* Custom styling for login button in sidebar */
  #user-login-form :global(button) {
    width: 100%;
    padding: 10px 10px !important;
    filter: hue-rotate(180deg);
    -webkit-filter: hue-rotate(180deg);
  }

  aside.sidebar {
    /* outline: 1px solid red; */
    position: fixed;
    height: 100%;
    right: 0;
    top: 0;
    background: var(--header-background);
    padding: 100px 30px 30px 30px;
    display: flex;
    align-items: center;
    justify-content: center;
    flex-direction: column;
    z-index: 10;
    box-shadow: 0 0 50px rgba(0, 0, 0, 0.329);
    width: 20%;
    min-width: 240px;
    animation: slideInFromRight 400ms cubic-bezier(0.25, 0.46, 0.45, 0.94);
    transform: translateX(0);
    transition: background-color 300ms ease-in-out;
    overflow-y: auto;
  }
  #sidebar-heading {
    font-size: 1.5rem;
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
      padding: 20px;
    }
  }
</style>
