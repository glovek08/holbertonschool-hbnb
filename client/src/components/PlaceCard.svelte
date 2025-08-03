<script>
  import RatingBox from "./RatingBox.svelte";

  export const place_id = "";
  export let title = "No Title";
  export let description = "No Description";
  export let price = "00.00";
  export let image = "/template-bnb.jpg";
  export let rating = 0; // If place provides image, this will get overwritten.
</script>

<a href="/places">
  <div
    class="card-container"
    style="background-image: url('{image}'); background-size: cover; background-position: center;"
  >
    <div class="place-card-data-container">
      <div class="place-card-infobox">
        <RatingBox {rating} />
        <p class="place-price">
          $ <span class="price-span">{price}</span> per Day.
        </p>
      </div>
      <h3 class="place-title">{title}</h3>
      <p class="place-description">{description}</p>
    </div>
  </div>
</a>

<style>
  .card-container {
    /* outline: 1px solid green; */
    padding: 0;
    background: var(--white);
    color: rgb(27, 26, 26);
    transition: 300ms ease-in-out;
    width: 300px;
    height: 450px;
    margin: 30px;
    display: flex;
    flex-direction: column;
    justify-content: flex-end;
    position: relative;
    z-index: 1;
    transition:
      transform 300ms ease-in-out,
      z-index 0ms ease-in-out;
  }
  .card-container:hover {
    z-index: 10;
    transform: scale(1.1);
    .place-card-data-container {
      background: rgba(255, 255, 255, 0.62);
    }
  }
  .place-card-data-container {
    /* outline: 1px solid yellow; */
    background: rgba(255, 255, 255, 0.3);
    height: 50%;
    overflow-y: auto;
    margin-bottom: 0;
    margin-top: auto;
    transition: background 200ms ease-in-out;
    padding: 2px 20px 12px 20px;
    position: relative;
    backdrop-filter: blur(6px);
    -webkit-backdrop-filter: blur(6px);
    text-shadow: 0 0 10px rgb(165, 163, 163);
    scrollbar-width: thin; /* Makes the scrollbar thinner */
    scrollbar-color: rgb(43, 49, 59) transparent;
    display: flex;
    align-items: center;
    justify-content: flex-start;
    flex-direction: column;
  }
  .place-card-infobox {
    /* outline: 1px solid green; */
    width: 100%;
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 0;
  }
  .place-price {
    /* outline: 1px solid red; */
    text-align: right;
  }
  .place-title {
    font-weight: bolder;
    font-size: 1.3rem;
    padding: 0;
    margin-top: 0;
    margin-bottom: 5px;
  }
  .place-title,
  .place-description {
    width: 100%;
  }
  .price-span {
    font-size: 1.5rem;
  }
  .place-card-data-container::-webkit-scrollbar {
    width: 6px;
  }

  .place-card-data-container::-webkit-scrollbar-thumb {
    background: rgba(0, 0, 0, 0.5);
    border-radius: 10px;
  }

  .place-card-data-container::-webkit-scrollbar-thumb:hover {
    background: rgba(0, 0, 0, 0.7);
  }

  .place-card-data-container::-webkit-scrollbar-track {
    background: transparent;
  }

  /* .card-container:hover .place-card-image {
    filter: saturate(1);
  }
  .card-container:hover .image-container::before {
    box-shadow: none;
  }
  .image-container {
    display: flex;
    justify-content: center;
    align-items: center;
    position: relative;
    overflow: hidden;
  }

  .image-container::before {
    content: "";
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    /* box-shadow: inset 0 5px 23px rgba(0, 0, 0, 0.747); */
  /* pointer-events: none;
    z-index: 1;
    transition: box-shadow 300ms ease-in-out;
  } */
  /* .place-card-image {
    filter: saturate(0);
    transition: filter 300ms ease-in-out;
  } */
</style>
