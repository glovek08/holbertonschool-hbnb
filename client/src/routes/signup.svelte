<script>
  import { onMount } from "svelte";
  let name = "";
  let email = "";
  let password = "";
  let error = "";
  let success = "";
  console.log("SIGNPOOASD!");
  onMount(() => {
    console.log("SIGNPOOASD!");
  });

  async function handleSignup(event) {
    event.preventDefault();
    error = "";
    success = "";
    // TODO: Replace with your backend endpoint
    try {
      const response = await fetch("/api/v1/auth/signup", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ name, email, password }),
      });
      if (response.ok) {
        success = "Account created! You can now log in.";
        name = email = password = "";
      } else {
        const data = await response.json();
        error = data.error || "Signup failed.";
      }
    } catch (error) {
      error = "Network error.";
    }
  }
</script>

<div class="signup-container">
  <h2>Sign Up</h2>
  <form on:submit={handleSignup}>
    <input type="text" placeholder="Name" bind:value={name} required />
    <input type="email" placeholder="Email" bind:value={email} required />
    <input
      type="password"
      placeholder="Password"
      bind:value={password}
      required
    />
    <button type="submit">Create Account</button>
    {#if error}
      <div class="error">{error}</div>
    {/if}
    {#if success}
      <div class="success">{success}</div>
    {/if}
  </form>
</div>

<style>
  .signup-container {
    max-width: 350px;
    margin: 60px auto;
    padding: 2em;
    background: #fff;
    border-radius: 8px;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
    display: flex;
    flex-direction: column;
    align-items: center;
  }
  .signup-container h2 {
    margin-bottom: 1em;
  }
  .signup-container form {
    display: flex;
    flex-direction: column;
    gap: 1em;
    width: 100%;
  }
  .signup-container input {
    padding: 0.7em;
    border: 1px solid #ccc;
    border-radius: 4px;
    font-size: 1em;
  }
  .signup-container button {
    padding: 0.7em;
    background: var(--green, #2ecc40);
    color: #fff;
    border: none;
    border-radius: 4px;
    font-size: 1em;
    cursor: pointer;
  }
  .signup-container .error {
    color: var(--red, #e74c3c);
    font-weight: bold;
  }
  .signup-container .success {
    color: var(--green, #2ecc40);
    font-weight: bold;
  }
</style>
