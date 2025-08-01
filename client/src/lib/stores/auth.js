import { writable } from "svelte/store";

export const isAuthenticated = writable(false);

export async function login(email, password, stay_logged) {
  try {
    console.log(`Login in with: ${email}, ${password}, ${stay_logged}`);
    const response = await fetch("/api/v1/auth/login", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ email, password, stay_logged }),
      credentials: "include",
    });
    console.log(`Sending response: ${response}`);
    const data = await response.json();
    if (response.ok) {
      isAuthenticated.set(true);
      return { success: true, msg: "Login successful" };
    } else {
      isAuthenticated.set(false);
      return { success: false, error: data.error };
    }
  } catch (error) {
    return { success: false, error: "Something happened." };
  }
}

export async function logout() {
  // call logout endpoint, on success clear svelte thing
  try {
    const requestLogout = await fetch("/api/v1/auth/logout", {
      method: "POST",
    });
    if (requestLogout.ok) {
      isAuthenticated.set(false);
      return { success: true, msg: "Log Out Successful CYA!" };
    } else {
      isAuthenticated.set(false);
      return { success: false, error: "Couldn't Log Out" };
    }
  } catch (error) {
    return { error: `Error in fetching session logout: ${error}` };
  }
}

export async function checkAuth() {
  try {
    const response = await fetch("/api/v1/auth/check_status", {
      method: "POST",
      credentials: "include",
    });
    if (response.ok) {
      isAuthenticated.set(true);
      return { success: true, msg: "User is authenticated" };
    } else {
      return {success: false, error: "User is not authenticated"};
    }
  }
  catch (error) {
    return { error: `Error in checking authentication: ${error}`};
  }
}


// Will move authentification, trust me bro
