<script>
  import { onMount } from 'svelte';
  import apiService from './api.js';

  let users = [];
  let places = [];
  let amenities = [];
  let loading = false;
  let error = null;

  async function loadData() {
    loading = true;
    error = null;
    
    try {
      // Test multiple endpoints
      const [usersData, placesData, amenitiesData] = await Promise.all([
        apiService.getUsers(),
        apiService.getPlaces(),
        apiService.getAmenities()
      ]);
      
      users = usersData;
      places = placesData;
      amenities = amenitiesData;
      
      console.log('API Data loaded:', { users, places, amenities });
    } catch (err) {
      error = err.message;
      console.error('Failed to load data:', err);
    } finally {
      loading = false;
    }
  }

  onMount(() => {
    loadData();
  });
</script>

<div class="api-test">
  <h2>🔌 API Connection Test</h2>
  
  <button on:click={loadData} disabled={loading}>
    {loading ? 'Loading...' : 'Refresh Data'}
  </button>

  {#if error}
    <div class="error">
      ❌ Error: {error}
    </div>
  {/if}

  {#if loading}
    <div class="loading">⏳ Loading data from Flask API...</div>
  {/if}

  {#if !loading && !error}
    <div class="results">
      <div class="section">
        <h3>👥 Users ({users.length})</h3>
        {#if users.length > 0}
          <ul>
            {#each users.slice(0, 3) as user}
              <li>{user.first_name} {user.last_name} ({user.email})</li>
            {/each}
          </ul>
        {:else}
          <p>No users found</p>
        {/if}
      </div>

      <div class="section">
        <h3>🏠 Places ({places.length})</h3>
        {#if places.length > 0}
          <ul>
            {#each places.slice(0, 3) as place}
              <li>{place.title} - ${place.price}/night</li>
            {/each}
          </ul>
        {:else}
          <p>No places found</p>
        {/if}
      </div>

      <div class="section">
        <h3>✨ Amenities ({amenities.length})</h3>
        {#if amenities.length > 0}
          <ul>
            {#each amenities.slice(0, 3) as amenity}
              <li>{amenity.name}</li>
            {/each}
          </ul>
        {:else}
          <p>No amenities found</p>
        {/if}
      </div>
    </div>
  {/if}
</div>

<style>
  .api-test {
    margin: 20px 0;
    padding: 20px;
    border: 2px solid #ccc;
    border-radius: 8px;
    background: #f9f9f9;
  }

  .error {
    color: red;
    background: #ffe6e6;
    padding: 10px;
    border-radius: 4px;
    margin: 10px 0;
  }

  .loading {
    color: #666;
    font-style: italic;
    padding: 10px 0;
  }

  .results {
    margin-top: 20px;
  }

  .section {
    margin: 15px 0;
    padding: 10px;
    background: white;
    border-radius: 4px;
  }

  ul {
    margin: 5px 0;
    padding-left: 20px;
  }

  li {
    margin: 5px 0;
  }

  button {
    background: #4CAF50;
    color: white;
    border: none;
    padding: 10px 20px;
    border-radius: 4px;
    cursor: pointer;
  }

  button:disabled {
    background: #ccc;
    cursor: not-allowed;
  }
</style>
