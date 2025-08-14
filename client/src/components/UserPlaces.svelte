<script>
  import PlaceCardSmall from "./PlaceCardSmall.svelte";
  import Button_2 from "./Button-2.svelte";
  import AddPlaceModal from "./AddPlaceModal.svelte";
  import { showAddPlaceModal } from "../lib/stores/add_place_modal";

  export let userPlaces = [];
  // console.log(`Receiving: ${userPlaces}`)
</script>

{#if $showAddPlaceModal}
  <AddPlaceModal/>
{/if}
<div id="user-placer-header">
  <h2>My Places</h2>
  <Button_2
    text="Add Place"
    title="Add Place"
    btnType="add"
    on:click={() => {showAddPlaceModal.set(true);}}
  />
</div>
{#if userPlaces.length > 0}
  {#each userPlaces as place}
    <PlaceCardSmall {place} />
  {/each}
{:else}
  <p>No places found.</p>
{/if}

<style>
  #user-placer-header {
    /* outline: 1px solid red; */
    width: 90%;
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 5px 1.3px;
  }
</style>
