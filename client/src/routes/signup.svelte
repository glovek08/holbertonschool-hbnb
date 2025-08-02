<script>
  import { onMount } from "svelte";
  import Button_1 from "../components/Button-1.svelte";

  let firstName = "";
  let lastName = "";
  let email = "";
  let password = "";
  let error = "";
  let success = "";
  console.log("Checking mount signup...");
  onMount(() => {
    console.log("Mounted");
  });

  async function handleSignup(event) {
    event.preventDefault();
    error = "";
    success = "";
    try {
      const response = await fetch("/api/v1/users/", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ first_name: firstName, last_name: lastName, email, password }),
      });
      if (response.ok) {
        success = "Account created! You can now log in.";
        firstName = lastName = email = password = "";
      } else {
        const data = await response.json();
        error = data.error || "Signup failed.";
        console.warn(error);
      }
    } catch (error) {
      error = "Network error.";
    }
  }
</script>

<div class="signup-container">
  <h2>Sign Up</h2>
  <form on:submit={handleSignup}>
    <input type="text" placeholder="First Name" bind:value={firstName} maxlength="50" aria-label="First Name" aria-required="true" required/>
    <input type="text" placeholder="Last Name" bind:value={lastName} maxlength="50" aria-label="Last Name" aria-required="true" required/>
    <input type="email" placeholder="Email" bind:value={email} maxlength="254" aria-required="true" required />
    <input
      type="password"
      placeholder="Password"
      bind:value={password}
      maxlength="60"
      aria-required="true"
      required
    />
    <Button_1 text="Sign Up" type="submit"></Button_1>
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
    /* outline: 1px solid green; */
    color: var(--font-primary);
    background-color: var(--gray);
    width: clamp(260px, 35vw, 420px);
    padding: 2rem 1.5rem;
    border-radius: 12px;
    display: flex;
    align-items: center;
    justify-content: center;
    flex-direction: column;
    box-shadow: 10px 10px 20px var(--shadow-primary);
  }
  .signup-container h2 {
    margin-bottom: 2.6rem;
  }
  .signup-container form {
    /* border: 1px solid rgb(139, 135, 135); */
    border-radius: 10px;
    display: flex;
    align-items: center;
    flex-direction: column;
    gap: 30px;
    width: 95%;
    padding: 10px 5px 30px 5px;
    }
  .signup-container input {
    /* outline: 1px solid red; */
    color: rgb(255, 255, 255);
    border: none;
    border-radius: 10px;
    background: rgb(56, 53, 53);
    padding: 10px 15px;
  }
  .signup-container form input:last-of-type {
    margin-bottom: 20px;
  }
  .signup-container input::placeholder {
    color: rgb(228, 221, 221);
  }
  .signup-container .error {
    color: var(--red);
    font-weight: bold;
  }
  .signup-container .success {
    color: var(--green);
    font-weight: bold;
  }
</style>
