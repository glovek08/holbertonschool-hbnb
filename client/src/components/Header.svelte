<script>
  import { onMount } from "svelte";
  import Sidebar from "./Sidebar.svelte";
  import { isAuthenticated, isAdmin } from "../lib/stores/auth";
  import { showSidebar } from "../lib/stores/sidebar";
  import { writable } from "svelte/store";

  const theme = writable(localStorage.getItem("theme") || "dark");

  let sidebarComponent;
  let headerElement; // Ignore this because we need to bind it, trust me bro.

  function toggleSidebar() {
    if ($showSidebar) {
      sidebarComponent?.requestClose();
    } else {
      showSidebar.set(true);
    }
  }

  function toggleTheme() {
    theme.update((currentTheme) => {
      const newTheme = currentTheme === "light" ? "dark" : "light";
      localStorage.setItem("theme", newTheme);
      document.documentElement.classList.toggle("light", newTheme === "light");
      window.dispatchEvent(new CustomEvent("themechange"));
      return newTheme;
    });
  }

  let isScrolled = false;
  onMount(() => {
    const savedTheme = localStorage.getItem("theme");
    document.documentElement.classList.toggle("light", savedTheme === "light");

    const handleScroll = () => {
      isScrolled = window.scrollY > 100;
    };

    window.addEventListener("scroll", handleScroll);
    return () => {
      window.removeEventListener("scroll", handleScroll);
    };
  });
</script>

<header bind:this={headerElement} class:scrolled={isScrolled}>
  <a id="header-logo-anchor" href="/" title="Back to Home" aria-label="Go Home">
    <img src="/main_logo.png" alt="HBnB Logo" height="40" />
  </a>
  <nav>
    <ul id="header-ul">
      {#if $isAdmin}
        <li class="header-li" title="Open command center">
          <button
            id="admin-command-button"
            class="header-button"
            aria-label="Enter command center"
            on:click={() => (window.location.href = "/command_center")}
          >
            <i id="admin-command-button-span" class="fa-regular fa-chess-queen"></i>
          </button>
        </li>
      {/if}
      <li class="header-li" title="Change theme">
        <button
          id="theme-button"
          class="header-button"
          aria-label="Switch Theme"
          on:click={toggleTheme}
        >
          <i
            id="theme-switch-span"
            class="fa-solid"
            class:fa-sun={$theme === "dark"}
            class:fa-moon={$theme === "light"}
          ></i>
        </button>
      </li>
      <li class="header-li" title={$showSidebar ? "Close menu" : "Open menu"}>
        <button
          id="toggle-sidebar"
          class="header-button"
          aria-label={$showSidebar ? "Close Menu" : "Open Menu"}
          on:click={toggleSidebar}
        >
          <i
            id="toggle-sidebar-span"
            class="fa-solid"
            class:fa-sliders={!$showSidebar}
            class:fa-circle-xmark={$showSidebar}
          ></i>
        </button>
      </li>
    </ul>
  </nav>
</header>

<Sidebar bind:this={sidebarComponent} />

<style>
  header {
    z-index: 20;
    position: sticky;
    top: 0;
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 15px 2rem;
    width: 100%;
    max-height: 90px;
    background: var(--header-background);
    transition: background 400ms ease-out;
    overflow-x: auto;
  }
  header.scrolled {
    background: transparent;
  }
  :root.light header.scrolled {
    background: transparent;
  }

  #header-ul {
    list-style: none;
    display: flex;
    gap: 20px;
    margin: 0;
  }
  .header-li {
    font-size: 2rem;
  }
  li:hover {
    transform: scale(1.2);
    color: var(--accent);
    text-shadow: 0px 0px 10px rgba(0, 0, 0, 0.267);
  }
  .header-button {
    margin: 0;
    padding: 10px;
    font-size: 1.4rem;
    background: transparent;
    color: var(--text-color);
    border: none;
    cursor: pointer;
    transition: color 150ms ease-in-out;
  }

  #header-logo-anchor img {
    filter: brightness(0) invert(1);
    transition: filter 200ms ease-in-out;
  }
  :root.light #header-logo-anchor img {
    filter: brightness(0);
  }
  :root.light #header-logo-anchor img:hover {
    filter: brightness(1);
  }
  #header-logo-anchor img:hover {
    filter: brightness(1.2);
  }
</style>