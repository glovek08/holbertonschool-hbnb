<script>
  import { onMount } from "svelte";
  import api from "../lib/api";

  export let amenitiesID = [];
  let amenitiesDetail = [];

  $: if (amenitiesID && amenitiesID.length > 0) {
    fetchAmenities();
  }
  async function fetchAmenities() {
    console.log(
      "Calling with IDs:",
      amenitiesID.map((a) => a.id || a)
    );
    amenitiesDetail = await Promise.all(
      amenitiesID.map((a) => api.getAmenityById(a.id || a))
    );
  }
</script>

<div id="place-amenities-box" class="place-information-container-item">
  <h3>Amenities included:</h3>
  <div id="amenities-svgs-container">
    {#each amenitiesDetail as amenity}
      <img
        src={"/src/assets/svgs/"+amenity.icon || "/src/assets/svgs/no_data.svg"}
        class="place-amentiy-svg"
        alt={amenity.name}
        width="30"
        height="30"
        title={amenity.name}
      />
    {/each}
  </div>
</div>

<style>
  #place-amenities-box {
    padding: 10px 20px;
  }
  #place-amenities-box h3 {
    margin: 5px 0 10px 0;
  }
  #amenities-svgs-container {
    /* outline: 1px solid rgb(12, 12, 122); */
    width: 100%;
    display: flex;
    align-items: center;
    justify-content: flex-start;
    gap: 10px;
    padding: 2px 10px 10px 10px;
  }
  :root {
    #amenities-svgs-container {
      filter: invert(1);
    }
  }
  :root.light {
    #amenities-svgs-container {
      filter: invert(0);
    }
  }
</style>
