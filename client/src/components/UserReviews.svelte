<script>
  import ReviewCard from "./ReviewCard.svelte";

  export let userReviews = [];
</script>

{#if userReviews.length > 0}
  <ul class="user-review-ul">
    {#each userReviews as review}
      <li>
        <ReviewCard
          authorFirstName={review.author_first_name}
          authorLastName={review.author_last_name}
          rating={review.rating}
          comment={review.comment}
        />
      </li>
    {/each}
  </ul>
{:else}
  <p>No reviews found.</p>
{/if}

<style>
  .user-review-ul {
    width: 100%;
    padding: 20px;
  }
  .user-review-ul li {
    padding: 0;
    margin: 0;
  }
</style>
