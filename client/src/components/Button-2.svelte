<!-- 
  Functional utility button.
  Icons vary by btnType: "refresh" | "add"
-->

<script>
  export let text = "Replace This Text"; // Visible text label shown to the right of the icon.
  export let title = "Title not set"; // Accessible title/tooltip for the button, Also used as aria-label.
  export let btnType = "refresh"; //Determines which icon is rendered:
  export let disabled = false; // disables interaction when true.
</script>

<button class="button-2" {title} aria-label={title} {disabled} on:click>
  {#if btnType === "refresh"}
    <svg
      xmlns="http://www.w3.org/2000/svg"
      width="20"
      viewBox="0 0 20 20"
      height="20"
      fill="none"
      class="icon svg-icon-refresh"
    >
      <g
        stroke-width="1.5"
        stroke-linecap="round"
        stroke="var(--font-secondary)"
      >
        <path
          d="m3.33337 10.8333c0 3.6819 2.98477 6.6667 6.66663 6.6667 3.682 0 6.6667-2.9848 6.6667-6.6667 0-3.68188-2.9847-6.66664-6.6667-6.66664-1.29938 0-2.51191.37174-3.5371 1.01468"
        />
        <path
          d="m7.69867 1.58163-1.44987 3.28435c-.18587.42104.00478.91303.42582 1.0989l3.28438 1.44986"
        />
      </g>
    </svg>
  {:else if btnType === "add"}
    <i class="fa-solid fa-plus icon svg-icon-add" aria-hidden="true"></i>
  {:else if btnType === "remove"}
    <i class="fa-solid fa-trash icon svg-icon-remove" aria-hidden="true"></i>
  {/if}
  <span class="label">{text}</span>
</button>

<style>
  .button-2 {
    display: flex;
    justify-content: center;
    align-items: center;
    padding: 6px 12px;
    gap: 8px;
    height: 34px;
    width: max-content;
    border: none;
    background: var(--background-secondary);
    color: var(--font-secondary);
    border-radius: 20px;
    cursor: pointer;
    transition:
      background 0.25s,
      color 0.2s ease-in-out;
  }
  .button-2:disabled {
    opacity: 0.6;
    cursor: not-allowed;
  }
  .icon {
    display: inline-flex;
  }
  .label {
    line-height: 20px;
    font-size: 15px;
    letter-spacing: 0.5px;
    white-space: nowrap;
  }
  .button-2:hover:not(:disabled) {
    background: var(--accent);
    .svg-icon-remove {
      color: var(--red);
    }
  }
  .button-2:hover:not(:disabled) .svg-icon-refresh {
    animation: spin 2s linear infinite;
  }
  .svg-icon-add {
    font-size: 1.2rem;
  }
  @keyframes spin {
    to {
      transform: rotate(-360deg);
    }
  }
  @media screen and (max-width: 800px) {
    .button-2 {
      padding: 5px 8px;
      font-size: 14px;
      gap: 6px;
      height: 30px;
    }
    .label {
      font-size: 13px;
    }
    .icon,
    .svg-icon-add,
    .svg-icon-remove,
    .svg-icon-refresh {
      width: 18px;
      height: 18px;
      font-size: 1rem;
    }
  }
  @media screen and (max-width: 400px) {
    .button-2 {
      width: fit-content;
      min-width: 0;
      padding: 4px 6px;
      font-size: 13px;
      gap: 4px;
      height: 28px;
    }
    .label {
      font-size: 12px;
      display: none;
    }
    .icon,
    .svg-icon-add,
    .svg-icon-remove,
    .svg-icon-refresh {
      width: 16px;
      height: 16px;
      font-size: 0.9rem;
      position: relative;
      left: 1.6px;
      top: .3px;
    }
  }
</style>
