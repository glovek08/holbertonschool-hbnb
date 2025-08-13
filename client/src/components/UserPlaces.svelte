<script>
  import PlaceCardSmall from "./PlaceCardSmall.svelte";

  export let userPlaces = [];
  // console.log(`Receiving: ${userPlaces}`)
</script>

<h2>My Places</h2>
{#if userPlaces.length > 0}
  {#each userPlaces as place}
    <PlaceCardSmall {place} />
  {/each}
{:else}
  <p>No places found.</p>
{/if}
