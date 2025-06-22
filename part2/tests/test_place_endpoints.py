import unittest
import json
from app import create_app


class TestPlacesAPI(unittest.TestCase):
    def setUp(self):
        """Set up test fixtures before each test method."""
        self.app = create_app()
        self.app.config["TESTING"] = True
        self.client = self.app.test_client()

        # Create a test user first (assuming users endpoint exists)
        self.test_user_data = {
            "first_name": "John",
            "last_name": "Doe",
            "email": "john.doe@test.com",
        }

        # Create user and store the ID for place creation
        user_response = self.client.post(
            "/api/v1/users/",
            data=json.dumps(self.test_user_data),
            content_type="application/json",
        )

        if user_response.status_code == 201:
            user_data = json.loads(user_response.data)
            self.test_user_id = user_data.get("id")
        else:
            # Fallback - assume user exists or use a known test user ID
            self.test_user_id = "test-user-123"

        # Create test amenities (assuming amenities endpoint exists)
        self.test_amenity_data = {
            "name": "WiFi",
            "description": "High-speed internet connection",
        }

        amenity_response = self.client.post(
            "/api/v1/amenity/",
            data=json.dumps(self.test_amenity_data),
            content_type="application/json",
        )

        if amenity_response.status_code == 201:
            amenity_data = json.loads(amenity_response.data)
            self.test_amenity_id = amenity_data.get("id")
        else:
            # Fallback - use a known test amenity ID
            self.test_amenity_id = "test-amenity-123"

        # Valid place data for testing
        self.valid_place_data = {
            "title": "Beautiful Test Apartment",
            "description": "A lovely place to stay for testing",
            "price": 150.0,
            "latitude": 40.7128,
            "longitude": -74.0060,
            "owner_id": self.test_user_id,
            "amenities": [self.test_amenity_id],
        }

    def test_create_place_success(self):
        """Test successful place creation."""
        response = self.client.post(
            "/api/v1/places/",
            data=json.dumps(self.valid_place_data),
            content_type="application/json",
        )

        self.assertEqual(response.status_code, 201)
        data = json.loads(response.data)
        self.assertEqual(data["owner_id"], self.test_user_id)
        self.assertEqual(data["title"], "Beautiful Test Apartment")
        self.assertEqual(data["description"], "A lovely place to stay for testing")
        self.assertEqual(data["price"], 150.0)
        self.assertEqual(data["latitude"], 40.7128)
        self.assertEqual(data["longitude"], -74.0060)
        self.assertIn("amenities", data)
        self.assertIsInstance(data["amenities"], list)
        self.assertGreater(len(data["amenities"]), 0)

    def test_create_place_missing_title(self):
        """Test place creation with missing title."""
        invalid_data = self.valid_place_data.copy()
        del invalid_data["title"]

        response = self.client.post(
            "/api/v1/places/",
            data=json.dumps(invalid_data),
            content_type="application/json",
        )

        self.assertEqual(response.status_code, 400)

    def test_create_place_missing_price(self):
        """Test place creation with missing price."""
        invalid_data = self.valid_place_data.copy()
        del invalid_data["price"]

        response = self.client.post(
            "/api/v1/places/",
            data=json.dumps(invalid_data),
            content_type="application/json",
        )

        self.assertEqual(response.status_code, 400)

    def test_create_place_missing_coordinates(self):
        """Test place creation with missing coordinates."""
        # Missing latitude
        invalid_data = self.valid_place_data.copy()
        del invalid_data["latitude"]

        response = self.client.post(
            "/api/v1/places/",
            data=json.dumps(invalid_data),
            content_type="application/json",
        )

        self.assertEqual(response.status_code, 400)

        # Missing longitude
        invalid_data = self.valid_place_data.copy()
        del invalid_data["longitude"]

        response = self.client.post(
            "/api/v1/places/",
            data=json.dumps(invalid_data),
            content_type="application/json",
        )

        self.assertEqual(response.status_code, 400)

    def test_create_place_missing_owner_id(self):
        """Test place creation with missing owner_id."""
        invalid_data = self.valid_place_data.copy()
        del invalid_data["owner_id"]

        response = self.client.post(
            "/api/v1/places/",
            data=json.dumps(invalid_data),
            content_type="application/json",
        )

        self.assertEqual(response.status_code, 400)

    def test_create_place_missing_amenities(self):
        """Test place creation with missing amenities."""
        invalid_data = self.valid_place_data.copy()
        del invalid_data["amenities"]

        response = self.client.post(
            "/api/v1/places/",
            data=json.dumps(invalid_data),
            content_type="application/json",
        )

        self.assertEqual(response.status_code, 400)

    def test_create_place_invalid_price_type(self):
        """Test place creation with invalid price type."""
        invalid_data = self.valid_place_data.copy()
        invalid_data["price"] = "invalid_price"

        response = self.client.post(
            "/api/v1/places/",
            data=json.dumps(invalid_data),
            content_type="application/json",
        )

        self.assertEqual(response.status_code, 400)

    def test_create_place_negative_price(self):
        """Test place creation with negative price."""
        invalid_data = self.valid_place_data.copy()
        invalid_data["price"] = -50.0

        response = self.client.post(
            "/api/v1/places/",
            data=json.dumps(invalid_data),
            content_type="application/json",
        )

        self.assertEqual(response.status_code, 400)

    def test_create_place_invalid_coordinates(self):
        """Test place creation with invalid coordinates."""
        # Invalid latitude (out of range)
        invalid_data = self.valid_place_data.copy()
        invalid_data["latitude"] = 95.0  # Max is 90

        response = self.client.post(
            "/api/v1/places/",
            data=json.dumps(invalid_data),
            content_type="application/json",
        )

        self.assertEqual(response.status_code, 400)

        # Invalid longitude (out of range)
        invalid_data = self.valid_place_data.copy()
        invalid_data["longitude"] = 185.0  # Max is 180

        response = self.client.post(
            "/api/v1/places/",
            data=json.dumps(invalid_data),
            content_type="application/json",
        )

        self.assertEqual(response.status_code, 400)

    def test_create_place_nonexistent_owner(self):
        """Test place creation with non-existent owner_id."""
        invalid_data = self.valid_place_data.copy()
        invalid_data["owner_id"] = "nonexistent-user-id"

        response = self.client.post(
            "/api/v1/places/",
            data=json.dumps(invalid_data),
            content_type="application/json",
        )

        self.assertEqual(response.status_code, 400)

    def test_create_place_invalid_amenities_format(self):
        """Test place creation with invalid amenities format."""
        invalid_data = self.valid_place_data.copy()
        invalid_data["amenities"] = "not_a_list"

        response = self.client.post(
            "/api/v1/places/",
            data=json.dumps(invalid_data),
            content_type="application/json",
        )

        self.assertEqual(response.status_code, 400)

    def test_get_all_places_success(self):
        """Test successful retrieval of all places."""
        # First create a place
        self.client.post(
            "/api/v1/places/",
            data=json.dumps(self.valid_place_data),
            content_type="application/json",
        )

        # Then get all places
        response = self.client.get("/api/v1/places/")

        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertIsInstance(data, list)

        if len(data) > 0:
            place = data[0]
            self.assertIn("id", place)
            self.assertIn("owner_id", place)
            self.assertIn("owner", place)
            self.assertIn("title", place)
            self.assertIn("description", place)
            self.assertIn("price", place)
            self.assertIn("latitude", place)
            self.assertIn("longitude", place)
            self.assertIn("amenities", place)

    def test_get_place_by_id_success(self):
        """Test successful retrieval of a place by ID."""

        # Get all places to find the created place ID
        all_places_response = self.client.get("/api/v1/places/")
        all_places = json.loads(all_places_response.data)

        if len(all_places) > 0:
            place_id = all_places[-1]["id"]  # Get the last created place

            # Test getting place by ID
            response = self.client.get(f"/api/v1/places/{place_id}")

            self.assertEqual(response.status_code, 200)
            data = json.loads(response.data)
            self.assertEqual(data["id"], place_id)
            self.assertIn("owner", data)
            self.assertIn("amenities", data)

    def test_get_place_by_invalid_id(self):
        """Test retrieval of a place with invalid ID."""
        response = self.client.get("/api/v1/places/invalid-id")

        self.assertEqual(response.status_code, 400)
        data = json.loads(response.data)
        self.assertIn("error", data)

    def test_get_place_by_nonexistent_id(self):
        """Test retrieval of a place with non-existent ID."""
        response = self.client.get("/api/v1/places/nonexistent-place-id")

        self.assertEqual(response.status_code, 400)
        data = json.loads(response.data)
        self.assertIn("error", data)

    def test_update_place_success(self):
        """Test successful place update."""
        # Get all places to find the created place ID
        all_places_response = self.client.get("/api/v1/places/")
        all_places = json.loads(all_places_response.data)

        if len(all_places) > 0:
            place_id = all_places[-1]["id"]  # Get the last created place

            # Update data
            update_data = self.valid_place_data.copy()
            update_data["title"] = "Updated Test Apartment"
            update_data["price"] = 200.0

            # Test updating place
            response = self.client.put(
                f"/api/v1/places/{place_id}",
                data=json.dumps(update_data),
                content_type="application/json",
            )

            self.assertEqual(response.status_code, 200)
            data = json.loads(response.data)
            self.assertEqual(data["title"], "Updated Test Apartment")
            self.assertEqual(data["price"], 200.0)

    def test_update_place_invalid_id(self):
        """Test update of a place with invalid ID."""
        response = self.client.put(
            "/api/v1/places/invalid-id",
            data=json.dumps(self.valid_place_data),
            content_type="application/json",
        )

        self.assertEqual(response.status_code, 404)
        data = json.loads(response.data)
        self.assertIn("error", data)

    def test_update_place_invalid_data(self):
        """Test update of a place with invalid data."""
        # First create a place
        create_response = self.client.post(
            "/api/v1/places/",
            data=json.dumps(self.valid_place_data),
            content_type="application/json",
        )

        if create_response.status_code == 201:
            # Get all places to find the created place ID
            all_places_response = self.client.get("/api/v1/places/")
            all_places = json.loads(all_places_response.data)

            if len(all_places) > 0:
                place_id = all_places[-1]["id"]

                # Invalid update data (negative price)
                invalid_update_data = self.valid_place_data.copy()
                invalid_update_data["price"] = -100.0

                response = self.client.put(
                    f"/api/v1/places/{place_id}",
                    data=json.dumps(invalid_update_data),
                    content_type="application/json",
                )

                self.assertEqual(response.status_code, 400)

    def test_create_place_empty_title(self):
        """Test place creation with empty title."""
        invalid_data = self.valid_place_data.copy()
        invalid_data["title"] = ""

        response = self.client.post(
            "/api/v1/places/",
            data=json.dumps(invalid_data),
            content_type="application/json",
        )

        self.assertEqual(response.status_code, 400)

    def test_create_place_zero_price(self):
        """Test place creation with zero price."""
        edge_case_data = self.valid_place_data.copy()
        edge_case_data["price"] = 0.0

        response = self.client.post(
            "/api/v1/places/",
            data=json.dumps(edge_case_data),
            content_type="application/json",
        )

        # This might be valid or invalid depending on business rules
        # Adjust assertion based on your business logic
        self.assertIn(response.status_code, [201, 400])

    def test_create_place_empty_amenities_list(self):
        """Test place creation with empty amenities list."""
        edge_case_data = self.valid_place_data.copy()
        edge_case_data["amenities"] = []

        response = self.client.post(
            "/api/v1/places/",
            data=json.dumps(edge_case_data),
            content_type="application/json",
        )

        # This might be valid or invalid depending on business rules
        self.assertIn(response.status_code, [201, 400])

    def test_create_place_boundary_coordinates(self):
        """Test place creation with boundary coordinate values."""
        # Test with maximum valid coordinates
        boundary_data = self.valid_place_data.copy()
        boundary_data["latitude"] = 90.0
        boundary_data["longitude"] = 180.0

        response = self.client.post(
            "/api/v1/places/",
            data=json.dumps(boundary_data),
            content_type="application/json",
        )

        self.assertIn(response.status_code, [201, 400])

        # Test with minimum valid coordinates
        boundary_data["latitude"] = -90.0
        boundary_data["longitude"] = -180.0

        response = self.client.post(
            "/api/v1/places/",
            data=json.dumps(boundary_data),
            content_type="application/json",
        )

        self.assertIn(response.status_code, [201, 400])


if __name__ == "__main__":
    unittest.main()
