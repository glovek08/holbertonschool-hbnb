import { writable } from "svelte/store";

export const isAuthenticated = writable(false);
export const isAdmin = writable(false);
export const currentUserId = writable(null);
export const userName = writable("n/a");

export async function login(email, password, stay_logged) {
  try {
    const response = await fetch("/api/v1/auth/login", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ email, password, stay_logged }),
      credentials: "include",
    });

    const data = await response.json();

    if (response.ok) {
      const user_response = await fetch(`/api/v1/users/${data.id}`, {
        method: "GET",
        credentials: "include",
      });

      if (user_response.ok) {
        const user_data = await user_response.json();
        setAuth(user_data, user_data.is_admin === true);
        return { success: true, msg: "Login successful" };
      } else {
        clearAuth();
        return { success: false, error: "Failed to fetch user details" };
      }
    } else {
      clearAuth();
      return { success: false, error: data.error };
    }
  } catch (error) {
    clearAuth();
    return { success: false, error: "Something bad happened." };
  }
}

export async function logout() {
  try {
    const requestLogout = await fetch("/api/v1/auth/logout", {
      method: "POST",
      credentials: "include",
    });

    if (requestLogout.ok) {
      clearAuth();
      return { success: true, msg: "Log Out Successful CYA!" };
    } else {
      clearAuth();
      return { success: false, error: "Couldn't Log Out" };
    }
  } catch (error) {
    clearAuth();
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
      const user_response = await fetch(`/api/v1/users/${data.user.id}`, {
        method: "GET",
        credentials: "include",
      });

      if (user_response.ok) {
        const user_data = await user_response.json();
        setAuth(user_data, user_data.is_admin === true);
        return {
          success: true,
          msg: "User is authenticated and user data fetched",
        };
      } else {
        clearAuth();
        return { success: false, error: "Failed to fetch user details" };
      }
    } else {
      clearAuth();
      return { success: false, error: "User is not authenticated" };
    }
  } catch (error) {
    clearAuth();
    return { error: `Error in checking authentication: ${error}` };
  }
}


function setAuth(user, admin = false) {
  isAuthenticated.set(true);
  isAdmin.set(admin);
  currentUserId.set(user?.id ?? null);
  userName.set(user?.first_name ?? "n/a");
}

function clearAuth() {
  isAuthenticated.set(false);
  isAdmin.set(false);
  currentUserId.set(null);
  userName.set("n/a");
}

// Will move authentification, trust me bro
