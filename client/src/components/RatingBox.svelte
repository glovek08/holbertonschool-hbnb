<script>
  export let rating = 0;
</script>

<div class="rating-container">
  {#each Array(5) as _, index}
    <i
      class="star {index < rating ? 'fa-solid fa-star' : 'fa-regular fa-star'}"
      style="color: {index < rating ? 'var(--star-fill)' : 'var(--star-empty)'}"
    ></i>
  {/each}
</div>

<style>
  :root {
    --star-fill: red;
    --star-empty: rgb(158, 161, 158);
  }
  :root.light {
    --star-fill: red;
    --star-empty: rgb(110, 104, 104);
  }

  .rating-container {
    display: flex;
    justify-content: center;
    align-items: center;
  }

  .star {
    font-size: 1rem;
    margin-right: 5px;
    transition: color 0.2s ease-in-out;
  }
    @media screen and (max-width: 800px) {
      .star {
        font-size: 1dvw;
      }
    }
</style>
