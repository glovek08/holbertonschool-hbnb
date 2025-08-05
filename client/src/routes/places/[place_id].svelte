<script>
  import AuthBox from "../../components/AuthBox.svelte";
  import Button_1 from "../../components/Button-1.svelte";
  import api from "../../lib/api";
  import { params } from "@roxi/routify";
  import { onMount } from "svelte";

  let place_id;
  let place;

  $: place_id = $params.place_id; // <- must understand this!
  console.log($params);

  async function fetchPlace() {
    // catches the api.getPlace exception from deeper.
    try {
      place = await api.getPlace(place_id);
      console.log("Fetched place:", place);
    } catch (error) {
      console.error(`Error fetching place: ${error}`);
    }
  }
  $: if (place_id) {
    fetchPlace();
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
          <div class="price">
            <strong>${place.price}</strong> per Day
          </div>
          <Button_1 text="RESERVE" />
        </div>
      </div>
    </section>
  {:else}
    <p>Loading place details...</p>
  {/if}
</AuthBox>

<h3>HERE, ANOTHER CAROUSEL WILL GO</h3>
<small>Said yoda</small>

<style>
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
    margin: 20px 0;
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
    font-size: 1.5rem;
  }
  .price strong {
    font-weight: 700;
    font-size: 2rem;
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
