<!-- 
  This is a functional button, uses: functions xD
  As a function button, it shouldn't shine so it doesn't messes with the site flow.
  BY: andrew-demchenk0.
-->

<script>
  export let text = "Replace This Text";
  export let title = "Title not set";
</script>
<button class="button-2" title={title} on:click>
  <svg
    xmlns="http://www.w3.org/2000/svg"
    width="20"
    viewBox="0 0 20 20"
    height="20"
    fill="none"
    class="svg-icon"
  >
    <g stroke-width="1.5" stroke-linecap="round" stroke="var(--font-secondary)">
      <path
        d="m3.33337 10.8333c0 3.6819 2.98477 6.6667 6.66663 6.6667 3.682 0 6.6667-2.9848 6.6667-6.6667 0-3.68188-2.9847-6.66664-6.6667-6.66664-1.29938 0-2.51191.37174-3.5371 1.01468"
      ></path>
      <path
        d="m7.69867 1.58163-1.44987 3.28435c-.18587.42104.00478.91303.42582 1.0989l3.28438 1.44986"
      ></path>
    </g>
  </svg>
  <span class="lable">{text}</span>
</button>

<style>
  .button-2 {
    display: flex;
    justify-content: center;
    align-items: center;
    padding: 6px 12px;
    gap: 8px;
    height: 34px;
    width: 112px;
    border: none;
    background: var(--background-secondary);
    border-radius: 20px;
    cursor: pointer;
  }

  .lable {
    line-height: 20px;
    font-size: 17px;
    color: var(--font-secondary);
    letter-spacing: 1px;
  }

  .button-2:hover {
    background: var(--accent);
  }

  .button-2:hover .svg-icon {
    animation: spin 2s linear infinite;
  }

  @keyframes spin {
    0% {
      transform: rotate(0deg);
    }

    100% {
      transform: rotate(-360deg);
    }
  }
</style>
