<script>
  export const place_id = "";
  export let title = "No Title";
  export let description = "No Description";
  export let price = "$00.00";
  export let image = "/template-bnb.jpg"; // If place provides image, this will get overwritten.
</script>

<a href="/places">
  <div
    class="card-container"
    style="background-image: url('{image}'); background-size: cover; background-position: center;"
  >
    <div class="place-card-data-container">
      <h3 class="place-title">{title}</h3>
      <p class="place-description">{description}</p>
      <p class="place-price">{price}</p>
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
    min-height: 400px;
    width: 300px;
    margin: 30px;
    display: flex;
    flex-direction: column;
    justify-content: flex-end;
    position: relative;
    z-index: 1;
    transition: transform 300ms ease-in-out, z-index 0ms ease-in-out;
  }
  .card-container:hover {
    z-index: 10;
    transform: scale(1.1);
    .place-card-data-container {
      background: white;
    }
  }
  .place-card-data-container {
    background: rgba(255, 255, 255, 0.651);
    margin-bottom: 0;
    margin-top: auto;
    transition: background 200ms ease-in-out;
    padding: 2px 20px 12px 20px;
    position: relative;
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
