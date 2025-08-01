<script>
  import { onMount } from "svelte";
  import Sidebar from "./Sidebar.svelte";
  let headerElement;
  let isScrolled = false;
  let sidebarComponent;

  /******** SIDEBAR CRAP **********/
  let showSidebar = false;
  let userLoggedIn = false;
  function toggleSidebar() {
    const toggleSidebarSpan = document.querySelector("#toggle-sidebar-span");

    if (showSidebar) {
      // Use the sidebar's animated close instead of direct toggle
      if (sidebarComponent) {
        sidebarComponent.requestClose();
      }
      // Update icon immediately
      if (toggleSidebarSpan) {
        toggleSidebarSpan.classList.add("fa-sliders");
        toggleSidebarSpan.classList.remove("fa-circle-xmark");
      }
    } else {
      // Opening sidebar
      showSidebar = true;
      if (toggleSidebarSpan) {
        toggleSidebarSpan.classList.remove("fa-sliders");
        toggleSidebarSpan.classList.add("fa-circle-xmark");
      }
    }
  }
  function closeSidebar() {
    showSidebar = false;
    // Reset the icon when sidebar closes
    const toggleSidebarSpan = document.querySelector("#toggle-sidebar-span");
    if (toggleSidebarSpan) {
      toggleSidebarSpan.classList.add("fa-sliders");
      toggleSidebarSpan.classList.remove("fa-circle-xmark");
    }
  }

  function toggleTheme() {
    const root = document.documentElement;
    const themeIcon = document.querySelector("#theme-switch-span");

    if (root.classList.contains("light")) {
      // switch to dark theme
      root.classList.remove("light");
      themeIcon.classList.remove("fa-moon");
      themeIcon.classList.add("fa-sun");
      localStorage.setItem("theme", "dark");
    } else {
      // switch to light theme
      root.classList.add("light");
      themeIcon.classList.remove("fa-sun");
      themeIcon.classList.add("fa-moon");
      localStorage.setItem("theme", "light");
      // Remember to respect the fucking user preferences!
    }
    window.dispatchEvent(new CustomEvent("themechange"));
  }
  onMount(() => {
    const savedTheme = localStorage.getItem("theme");
    const root = document.documentElement;
    const themeIcon = document.querySelector("#theme-switch-span");
    if (savedTheme === "light") {
      root.classList.add("light");
      if (themeIcon) {
        themeIcon.classList.remove("fa-sun");
        themeIcon.classList.add("fa-moon");
      }
    } else {
      root.classList.remove("light");
      if (themeIcon) {
        themeIcon.classList.remove("fa-moon");
        themeIcon.classList.add("fa-sun");
      }
    }
    const handleScroll = () => {
      const scrollY = window.scrollY;
      if (scrollY > 100) {
        isScrolled = true;
      } else {
        isScrolled = false;
      }
    };

    window.addEventListener("scroll", handleScroll);

    return () => {
      window.removeEventListener("scroll", handleScroll);
    };
  });
</script>

<header bind:this={headerElement} class:scrolled={isScrolled}>
  <a id="header-logo-anchor" href="/">
    <img src="main_logo.png" alt="HBnB Logo" height="40" />
  </a>
  <nav>
    <ul>
      <li>
        <button
          id="theme-button"
          class="header-button"
          aria-label="Switch Theme"
          on:click={toggleTheme}
          ><i id="theme-switch-span" class="fa-solid fa-sun"></i></button
        >
      </li>
      <li>
        <button
          id="toggle-sidebar"
          class="header-button"
          aria-label={showSidebar ? "Close Menu" : "Open Menu"}
          on:click={toggleSidebar}
          ><i id="toggle-sidebar-span" class="fa-solid fa-sliders"></i></button
        >
      </li>
    </ul>
  </nav>
</header>

<Sidebar bind:this={sidebarComponent} show={showSidebar} {closeSidebar} />

<style>
  header {
    /* outline: 1px solid green; */
    z-index: 20;
    position: -webkit-sticky;
    position: sticky;
    top: 0;
    display: -webkit-box;
    display: -ms-flexbox;
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 15px 2rem;
    width: 100%;
    max-height: 90px;
    background: var(--header-background);
    transition: background 400ms ease-out;
    -webkit-transition: background 400ms ease-out;
  }
  header:hover {
    background: var(--header-background);
  }
  header.scrolled {
    background: transparent;
  }
  :root.light header.scrolled {
    background: transparent;
  }

  ul {
    /* outline: 1px solid red; */
    list-style: none;
    display: -webkit-box;
    display: -ms-flexbox;
    display: flex;
    gap: 20px;
    margin: 0;
  }
  ul > li:not(:last-child) {
    margin-right: 20px;
  }

  li {
    /* outline: 1px solid yellow; */
    padding: 0;
    margin: 0;
    font-size: 1.4em;
    transition: transform ease-in-out 150ms;
    cursor: pointer;
    display: flex;
    align-items: center;
    justify-content: center;
  }
  li:hover {
    transform-origin: center;
    transform: scale(1.2);
    color: var(--accent);
    text-shadow: 0px 0px 10px rgba(0, 0, 0, 0.267);
    .header-button {
      color: var(--accent);
    }
  }
  .header-button {
    /* outline: 1px solid red; */
    margin: 0;
    padding: 10px;
    font-size: 1.4rem;
    background: transparent;
    color: var(--text-color);
    border: none;
    cursor: pointer;
    transition: color 150ms ease-in-out;
  }

  #header-logo-anchor {
    display: flex;
    align-items: center;
    justify-content: center;
  }

  #header-logo-anchor img {
    -webkit-filter: brightness(5);
    filter: brightness(0) invert(1);
    transition: filter 200ms ease-in-out;
    -webkit-transition: -webkit-filter 200ms ease-in-out;
  }

  :root.light #header-logo-anchor img {
    -webkit-filter: brightness(0);
    filter: brightness(0);
  }
  :root.light #header-logo-anchor img:hover {
    -webkit-filter: brightness(1);
    filter: brightness(1);
  }
  #header-logo-anchor img:hover {
    -webkit-filter: brightness(1.2);
    filter: brightness(1.2);
  }
</style>
