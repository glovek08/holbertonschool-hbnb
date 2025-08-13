import { writable } from "svelte/store";

export const isAuthenticated = writable(false); // true after successful login/checkAuth, reset to false on logout or failures.
export const isAdmin = writable(false); // whether current user has admin privileges.
export const currentUserId = writable(null); //UUID (string) of the currently authenticated user.
export const userName = writable("n/a"); //First name (display name) of the authenticated user.
/**
 * Attempt to authenticate with credentials.
 * On success: fetch full user resource and populate auth stores.
 *
 * @param {string} email
 * @param {string} password
 * @param {boolean} stay_logged - if true session last 30 days.
 * @returns {Promise<{success: boolean, msg?: string, error?: string}>}
 */
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
/**
 * Terminate current session (server + local stores).
 *
 * @returns {Promise<{success?: boolean, msg?: string, error?: string}>}
 */
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
/**
 * Validates current access_token in cookies.
 * Refreshes auth stores if valid; clears them if not.
 *
 * @returns {Promise<{success: boolean, msg?: string, error?: string}>}
 */
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
    return { success: false, error: `Error in checking authentication: ${error}` };
  }
}

/**
 * Internal helper: populate auth-related stores.
 *
 * @param {Object} user - User object returned by API.
 * @param {boolean} [admin=false] - Whether user has admin privileges.
 */
function setAuth(user, admin = false) {
  console.log("setAuth called with user:", user);
  isAuthenticated.set(true);
  isAdmin.set(admin);
  currentUserId.set(user?.id || null);
  userName.set(user?.first_name || "n/a");
  console.log("Auth state updated:", {
    userId: user?.id,
    userName: user?.first_name,
    isAdmin: admin,
  });
}
/**
 * Internal helper: reset all auth-related stores to unauthenticated state.
 */
function clearAuth() {
  console.log("clearAuth called");
  isAuthenticated.set(false);
  isAdmin.set(false);
  currentUserId.set(null);
  userName.set("n/a");
  console.log("Auth state cleared");
}
