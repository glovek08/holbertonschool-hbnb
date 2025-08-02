<!-- 
  This is a redirection button, uses: navigation, deployment, engagement.
  AKA Important button, keep it shiny. It's important the user sees it.
-->


<script>
  export let text = "Replace This Text";
  export const type = "";

</script>

<button class="button-1" on:click>{text}</button>

<style>
  .button-1 {
    z-index: 2;
    margin: 10px;
    padding: 15px 30px;
    text-align: center;
    text-transform: uppercase;
    transition: 0.5s;
    background-size: 200% auto;
    color: white;
    border-radius: 10px;
    display: block;
    border: 0px;
    font-weight: 700;
    box-shadow: 0px 0px 14px -7px var(--accent);
    background-image: linear-gradient(
      45deg,
      var(--accent) 0%,
      #d6135e 51%,
      #ff512f 100%
    );
    cursor: pointer;
    user-select: none;
    -webkit-user-select: none;
    touch-action: manipulation;
  }

  .button-1:hover {
    background-position: right center;
    /* change the direction of the change here */
    color: #fff;
    text-decoration: none;
  }

  .button-1:active {
    transform: scale(0.95);
  }
</style>