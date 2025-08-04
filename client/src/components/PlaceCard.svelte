<script>
  import RatingBox from "./RatingBox.svelte";

  export let place_id = "";
  export let title = "No Title";
  export let description = "No Description";
  export let price = "00.00";
  export let image = "/template-bnb.jpg";
  export let rating = 0; // If place provides image, this will get overwritten.
</script>

<a href={`/places/${place_id}`}>
  <button
    class="place-btn"
    style="background-image: url('{image}'); background-size: cover; background-position: center;"
  >
    <div class="place-card-data-container">
      <div class="place-card-infobox">
        <RatingBox {rating} />
        <p class="place-price">
          $ <span class="price-span">{price}</span> per Day.
        </p>
      </div>
      <h3 class="place-title" {title}>{title}</h3>
      <p class="place-description" title={description}>{description}</p>
    </div>
  </button>
</a>

<style>
  :root {
    --card-desc-background: rgba(33, 36, 36, 0.752);
    --card-font-color: rgb(228, 218, 218);
    --card-text-shadow: black;
    --card-hover-background: rgba(63, 61, 60, 0.694);
  }
  :root.light {
    --card-desc-background: rgba(199, 206, 206, 0.39);
    --card-font-color: rgb(0, 0, 0);
    --card-text-shadow: rgb(193, 181, 181);
    --card-hover-background: rgba(232, 224, 224, 0.916);
  }
  .place-btn {
    /* outline: 1px solid green; */
    font-family: 'Quicksand';
    padding: 0;
    background: var(--white);
    color: var(--card-font-color);
    transition: 300ms ease-in-out;
    border: none;
    cursor: pointer;
    width: 300px;
    height: 450px;
    display: flex;
    flex-direction: column;
    justify-content: flex-end;
    position: relative;
    z-index: 1;
    transition:
      transform 300ms ease-in-out,
      z-index 0ms ease-in-out;
  }
  .place-btn:hover {
    z-index: 10;
    transform: scale(1.02);
    .place-card-data-container {
      background: var(--card-hover-background);
    }
  }
  .place-card-data-container {
    /* outline: 1px solid yellow; */
    background: var(--card-desc-background);
    height: 40%;
    overflow-y: auto;
    margin-bottom: 0;
    margin-top: auto;
    transition: background 200ms ease-in-out;
    padding: 2px 20px 12px 20px;
    position: relative;
    outline: 2px solid var(--card-desc-background);
    backdrop-filter: blur(6px);
    -webkit-backdrop-filter: blur(6px);
    text-shadow: 0 0 10px var(--card-text-shadow);
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
    width: 100%;
    height: 1.5em; /* Set a fixed height (adjust based on font size) */
    line-height: 1.5em; /* Match the height to ensure proper alignment */
    white-space: nowrap; /* Prevent wrapping */
    overflow: hidden; /* Hide overflowing text */
    text-overflow: ellipsis;
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
