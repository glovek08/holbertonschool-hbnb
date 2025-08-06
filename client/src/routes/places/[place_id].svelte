<script>
  import { params } from "@roxi/routify";
  import { onMount } from "svelte";
  import AuthBox from "../../components/AuthBox.svelte";
  import Button_1 from "../../components/Button-1.svelte";
  import ReviewCard from "../../components/ReviewCard.svelte";
  import RatingBox from "../../components/RatingBox.svelte";
  import api from "../../lib/api";

  let place;
  let place_id;
  let place_reviews;

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
    fetchPlace();
    // fetchReviews();
  }
</script>

<AuthBox>
  {#if place}
    <section
      id="place-details-section"
      style="background-image: url({place.image || '/template-bnb.jpg'});"
    >
      <div id="place-details-card">
        <h1>{place.title}</h1>
        <p class="place-description">{place.description}</p>

        <div class="renting-info-box">
          <div id="place-rating-price-container">
            <div class="price">
              <strong>${place.price}</strong> per Day
            </div>
            <RatingBox rating={place.rating}></RatingBox>
          </div>
          <Button_1 text="RESERVE" />
        </div>
      </div>
    </section>
    <section id="reviews-section">
      <h2>Check out these reviews!</h2>
      {#if place_reviews}
        {#each place_reviews as review}
          <ReviewCard
            authorFirstName={review.author_first_name}
            authorLastName={review.author_last_name}
            rating={review.rating}
            comment={review.comment}
          />
        {/each}
      {/if}
    </section>
  {:else}
    <p>Loading place details...</p>
  {/if}
</AuthBox>

<style>
  #place-details-section :global(.rating-container) {
    /* outline: 1px solid blue; */
    width: fit-content;
  }
  #place-details-section {
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
  }

  #place-details-card {
    background: var(--card-desc-background);
    backdrop-filter: blur(10px);
    border-radius: 5px;
    padding: 2rem;
    box-shadow: 0 4px 20px rgba(0, 0, 0, 0.15);
    width: 100%;
    max-width: 450px;
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
    min-height: 700px;
    max-height: 1000px;
    height: 100px;
    overflow-y: scroll;
    display: flex;
    align-items: center;
    justify-content: flex-start;
    flex-direction: column;
    padding: 10px;
    scrollbar-width: thin;
    scrollbar-color: var(--accent) transparent;
  }
  #reviews-section h2 {
    align-self: flex-start;
    margin-left: 20px;
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
  @media (max-width: 768px) {
    #place-details-section {
      justify-content: center;
      padding: 1rem;
      min-height: 80vh;
    }

    #place-details-card {
      max-width: 100%;
    }
  }
</style>
