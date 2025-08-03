import { writable } from "svelte/store";

export const isAuthenticated = writable(false);
export const isAdmin = writable(false);

export async function login(email, password, stay_logged) {
  try {
    console.log(`Logging in with: ${email}, ${password}, ${stay_logged}`);
    const response = await fetch("/api/v1/auth/login", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ email, password, stay_logged }),
      credentials: "include",
    });

    const data = await response.json();

    if (response.ok) {
      isAuthenticated.set(true);

      // check if the user is an admin
      const user_response = await fetch(`/api/v1/users/${data.id}`, {
        method: "GET",
        credentials: "include",
      });

      if (user_response.ok) {
        const user_data = await user_response.json();
        if (user_data.is_admin === true) {
          console.log("User is an admin");
          isAdmin.set(true);
        } else {
          console.log("User is not an admin");
          isAdmin.set(false);
        }
      } else {
        console.error("Failed to fetch user details");
        isAdmin.set(false);
      }

      return { success: true, msg: "Login successful" };
    } else {
      isAuthenticated.set(false);
      isAdmin.set(false);
      return { success: false, error: data.error };
    }
  } catch (error) {
    isAuthenticated.set(false);
    isAdmin.set(false);
    return { success: false, error: "Something bad happened." };
  }
}

export async function logout() {
  // on success clear svelte thing.
  try {
    const requestLogout = await fetch("/api/v1/auth/logout", {
      method: "POST",
      credentials: "include",
    });

    if (requestLogout.ok) {
      isAuthenticated.set(false);
      isAdmin.set(false);
      return { success: true, msg: "Log Out Successful CYA!" };
    } else {
      isAuthenticated.set(false);
      isAdmin.set(false);
      return { success: false, error: "Couldn't Log Out" };
    }
  } catch (error) {
    isAuthenticated.set(false);
    isAdmin.set(false);
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
      const data = await response.json();
      isAuthenticated.set(true);

      const user_response = await fetch(`/api/v1/users/${data.user.id}`, {
        method: "GET",
        credentials: "include",
      });

      if (user_response.ok) {
        const user_data = await user_response.json();
        console.log(user_data)
        if (user_data.is_admin === true) {
          console.log("IS ADMIN");
          isAdmin.set(true);
        } else {
          console.log("NOT ADMIN");
          isAdmin.set(false);
        }
        return {
          success: true,
          msg: "User is authenticated and user data fetched",
        };
      } else {
        console.error("Failed to fetch user details");
        isAdmin.set(false);
        return { success: false, error: "Failed to fetch user details" };
      }
    } else {
      isAuthenticated.set(false);
      isAdmin.set(false);
      return { success: false, error: "User is not authenticated" };
    }
  } catch (error) {
    isAuthenticated.set(false);
    isAdmin.set(false);
    console.error(`Error in checking authentication: ${error}`);
    return { error: `Error in checking authentication: ${error}` };
  }
}

// Will move authentification, trust me bro
