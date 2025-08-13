<script>
  import RatingBox from "./RatingBox.svelte";
  import Button_2 from "./Button-2.svelte";

  export let place = {};

  async function removePlace() {
    console.log("Will remove this place");
  }

  $: ({
    id: place_id = "",
    title = "No Title",
    description = "No Description",
    price = "00.00",
    rating = 0,
  } = place);
</script>

<div class="place-card-small-container">
  <a
    href={`/places/${place_id}`}
    class="place-small-anchor"
    aria-label="View {title} details"
  >
    <div class="card-header">
      <h3 class="place-small-title">{title}</h3>
      <RatingBox {rating} />
    </div>
    <div class="card-body">
      <p class="place-small-description">{description}</p>
      <span class="place-small-price">${price}</span>
    </div>
  </a>
  <div class="actions">
    <Button_2 text="Remove" title="Remove Place" btnType="remove" on:click={removePlace} />
  </div>
</div>

<style>
  .place-card-small-container {
    width: 97%;
    border: 1px solid var(--user-dashboard-card-bg);
    display: flex;
    align-items: center;
    justify-content: space-evenly;
    padding: 1.2dvw;
    border-radius: 10px;
  }
  .place-small-anchor {
    background: var(--user-dashboard-card-bg);
    box-shadow: 5px 5px 9px var(--user-dashboard-card-shadow);
    background-color: var(--gray);
    display: flex;
    align-items: flex-start;
    justify-content: center;
    flex-direction: column;
    min-height: 120px;
    border-radius: 20px;
    width: clamp(300px, 70%, 800px);
    padding: 20px 30px;
  }
  .card-header {
    /* outline: 1px solid red;*/
    width: 100%;
    display: flex;
    align-items: center;
    justify-content: space-between;
  }
  .place-small-title {
    margin: 5px;
  }
  @media screen and (max-width: 800px) {
    .place-small-anchor {
      font-size: 1.5dvw;
      padding: 5px 3dvw;
    }
  }
  @media screen and (max-width: 400px) {
    .place-small-anchor {
      width: clamp(50px, 70%, 800px);
      min-height: fit-content;
      padding-bottom: 2dvw;
      padding-top: 1dvw;
      border-radius: 2dvw;
    }
  }
</style>
