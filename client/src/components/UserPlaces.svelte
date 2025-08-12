<script>
  export let userPlaces = [];


</script>

<h2>My Places</h2>
{#if userPlaces.length > 0}
  Hee
{:else}
  <p>No places found.</p>
{/if}
