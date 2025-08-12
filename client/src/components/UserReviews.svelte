<script>
  import ReviewCard from "./ReviewCard.svelte";

  export let userReviews = [];
</script>

<h2>My Reviews</h2>
{#if userReviews.length > 0}
  {#each userReviews as review}
    <ReviewCard review={review}/>
  {/each}
{:else}
  <p>No reviews found.</p>
{/if}

<style>
</style>
