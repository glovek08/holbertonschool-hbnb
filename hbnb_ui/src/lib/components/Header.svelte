<header>
  <a id="header-logo-anchor" href="/">
    <picture id="header-logo-pictureset">
      <source srcset="/src/assets/images/main_logo.png" media="(max-width: 600px)" />
      <source
        srcset="/src/assets/images/hbnb_logo_black.png"
        media="(prefers-color-scheme: light)"
      />
      <source
        srcset="/src/assets/images/hbnb_logo_white.png"
        media="(prefers-color-scheme: dark)"
      />
      <img src="/src/assets/images/main_logo.png" alt="HBnB Logo" height="50"/>
    </picture>
  </a>
  <nav>
    <ul>
      <li>
        <a href="/" aria-label="User" title="User"><i class="fa-solid fa-user"></i></a
        >
      </li>
    </ul>
  </nav>
</header>

<style>
  header {
    /* outline: 1px solid green; */
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 10px 2rem;
    width: 100%;
    max-width: 100dvw;
    max-height: 90px;
    background: #08051d;
    background: linear-gradient(126deg, #3a0101 0%, #040a25 100%);
  }
  :root.light {
    header {
      background: #751b1b;
      background: linear-gradient(
        126deg,
        #f06e57 0%,
        #d87793 49%,
        #c579c5 100%
      );
    }
  }
  ul {
    /* outline: 1px solid red; */
    list-style: none;
    display: flex;
    gap: 20px;
    padding: 5px;
    margin: 0;
  }
  li {
    /* outline: 1px solid yellow; */
    padding: 10px;
    font-size: 1.2em;
    transition: transform ease-in-out 150ms;
    cursor: pointer;
  }
  li:hover {
    transform-origin: center;
    transform: scale(1.2);
    color: var(--accent);
    text-shadow: 0px 0px 10px rgba(0, 0, 0, 0.267);
  }
  #header-logo-pictureset {
    /* outline: 1px solid red; */
    display: flex;
    align-items: center;
    justify-content: center;
  }
</style>
