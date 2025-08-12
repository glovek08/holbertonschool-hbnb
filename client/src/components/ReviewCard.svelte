<script>
  import RatingBox from "./RatingBox.svelte";

  export let review = {};

  $: ({
    author_first_name: authorFirstName = "n/a",
    author_last_name: authorLastName = "n/a", 
    rating = 0,
    comment = "n/a",
    user_id: reviewAuthorID = ""
  } = review);
</script>

<div class="review-container">
  <div class="review-header">
    <h3 class="user-name-title">
      <a href="/user/{reviewAuthorID}" aria-label="Review Author Profile">
        {authorFirstName} {authorLastName}
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
    box-shadow: 5px 5px 9px var(--user-dashboard-card-shadow, rgba(0,0,0,0.1));
    width: clamp(300px, 90%, 800px);
    padding: 25px 30px 10px 30px;
    margin-bottom: 1rem;
  }
  .review-header {
    width: 100%;
    display: flex;
    align-items: center;
    justify-content: space-between;
  }
  .user-name-title {
    margin-top: 5px;
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
      padding: 1dvw 3dvw;
    }
  }
  @media screen and (max-width: 400px) {
    .review-container {
      width: clamp(50px, 70%, 800px);
    }
  }
</style>