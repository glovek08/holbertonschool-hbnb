<script>
  import { onMount } from "svelte";
  import PlaceCard from "../components/PlaceCard.svelte";
  import api from "../lib/api";

  let places = [];

  const fetchPlaces = async () => {
    try {
      places = await api.getPlaces();
      console.log("Fetched places:", places);
    } catch (error) {
      console.error("Error fetching places:", error);
    }
  };
  onMount(() => {
    fetchPlaces();
  });
</script>

<section id="places-grid-section">
  <div id="places-grid-toolbox">
    <input
      type="search"
      name="places-toolbox-search"
      id="places-toolbox-search"
      maxlength="60"
      placeholder="Search Place"
    />
    <div id="places-toolbox-btn-container">
      <button
        class="places-toolbox-btn"
        aria-label="Sort Descending"
        title="Sort Descending"
      >
        <i class="fa-solid fa-arrow-down-short-wide"></i>
      </button>
      <button
        class="places-toolbox-btn"
        aria-label="Sort Ascending"
        title="Sort Ascending"
      >
        <i class="fa-solid fa-arrow-down-wide-short"></i>
      </button>
      <button
        class="places-toolbox-btn"
        aria-label="Search? IDK"
        title="Search? IDK"
      >
        <i class="fa-solid fa-magnifying-glass"></i>
      </button>
    </div>
  </div>
  <div id="places-grid-container">
    {#each places as place (place.id)}
      <PlaceCard
        place_id={place.id}
        title={place.title}
        description={place.description}
        price={place.price}
        image={place.image || "template-bnb.jpg"}
        rating={place.rating}
        
      />
    {/each}
  </div>
</section>

<style>
  #places-grid-section {
    background: var(--background-primary);
    border-radius: 10px;
    width: 90%;
    width: clamp(400px, 1520px, 3040px);
    min-width: 400px;
    width: 74.6%;
    max-width: 2280px;
    height: 2400px;
  }
  #places-grid-toolbox {
    background: var(--gray);
    border-top-left-radius: 10px;
    border-top-right-radius: 10px;
    display: flex;
    align-items: center;
    justify-content: space-between;
    height: 50px;
    padding: 20px 3%;
    gap: 20px;
    overflow-x: auto;
    overflow-y: hidden;
  }
  #places-toolbox-search {
    background-color: var(--background-primary);
    border: none;
    padding: 5px 10px;
    border-radius: 10px;
    color: var(--font-primary);
    min-width: 80px;
    max-width: 250px;
  }
  #places-toolbox-btn-container {
    padding: 0px;
    display: flex;
    align-items: center;
    justify-content: center;
    flex-wrap: nowrap;
    gap: 10px;
  }
  .places-toolbox-btn {
    min-width: 30px;
    background-color: var(--background-primary);
    color: var(--font-primary);
    border: none;
    padding: 9px;
    border-radius: 10px;
    border: 2px solid transparent;
    transition: border ease-in-out 200ms;
  }
  .places-toolbox-btn:hover {
    color: var(--accent);
    border: 2px solid var(--accent);
    cursor: pointer;
  }
  #places-grid-container {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
    place-items: center;
    row-gap: 30px;
    width: 100%;
    padding: 40px;
  }
</style>
