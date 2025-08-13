<script>
  import { params } from "@roxi/routify";
  import { onMount } from "svelte";
  import AuthBox from "../../components/AuthBox.svelte";
  import Button_1 from "../../components/Button-1.svelte";
  import ReviewCard from "../../components/ReviewCard.svelte";
  import RatingBox from "../../components/RatingBox.svelte";
  import api from "../../lib/api";
  import { isAuthenticated } from "../../lib/stores/auth";
  import AmenitiesBox from "../../components/AmenitiesBox.svelte";

  console.clear();

  let place;
  let place_id;
  let place_reviews;
  let place_amenities;

  $: place_id = $params.place_id; // <- Can update to Svelte5 run'es once routify 4 releases.

  async function fetchPlace() {
    // catches the api.getPlace exception from deeper.
    try {
      place = await api.getPlace(place_id);
      console.log("Fetched place:", place);
      place_reviews = place.reviews;
      console.log(
        "Fetches place reviews: " + JSON.stringify(place.reviews, null, 2)
      );
      place_amenities = place.amenities;
      console.log(
        "Fetches place amenities: " + JSON.stringify(place.amenities, null, 2)
      );
    } catch (error) {
      console.error(`Error fetching place: ${error}`);
    }
  }

  // I'm storing each review inside the place model, but leaving fetching reviews
  // separatelly until I ask cape what version is better.
  // async function fetchReviews() {
  //   try {
  //     place_reviews = await api.getPlaceReviews(place_id);
  //     console.log("Fetched place reviews: ", place_reviews);
  //   } catch (error) {
  //     console.error(`Error fetching place reviews: ${error}`);
  //   }
  // }
  $: if (place_id) {
    if ($isAuthenticated) {
      fetchPlace();
      // fetchReviews();
    }
  }
</script>

<AuthBox>
  {#if place}
    <section
      id="place-details-section"
      style="background-image: url({place.image || '/template-bnb.jpg'});"
    >
      <div id="image-credit">
        Photo by {place.image_author} on
        <a href="http://unsplash" target="_blank" rel="noopener noreferrer"
          >Unsplash</a
        >
      </div>
      <!-- This button will link to this place's gallery -->
      <button
        id="place-gallery-btn"
        aria-label="Place Gallery"
        title="Place Gallery"
        style="background-image: url({place.image || '/template-bnb.jpg'});"
      ></button>
      <div id="place-information-container">
        <div id="place-details-card" class="place-information-container-item">
          <h1>{place.title}</h1>
          <p class="place-description">{place.description}</p>

          <div class="renting-info-box">
            <div id="place-rating-price-container">
              <div class="price">
                <strong>${place.price}</strong> per Day
              </div>
              <RatingBox rating={place.rating}></RatingBox>
            </div>
            <Button_1
              text="RESERVE"
              title="Reserve this place"
              ariaLabel="Reserve this place"
            />
          </div>
        </div>
        {#if place.amenities}
          <AmenitiesBox amenitiesID={place_amenities} />
        {/if}
      </div>
    </section>
    <section id="reviews-section">
      <h2>Check out these reviews!</h2>
      {#if place_reviews}
        {#each place_reviews as review}
          <ReviewCard review={review}/>
        {/each}
      {/if}
    </section>
  {:else}
    <p>Loading place details...</p>
  {/if}
</AuthBox>

<style>
  :global(.place-information-container-item) {
    /* This affects both cards in place description */
    background: var(--card-desc-background);
    box-shadow: 0 4px 20px rgba(0, 0, 0, 0.385);
    backdrop-filter: blur(10px);
    border-radius: 10px;
    width: 100%;
    max-width: 450px;
  }
  #place-details-section :global(.rating-container) {
    /* outline: 1px solid blue; */
    width: fit-content;
  }
  #place-details-section {
    /* outline: 1px solid red; */
    width: 90%;
    max-width: 2000px;
    min-height: 700px;
    max-height: 1000px;
    padding: 2rem;
    display: flex;
    align-items: center;
    justify-content: flex-end;
    background-size: cover;
    background-position: center;
    border-radius: 5px;
    margin: 20px 0 0 0;
    color: var(--card-font-color);
    box-shadow: inset 0 0 120px black;
    transition: 1200ms;
    position: relative;
    overflow: hidden;
  }
  #place-details-section::before {
    content: "";
    position: absolute;
    inset: 0;
    z-index: 0;
    background-image: inherit; /* or set the same background-image as the parent */
    background-size: cover;
    background-position: center;
    filter: blur(10px); /* Adjust blur as needed */
    pointer-events: none;
  }
  #place-details-section > * {
    position: relative;
    z-index: 1;
  }
  #image-credit {
    position: absolute;
    left: 10dvw;
    align-self: flex-end;
    color: white;
    margin-left: 0;
    margin-right: auto;
    font-size: 0.8rem;
    text-shadow: 0 0 2px rgb(0, 0, 0);
  }
  #place-gallery-btn {
    /* outline: 1px solid green; */
    min-height: 600px;
    background-size: cover;
    background-position: center top;
    animation: pan-bg 30s ease-out infinite alternate;
    border: none;
    box-shadow: 0px 0px 200px var(--shadow-primary);
    min-width: 400px;
    width: 50%;
    margin-right: 5%;
    cursor: pointer;
    border-radius: 10px;
    transition: transform 1500ms cubic-bezier(0.4, 0, 0.2, 1);
  }
  #place-gallery-btn:hover {
    transform: scale(1.05);
  }
  #place-information-container {
    /* outline: 1px solid yellow; */
    padding: 10px;
    gap: 20px;
    display: flex;
    align-items: center;
    justify-content: center;
    flex-direction: column;
  }

  #place-details-card {
    /* outline: 1px solid green; */
    padding: 2rem;
    display: flex;
    flex-direction: column;
    gap: 1rem;
  }

  #place-rating-price-container {
    /* outline: 1px solid yellow; */
    display: flex;
    align-items: center;
    justify-content: space-between;
    width: 100%;
  }

  .place-description {
    line-height: 1.6;
  }

  .renting-info-box {
    border-top: 1px solid var(--accent);
    padding-top: 1rem;
    margin-top: 1rem;
    display: flex;
    flex-direction: column;
    gap: 1rem;
  }

  .price {
    /* outline: 1px solid red; */
    font-size: 1.5rem;
    width: fit-content;
  }
  .price strong {
    font-weight: 700;
    font-size: 2rem;
  }
  /* *********************** REVIEWS SECTION ************************* */
  #reviews-section {
    /* outline: 1px solid red; */
    width: 90%;
    max-width: 2000px;
    min-height: 400px;
    max-height: 1000px;
    overflow-y: scroll;
    display: flex;
    align-items: center;
    justify-content: flex-start;
    flex-direction: column;
    padding: 10px;
    scrollbar-width: thin;
    scrollbar-color: var(--accent) transparent;
  }
  #reviews-section::-webkit-scrollbar {
    width: 6px;
  }

  #reviews-section::-webkit-scrollbar-thumb {
    background: rgba(0, 0, 0, 0.5);
    border-radius: 10px;
  }

  #reviews-section::-webkit-scrollbar-thumb:hover {
    background: rgba(0, 0, 0, 0.7);
  }

  #reviews-section::-webkit-scrollbar-track {
    background: transparent;
  }
  @media (min-width: 1800px) {
    #image-credit {
      left: 50%;
    }
  }
  @media (max-width: 900px) {
    #place-details-section {
      height: fit-content;
      justify-content: center;
      padding: 1rem;
      min-height: 80vh;
      height: auto;
      flex-direction: column;
      max-height: 3000px;
    }
    #place-information-container {
      order: 1;
      width: 100%;
      max-width: 100%;
      padding: 0;
      margin-top: 100px;
    }
    #place-gallery-btn {
      order: 2;
      width: 100%;
      min-width: unset;
      margin-right: 0;
      min-height: 300px;
      margin-top: 20px;
    }
    #place-details-card {
      max-width: 100%;
    }
    #reviews-section {
      margin-top: 150px;
    }
    #image-credit {
      top: 140px;
    }
  }
  @keyframes pan-bg {
    from {
      background-position: center top;
    }
    to {
      background-position: center bottom;
    }
  }
</style>
