<script>
  import RatingBox from "./RatingBox.svelte";

  export let review = {};

  $: ({
    author_first_name: authorFirstName = "n/a",
    author_last_name: authorLastName = "n/a",
    rating = 0,
    comment = "n/a",
    user_id: reviewAuthorID = "",
  } = review);
</script>

<div class="review-container">
  <div class="review-header">
    <h3 class="user-name-title">
      <a href="/user/{reviewAuthorID}" aria-label="Review Author Profile">
        {authorFirstName}
        {authorLastName}
      </a>
    </h3>
    <RatingBox {rating} />
  </div>
  <div class="review-body">
    <p class="review-comment">{comment}</p>
  </div>
</div>

<style>
  :global(.rating-container) {
    width: fit-content;
  }
  .review-container {
    border-radius: 20px;
    background: var(--user-dashboard-card-bg, #fff);
    box-shadow: 5px 5px 9px
      var(--user-dashboard-card-shadow, rgba(0, 0, 0, 0.1));
    width: clamp(300px, 90%, 800px);
    padding: 20px 30px;
    margin-bottom: 10px;
  }
  .review-header {
    /* outline: 1px solid red; */
    width: 100%;
    display: flex;
    align-items: center;
    justify-content: space-between;
  }
  .user-name-title {
    margin: 0;
  }
  .user-name-title a {
    text-decoration: none;
    color: inherit;
  }
  .user-name-title a:hover {
    text-decoration: underline;
  }
  @media screen and (max-width: 800px) {
    .review-container {
      font-size: 1.5dvw;
      width: fit-content;
      padding: 2dvw 3dvw 1dvw 3dvw;
    }
  }
  @media screen and (max-width: 400px) {
    .review-container {
      padding: 2dvw 5dvw 1dvw 5dvw;
    }
  }
</style>
