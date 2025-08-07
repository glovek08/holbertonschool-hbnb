<script>
  import RatingBox from "./RatingBox.svelte";
  export let authorFirstName = "n/a";
  export let authorLastName = "n/a";
  export let rating = 0;
  export let comment = "n/a";
  // export let reviewAuthorID = ""
</script>

<div class="review-container">
  <RatingBox {rating} />
  <h3 class="user-name-title">
    <a href="/This will take to review author" aria-label="Review Author"
      >{authorFirstName} {authorLastName}</a
    >
  </h3>
  <p class="review-comment">{comment}</p>
</div>

<style>
  :root {
    --review-background: rgba(48, 48, 51, 0.712);
    --review-shadow: rgba(0, 0, 0, 0.5);
  }
  :root.light {
    --review-background: white;
    --review-shadow: rgba(0, 0, 0, 0.24);
  }
  :global(.rating-container) {
    width: fit-content;
  }
  .review-container {
    /* outline: 1px solid red; */
    border-radius: 20px;
    background: var(--review-background);
    min-width: 300px;
    max-width: 800px;
    padding: 25px 30px 10px 30px;
    box-shadow: 5px 5px 9px var(--review-shadow);
  }
</style>
