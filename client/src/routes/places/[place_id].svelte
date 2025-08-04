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
    try {
      place = await api.getPlace(place_id);
    } catch (error) {
      console.error(`Error fetching place: ${error}`);
    }
  }
  onMount(() => {
    fetchPlace();
  });
</script>

<AuthBox>
  <h1 class="">Place Details</h1>
</AuthBox>

<style>
  h1 {
    font-size: 3rem;
  }
</style>
