<script>
  export let message = "Loading...";
</script>

<div class="loading-screen">
  <div class="spinner"></div>
  <p>{message}</p>
</div>

<style>
  .loading-screen {
    position: fixed;
    inset: 0;
    background-color: var(--background-primary);
    color: var(--font-primary, #fff);
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    z-index: 9999;
  }

  .spinner {
    width: 50px;
    height: 50px;
    border: 5px solid rgba(255, 255, 255, 0.3);
    border-top: 5px solid var(--primary-color, #fff);
    border-radius: 50%;
    animation: spin 1s linear infinite;
  }

  @keyframes spin {
    from {
      transform: rotate(0deg);
    }
    to {
      transform: rotate(360deg);
    }
  }
</style>
