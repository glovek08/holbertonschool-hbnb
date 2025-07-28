<script>
</script>

<footer>
  <div id="logo-container">
    <a id="footer-logo-anchor" href="/" title="Home" aria-label="Home">
      <img
        id="footer-logo-img"
        src="src/assets/images/main_logo.png"
        alt="HBnB Logo"
        height="100"
      /></a
    >
  </div>
  <section id="footer-info">
    <div id="footer-container">
      <div id="footer-info-wrapper">
        <div class="footer-item">
          <a class="footer-anchor"
            href="http://www.github.com/glovek08"
            target="_blank"
            rel="noopener noreferrer"
            >Gabriel Barn <i class="fa-brands fa-github"></i></a
          > / 
          <a class="footer-anchor"
            href="https://github.com/federico-paganini"
            target="_blank"
            rel="noopener noreferrer"
          >Federico Paganini <i class="fa-brands fa-github"></i></a
          >
        </div>
        <div class="horizontal-rule"></div>
        <div class="footer-item">
          <a href="/about">About</a> /
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
    background: var(--secondary-color);
    /* outline: 1px solid rgb(0, 255, 64); */
    color: var(--text-color);
    width: 100%;
    min-height: 100px;
    max-width: 100dvw;
    margin-top: 10px;
    display: flex;
    align-items: center;
    justify-content: center;
    flex-direction: column;
    gap: 20px;
    padding: 20px;
    text-align: center;
  }
  :root {
    footer {
      background: #08051d;
      background: linear-gradient(126deg, #080b16 0%, #220b0b 100%);
    }
  }
  :root.light {
    footer {
      background: #08051d;
      background: linear-gradient(126deg, #ee6d6d 0%, #b0bdec 100%);
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
  }
</style>
