import unittest
import json
from app import create_app


class TestReviewsAPI(unittest.TestCase):
    def setUp(self):
        """Set up test fixtures before each test method."""
        self.app = create_app()
        self.app.config["TESTING"] = True
        self.client = self.app.test_client()

        # Create a test user first
        self.test_user_data = {
            "first_name": "John",
            "last_name": "Doe",
            "email": "john.doe@test.com",
        }

        # Create user and store the ID for review creation
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

        # Create test amenity for place creation
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

        # Create a test place
        self.test_place_data = {
            "title": "Test Place for Reviews",
            "description": "A place to test reviews",
            "price": 100.0,
            "latitude": 40.7128,
            "longitude": -74.0060,
            "owner_id": self.test_user_id,
            "amenities": [self.test_amenity_id],
        }

        # Create place and store the ID for review creation
        place_response = self.client.post(
            "/api/v1/places/",
            data=json.dumps(self.test_place_data),
            content_type="application/json",
        )

        if place_response.status_code == 201:
            # Get all places to find the created place ID
            all_places_response = self.client.get("/api/v1/places/")
            all_places = json.loads(all_places_response.data)
            if len(all_places) > 0:
                self.test_place_id = all_places[-1]["id"]  # Get the last created place
            else:
                self.test_place_id = "test-place-123"
        else:
            # Fallback - use a known test place ID
            self.test_place_id = "test-place-123"

        # Valid review data for testing
        self.valid_review_data = {
            "owner_id": self.test_user_id,
            "place_id": self.test_place_id,
            "rating": 5,
            "comment": "Excellent place to stay!",
        }

    def test_create_review_success(self):
        """Test successful review creation."""
        response = self.client.post(
            "/api/v1/reviews/",
            data=json.dumps(self.valid_review_data),
            content_type="application/json",
        )

        self.assertEqual(response.status_code, 201)
        data = json.loads(response.data)
        self.assertEqual(data["owner_id"], self.test_user_id)
        self.assertEqual(data["place_id"], self.test_place_id)
        self.assertEqual(data["rating"], 5)
        self.assertEqual(data["comment"], "Excellent place to stay!")
        self.assertIn("id", data)

    def test_create_review_missing_owner_id(self):
        """Test review creation with missing owner_id."""
        invalid_data = self.valid_review_data.copy()
        del invalid_data["owner_id"]

        response = self.client.post(
            "/api/v1/reviews/",
            data=json.dumps(invalid_data),
            content_type="application/json",
        )

        self.assertEqual(response.status_code, 400)

    def test_create_review_missing_place_id(self):
        """Test review creation with missing place_id."""
        invalid_data = self.valid_review_data.copy()
        del invalid_data["place_id"]

        response = self.client.post(
            "/api/v1/reviews/",
            data=json.dumps(invalid_data),
            content_type="application/json",
        )

        self.assertEqual(response.status_code, 400)

    def test_create_review_missing_rating(self):
        """Test review creation with missing rating."""
        invalid_data = self.valid_review_data.copy()
        del invalid_data["rating"]

        response = self.client.post(
            "/api/v1/reviews/",
            data=json.dumps(invalid_data),
            content_type="application/json",
        )

        self.assertEqual(response.status_code, 400)

    def test_create_review_missing_comment(self):
        """Test review creation with missing comment."""
        invalid_data = self.valid_review_data.copy()
        del invalid_data["comment"]

        response = self.client.post(
            "/api/v1/reviews/",
            data=json.dumps(invalid_data),
            content_type="application/json",
        )

        self.assertEqual(response.status_code, 400)

    def test_create_review_invalid_rating_high(self):
        """Test review creation with rating above 5."""
        invalid_data = self.valid_review_data.copy()
        invalid_data["rating"] = 6

        response = self.client.post(
            "/api/v1/reviews/",
            data=json.dumps(invalid_data),
            content_type="application/json",
        )

        self.assertEqual(response.status_code, 400)

    def test_create_review_invalid_rating_low(self):
        """Test review creation with rating below 1."""
        invalid_data = self.valid_review_data.copy()
        invalid_data["rating"] = 0

        response = self.client.post(
            "/api/v1/reviews/",
            data=json.dumps(invalid_data),
            content_type="application/json",
        )

        self.assertEqual(response.status_code, 400)

    def test_create_review_invalid_rating_type(self):
        """Test review creation with invalid rating type."""
        invalid_data = self.valid_review_data.copy()
        invalid_data["rating"] = "five"

        response = self.client.post(
            "/api/v1/reviews/",
            data=json.dumps(invalid_data),
            content_type="application/json",
        )

        self.assertEqual(response.status_code, 400)

    def test_create_review_nonexistent_owner(self):
        """Test review creation with non-existent owner_id."""
        invalid_data = self.valid_review_data.copy()
        invalid_data["owner_id"] = "nonexistent-user-id"

        response = self.client.post(
            "/api/v1/reviews/",
            data=json.dumps(invalid_data),
            content_type="application/json",
        )

        self.assertEqual(response.status_code, 400)

    def test_create_review_nonexistent_place(self):
        """Test review creation with non-existent place_id."""
        invalid_data = self.valid_review_data.copy()
        invalid_data["place_id"] = "nonexistent-place-id"

        response = self.client.post(
            "/api/v1/reviews/",
            data=json.dumps(invalid_data),
            content_type="application/json",
        )

        self.assertEqual(response.status_code, 400)

    def test_create_review_empty_comment(self):
        """Test review creation with empty comment."""
        invalid_data = self.valid_review_data.copy()
        invalid_data["comment"] = ""

        response = self.client.post(
            "/api/v1/reviews/",
            data=json.dumps(invalid_data),
            content_type="application/json",
        )

        self.assertEqual(response.status_code, 400)

    def test_get_all_reviews_success(self):
        """Test successful retrieval of all reviews."""
        # First create a review
        self.client.post(
            "/api/v1/reviews/",
            data=json.dumps(self.valid_review_data),
            content_type="application/json",
        )

        # Then get all reviews
        response = self.client.get("/api/v1/reviews/")

        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertIsInstance(data, list)

        if len(data) > 0:
            review = data[0]
            self.assertIn("id", review)
            self.assertIn("owner_id", review)
            self.assertIn("place_id", review)
            self.assertIn("rating", review)
            self.assertIn("comment", review)

    def test_get_review_by_id_success(self):
        """Test successful retrieval of a review by ID."""
        # First create a review
        create_response = self.client.post(
            "/api/v1/reviews/",
            data=json.dumps(self.valid_review_data),
            content_type="application/json",
        )

        self.assertEqual(create_response.status_code, 201)
        created_review = json.loads(create_response.data)
        review_id = created_review["id"]

        # Test getting review by ID
        response = self.client.get(f"/api/v1/reviews/{review_id}")

        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data["id"], review_id)
        self.assertEqual(data["owner_id"], self.test_user_id)
        self.assertEqual(data["place_id"], self.test_place_id)
        self.assertEqual(data["rating"], 5)
        self.assertEqual(data["comment"], "Excellent place to stay!")

    def test_get_review_by_invalid_id(self):
        """Test retrieval of a review with invalid ID."""
        response = self.client.get("/api/v1/reviews/invalid-id")

        self.assertEqual(response.status_code, 404)
        data = json.loads(response.data)
        self.assertIn("error", data)

    def test_get_review_by_nonexistent_id(self):
        """Test retrieval of a review with non-existent ID."""
        response = self.client.get("/api/v1/reviews/nonexistent-review-id")

        self.assertEqual(response.status_code, 404)
        data = json.loads(response.data)
        self.assertIn("error", data)

    def test_update_review_success(self):
        """Test successful review update."""
        # First create a review
        create_response = self.client.post(
            "/api/v1/reviews/",
            data=json.dumps(self.valid_review_data),
            content_type="application/json",
        )

        self.assertEqual(create_response.status_code, 201)
        created_review = json.loads(create_response.data)
        review_id = created_review["id"]

        # Update data
        update_data = self.valid_review_data.copy()
        update_data["rating"] = 4
        update_data["comment"] = "Good place, but could be better"

        # Test updating review
        response = self.client.put(
            f"/api/v1/reviews/{review_id}",
            data=json.dumps(update_data),
            content_type="application/json",
        )

        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data["rating"], 4)
        self.assertEqual(data["comment"], "Good place, but could be better")

    def test_update_review_invalid_id(self):
        """Test update of a review with invalid ID."""
        response = self.client.put(
            "/api/v1/reviews/invalid-id",
            data=json.dumps(self.valid_review_data),
            content_type="application/json",
        )

        self.assertEqual(response.status_code, 404)
        data = json.loads(response.data)
        self.assertIn("error", data)

    def test_update_review_invalid_data(self):
        """Test update of a review with invalid data."""
        # First create a review
        create_response = self.client.post(
            "/api/v1/reviews/",
            data=json.dumps(self.valid_review_data),
            content_type="application/json",
        )

        if create_response.status_code == 201:
            created_review = json.loads(create_response.data)
            review_id = created_review["id"]

            # Invalid update data (rating out of range)
            invalid_update_data = self.valid_review_data.copy()
            invalid_update_data["rating"] = 10

            response = self.client.put(
                f"/api/v1/reviews/{review_id}",
                data=json.dumps(invalid_update_data),
                content_type="application/json",
            )

            self.assertEqual(response.status_code, 400)

    def test_delete_review_success(self):
        """Test successful review deletion."""
        # First create a review
        create_response = self.client.post(
            "/api/v1/reviews/",
            data=json.dumps(self.valid_review_data),
            content_type="application/json",
        )

        self.assertEqual(create_response.status_code, 201)
        created_review = json.loads(create_response.data)
        review_id = created_review["id"]

        # Test deleting review
        response = self.client.delete(f"/api/v1/reviews/{review_id}")

        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertIn("message", data)
        self.assertEqual(data["message"], "Review deleted successfully")

        # Verify review is deleted by trying to get it
        get_response = self.client.get(f"/api/v1/reviews/{review_id}")
        self.assertEqual(get_response.status_code, 404)

    def test_delete_review_invalid_id(self):
        """Test deletion of a review with invalid ID."""
        response = self.client.delete("/api/v1/reviews/invalid-id")

        self.assertEqual(response.status_code, 404)
        data = json.loads(response.data)
        self.assertIn("error", data)

    def test_delete_review_nonexistent_id(self):
        """Test deletion of a review with non-existent ID."""
        response = self.client.delete("/api/v1/reviews/nonexistent-review-id")

        self.assertEqual(response.status_code, 404)
        data = json.loads(response.data)
        self.assertIn("error", data)

    def test_get_reviews_by_place_success(self):
        """Test successful retrieval of reviews by place ID."""
        # First create a review for the place
        create_response = self.client.post(
            "/api/v1/reviews/",
            data=json.dumps(self.valid_review_data),
            content_type="application/json",
        )

        self.assertEqual(create_response.status_code, 201)

        # Test getting reviews by place ID
        response = self.client.get(
            f"/api/v1/reviews/places/{self.test_place_id}/reviews"
        )

        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertIsInstance(data, list)

        if len(data) > 0:
            review = data[0]
            self.assertEqual(review["place_id"], self.test_place_id)
            self.assertIn("id", review)
            self.assertIn("owner_id", review)
            self.assertIn("rating", review)
            self.assertIn("comment", review)

    def test_get_reviews_by_nonexistent_place(self):
        """Test retrieval of reviews for non-existent place."""
        response = self.client.get(
            "/api/v1/reviews/places/nonexistent-place-id/reviews"
        )

        self.assertEqual(response.status_code, 404)
        data = json.loads(response.data)
        self.assertIn("error", data)

    def test_get_reviews_by_invalid_place_id(self):
        """Test retrieval of reviews for invalid place ID."""
        response = self.client.get("/api/v1/reviews/places/invalid-place-id/reviews")

        self.assertEqual(response.status_code, 404)
        data = json.loads(response.data)
        self.assertIn("error", data)

    def test_create_review_boundary_ratings(self):
        """Test review creation with boundary rating values."""
        # Test with minimum valid rating (1)
        boundary_data = self.valid_review_data.copy()
        boundary_data["rating"] = 1

        response = self.client.post(
            "/api/v1/reviews/",
            data=json.dumps(boundary_data),
            content_type="application/json",
        )

        self.assertEqual(response.status_code, 201)
        data = json.loads(response.data)
        self.assertEqual(data["rating"], 1)

        # Test with maximum valid rating (5)
        boundary_data["rating"] = 5

        response = self.client.post(
            "/api/v1/reviews/",
            data=json.dumps(boundary_data),
            content_type="application/json",
        )

        self.assertEqual(response.status_code, 201)
        data = json.loads(response.data)
        self.assertEqual(data["rating"], 5)

    def test_create_review_very_long_comment(self):
        """Test review creation with very long comment."""
        long_comment_data = self.valid_review_data.copy()
        long_comment_data["comment"] = (
            "This is a very long comment " * 100
        )  # Very long comment

        response = self.client.post(
            "/api/v1/reviews/",
            data=json.dumps(long_comment_data),
            content_type="application/json",
        )

        # This might be valid or invalid depending on business rules
        self.assertIn(response.status_code, [201, 400])

    def test_create_multiple_reviews_same_user_place(self):
        """Test creating multiple reviews for the same place by the same user."""
        # Create first review
        first_response = self.client.post(
            "/api/v1/reviews/",
            data=json.dumps(self.valid_review_data),
            content_type="application/json",
        )

        self.assertEqual(first_response.status_code, 201)

        # Try to create second review for the same place by the same user
        second_review_data = self.valid_review_data.copy()
        second_review_data["comment"] = "Another review for the same place"
        second_review_data["rating"] = 3

        second_response = self.client.post(
            "/api/v1/reviews/",
            data=json.dumps(second_review_data),
            content_type="application/json",
        )

        # This might be allowed or not depending on business rules
        self.assertIn(second_response.status_code, [201, 400])

    def test_update_review_change_place_id(self):
        """Test updating a review to change place_id."""
        # First create a review
        create_response = self.client.post(
            "/api/v1/reviews/",
            data=json.dumps(self.valid_review_data),
            content_type="application/json",
        )

        if create_response.status_code == 201:
            created_review = json.loads(create_response.data)
            review_id = created_review["id"]

            # Try to update with different place_id
            update_data = self.valid_review_data.copy()
            update_data["place_id"] = "different-place-id"

            response = self.client.put(
                f"/api/v1/reviews/{review_id}",
                data=json.dumps(update_data),
                content_type="application/json",
            )

            # This might be allowed or not depending on business rules
            self.assertIn(response.status_code, [200, 400, 404])

    def test_create_review_float_rating(self):
        """Test review creation with float rating."""
        invalid_data = self.valid_review_data.copy()
        invalid_data["rating"] = 3.5

        response = self.client.post(
            "/api/v1/reviews/",
            data=json.dumps(invalid_data),
            content_type="application/json",
        )

        # Should be invalid since rating should be integer
        self.assertEqual(response.status_code, 400)


if __name__ == "__main__":
    unittest.main()
