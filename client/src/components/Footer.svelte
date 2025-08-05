<script>
</script>

<footer>
  <div id="logo-container">
    <a id="footer-logo-anchor" href="/" title="Home" aria-label="Home">
      <img
        id="footer-logo-img"
        src="/main_logo.webp"
        alt="HBnB Logo"
        height="100"
        width="100"
      /></a
    >
  </div>
  <section id="footer-info">
    <div id="footer-container">
      <div id="footer-info-wrapper">
        <div class="footer-item">
          <a
            class="footer-anchor"
            href="https://www.github.com/glovek08"
            target="_blank"
            rel="noopener noreferrer"
            aria-label="Gabriel Barn github link"
            >Gabriel Barn <i class="fa-brands fa-github"></i></a
          >
          <a
            class="footer-anchor"
            href="https://www.github.com/federico-paganini"
            target="_blank"
            rel="noopener noreferrer"
            aria-label="Federico Paganini github link"
            >Federico Paganini <i class="fa-brands fa-github"></i></a
          >
        </div>
        <div class="horizontal-rule"></div>
        <div class="footer-item">
          <a href="/about">About</a>
          <a href="/contact">Contact</a>
        </div>
        <h3 class="playwrite">Made in Uruguay</h3>
      </div>
    </div>
  </section>
  <p>Holberton MVD - 2025</p>
</footer>

<style>
  footer {
    /* outline: 1px solid rgb(0, 255, 64); */
    color: var(--text-color);
    width: 100%;
    min-height: 100px;
    margin-top: 10px;
    display: flex;
    align-items: center;
    justify-content: center;
    flex-direction: column;
    gap: 20px;
    padding: 50px 20px 20px 20px;
    text-align: center;
  }
  :root {
    footer {
      background: url("/src/assets/svgs/footer_bg_dark.svg");
      background-size: cover;
      background-position: center;
      background-repeat: no-repeat;
    }
  }
  :root.light {
    footer {
      background: url("/src/assets/svgs/footer_bg_light.svg");
      background-size: cover;
      background-position: center;
      background-repeat: no-repeat;
    }
  }
  #footer-logo-img {
    filter: grayscale(1);
    transition: filter ease-in-out 240ms;
  }
  #footer-logo-img:hover {
    filter: grayscale(0);
  }
  #footer-info {
    /* outline: 1px solid yellow; */
    font-size: 1.2rem;
    display: flex;
    align-items: center;
    justify-content: center;
    width: 90%;
    min-height: 100px;
  }
  #footer-info-wrapper {
    /* outline: 1px solid red; */
    display: flex;
    align-items: center;
    justify-content: center;
    flex-wrap: wrap;
    gap: 20px;
    margin-bottom: 20px;
  }
  .footer-item {
    /* outline: 1px solid blue; */
    padding: 2px;
    margin: 2px;
    font-weight: 100;
    text-align: left;
    min-width: 220px;
  }
  .footer-item a {
    margin: 10px;
  }
  footer a:hover {
    text-shadow: 0 0 10px var(--background-color);
  }
  .footer-anchor {
    /* outline: 1px solid green;  */
    text-align: right;
    margin: 2px;
    text-wrap: nowrap;
  }
  .horizontal-rule {
    width: 1px;
    min-height: 45px;
    background: var(--text-color);
  }

  @media (max-width: 720px) {
    .horizontal-rule {
      display: none;
    }
    .footer-item {
      display: flex;
      align-items: center;
      justify-content: center;
      width: 100%;
      flex-direction: column;
    }
    .footer-anchor {
      margin: 10px;
    }
  }
</style>
