<script>
  import Button_1 from "../components/Button-1.svelte";
  import Button_2 from "../components/Button-2.svelte";
  import PlaceCard from "../components/PlaceCard.svelte";
  import Carousel from "svelte-carousel";
  import { onMount } from "svelte";
  import api from "../lib/api";
  import { currentUserId } from "../lib/stores/auth";
  console.log(`Current User: ${$currentUserId}`);

  let particlesToShow = 3; /* For the Carousel, base cards to show */
  let places = [];

  const fetchPlaces = async () => {
    try {
      places = await api.getPlaces(9); //find way to randomize or get next 9.
      console.log("Fetched places:", places);
    } catch (error) {
      console.error("Error fetching places:", error);
    }
  };
  // dynamically set the ammount of cards shown in the places carousel by calculating the width of the
  // parent container.
  const calculateParticlesToShow = () => {
    const containerWidth =
      document.getElementById("places-carousel-container")?.offsetWidth || 0;
    particlesToShow = Math.floor(containerWidth / 340); // 300 width + 60px left/right padding
  };
  const shuffleCards = () => {
    console.log("Cards are shuffled, trust me bro.");
    places = [...places].sort(() => Math.random() - 0.5);
  };
  onMount(() => {
    fetchPlaces();
    calculateParticlesToShow();
    window.addEventListener("resize", calculateParticlesToShow);
    return () => window.removeEventListener("resize", calculateParticlesToShow);
  });
</script>

<section id="welcome-section" aria-label="Welcome to HBNB section">
  <svg
    xmlns="http://www.w3.org/2000/svg"
    viewBox="0 0 1400 320"
    id="waves-svg-bg"
  >
    <path
      fill="var(--header-background)"
      fill-opacity="1"
      d="M0,64L80,64C160,64,320,64,480,85.3C640,107,800,149,960,149.3C1120,149,1280,107,1360,85.3L1440,64L1440,0L1360,0C1280,0,1120,0,960,0C800,0,640,0,480,0C320,0,160,0,80,0L0,0Z"
    ></path>
  </svg>
  <div id="welcome-section-wrapper">
    <div id="welcome-section-svg-container" class="welcome-section-flex-item">
      <img
        src="/src/assets/images/welcome-home-1.svg"
        alt="House Search"
        height="400"
        id="house-search"
      />
    </div>
    <div id="user-welcome-container" class="welcome-section-flex-item">
      <h1 id="user-title">Welcome!</h1>
      <h3 id="user-subtitle">Let's find you a place :D</h3>
      <Button_1
        text="Find My Place"
        on:click={() => {
          const section = document.querySelector("#places-section");
          if (section) {
            section.scrollIntoView({ behavior: "smooth", block: "start" });
            console.log("Scrolling into view...");
          } else {
            console.warn("Section not found!");
          }
        }}
      />
    </div>
  </div>
</section>

<section id="places-section" aria-label="Section showing hot offers">
  <div id="places-carousel-container">
    <h2 class="places-section-h2">Hot places</h2>
    <p class="places-section-p">
      Discover a curated selection of our top-rated places—these exclusive
      offers are handpicked to give you the best experience. Explore the
      carousel above and find your next favorite stay!
    </p>
    {#if places.length > 0}
      <Carousel
        {particlesToShow}
        particlesToScroll={particlesToShow >= 3 ? 3 : 1}
        autoplay
        autoplayDuration={5000}
        autoplayProgressVisible
        pauseOnFocus
      >
        {#each places as place (place.id)}
          <PlaceCard
            place_id={place.id}
            title={place.title}
            description={place.description}
            price={place.price}
            rating={place.rating}
            image={place.image || "template-bnb.jpg"}
          />
        {/each}
      </Carousel>
    {:else}
      <p>Loading places...</p>
    {/if}
    <div id="places-carousel-toolbar">
      <Button_2
        text="Shuffle"
        title="Shuffle Place Listings"
        on:click={() => {
          shuffleCards();
        }}
      />
    </div>
  </div>
  <a href="/places"><Button_1 text="See All" /></a>
</section>

<style>
  :global(.button-1) {
    /* for this page only */
    font-size: 1.5rem;
    font-family: "Quicksand";
    font-style: normal;
    padding: 20px 40px !important;
  }
  #welcome-section {
    /* outline: 1px solid red; */
    /* position: relative; Might fuck things up, in that case, revert to normal positioning. */
    width: 100%;
    min-height: 100%;
    display: flex;
    align-items: center;
    justify-content: center;
    flex-direction: column;
    overflow: hidden;
    padding: 50px 20px;
  }
  #waves-svg-bg {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    z-index: -1;
    object-fit: cover;
    pointer-events: none;
    transition: 500ms ease-in-out; /* Might not work, but this is essentially to
    simulate the transition of the header on scrollY*/
  }
  #welcome-section-wrapper {
    /* outline: 1px solid red; */
    padding: 20px;
    display: flex;
    align-items: center;
    justify-content: space-between;
    flex-wrap: wrap-reverse;
    gap: 20px;
    position: relative;
    left: -40px;
  }

  .welcome-section-flex-item {
    /* outline: 1px solid blue; */
    padding: 20px;
  }

  #user-welcome-container {
    /* outline: 1px solid yellow; */
    display: flex;
    align-items: center;
    justify-content: center;
    flex-direction: column;
    text-align: left;
    font-size: 1.5rem;
    max-width: 500px;
  }
  #user-title {
    align-self: flex-start;
    padding: 0;
    margin: 0;
    font-family: Playwrite;
  }
  #user-subtitle {
    padding: 10px;
    margin: 0 0 50px 0;
  }

  @media screen and (max-width: 1200px) {
    #welcome-section-wrapper {
      padding-top: 0;
      margin-top: 0;
      align-items: center;
      justify-content: center;
      position: static;
    }
    #house-search {
      width: 100%;
    }
  }

  /* ********************* PLACE CAROUSEL *********************** */
  #places-section {
    margin-top: 150px;
    background: var(--header-background);
    width: 100%;
    min-height: 200px;
    padding: 100px 30px;
    display: flex;
    align-items: center;
    justify-content: center;
    flex-direction: column;
    gap: 40px;
  }
  .places-section-h2 {
    text-align: left;
    width: 100%;
    margin-left: 30px;
    font-size: 2.5rem;
    margin: 0 0 0 60px;
  }
  .places-section-p {
    width: 100%;
    padding: 10px 40px;
    margin-top: 0;
  }
  #places-carousel-container {
    background: var(--background-primary);
    border-radius: 10px;
    width: 93%;
    max-width: 3000px;
    display: flex;
    align-items: center;
    justify-content: center;
    flex-direction: column;
    gap: 15px;
    padding: 50px 60px;
    overflow: visible;
    position: relative;
  }
  #places-carousel-toolbar {
    /* outline: 1px solid red; */
    padding: 5px;
    width: 100%;
    gap: 20px;
    display: flex;
    align-items: center;
    justify-content: flex-end;
  }
  @media screen and (max-width: 600px) {
    .places-section-h2,
    .places-section-p {
      margin: 0;
      padding: 0;
      text-align: center;
    }
    #places-carousel-container {
      width: 100dvw;
    }
  }
</style>
