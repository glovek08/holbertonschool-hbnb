<script>
  import AuthBox from "../../components/AuthBox.svelte";
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
    <h1>{place.title}</h1>
    <p>{place.description}</p>
  {:else}
    <p>Loading place details...</p>
  {/if}
</AuthBox>

<style>
  h1 {
    font-size: 3rem;
  }
</style>
