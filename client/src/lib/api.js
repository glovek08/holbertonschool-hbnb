const API_BASE_URL = "http://localhost:5000/api/v1";

class ApiService {
  constructor() {
    this.baseURL = API_BASE_URL;
  }

  async request(endpoint, options = {}) {
    const url = `${this.baseURL}${endpoint}`;
    const config = {
      headers: {
        "Content-Type": "application/json",
        ...options.headers,
      },
      ...options,
    };

    try {
      const response = await fetch(url, config);

      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }

      return await response.json();
    } catch (error) {
      console.error("API request failed:", error);
      throw error;
    }
  }

  // ******** USERS KINGDOM ********
  async getUsers() {
    return this.request("/users/");
  }

  async createUser(userData) {
    return this.request("/users/", {
      method: "POST",
      body: JSON.stringify(userData),
    });
  }

  async getUser(userId) {
    return this.request(`/users/${userId}/`);
  }

  // ******** PLACES KINGDOM ********
  async getPlaces() {
    return this.request("/places/", {
      method: "GET",
      credentials: "include",
    });
  }

  async createPlace(placeData) {
    return this.request("/places/", {
      method: "POST",
      body: JSON.stringify(placeData),
    });
  }

  async getPlace(placeId) {
    return this.request(`/places/${placeId}/`);
  }

  // ******** AMENITIES KINGDOM ********
  async getAmenities() {
    return this.request("/amenities/");
  }

  async createAmenity(amenityData) {
    return this.request("/amenities/", {
      method: "POST",
      body: JSON.stringify(amenityData),
    });
  }

  // ******** REVIEWS KINGDOM ********
  async getReviews() {
    return this.request("/reviews/");
  }

  async createReview(reviewData) {
    return this.request("/reviews/", {
      method: "POST",
      body: JSON.stringify(reviewData),
    });
  }

  async getPlaceReviews(placeId) {
    return this.request(`/reviews/places/${placeId}/reviews/`);
  }

  // ******** AUTHENTICATION KINGDOM ********
  // Using auth.js instead!!!

  // async login(credentials) {
  //   return this.request('/auth/login/', {
  //     method: 'POST',
  //     body: JSON.stringify(credentials),
  //   });
  // }
}

export default new ApiService();