<script>
  import { onMount } from "svelte";
  let headerElement;
  let isScrolled = false;

  onMount(() => {
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
    <img src="src/assets/images/main_logo.png" alt="HBnB Logo" height="40" />
  </a>
  <nav>
    <ul>
      <li>
        <a href="/login" aria-label="User" title="User" class="header_button"
          ><i class="fa-solid fa-user"></i></a
        >
      </li>
    </ul>
  </nav>
</header>

<style>
  header {
    /* outline: 1px solid green; */
    z-index: 1000;
    position: sticky;
    top: 0;
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 5px 2rem;
    width: 100%;
    max-height: 90px;
    background: var(--header-background);
    transition: background 500ms ease-in-out;
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
    display: flex;
    gap: 20px;
    margin: 0;
  }
  li {
    /* outline: 1px solid yellow; */
    padding: 15px;
    font-size: 1.4em;
    transition: transform ease-in-out 150ms;
    cursor: pointer;
  }
  li:hover {
    transform-origin: center;
    transform: scale(1.2);
    color: var(--accent);
    text-shadow: 0px 0px 10px rgba(0, 0, 0, 0.267);
  }
  #header-logo-anchor {
    display: flex;
    align-items: center;
    justify-content: center;
  }

  #header-logo-anchor img {
    filter: brightness(5);
    transition: filter 200ms ease-in-out;
  }
  :root.light #header-logo-anchor img {
    filter: brightness(0);
  }
    :root.light #header-logo-anchor img:hover {
    filter: brightness(0.9);
  }
  #header-logo-anchor img:hover {
    filter: brightness(1.2);
  }
</style>
