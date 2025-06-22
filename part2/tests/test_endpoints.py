import unittest
from app import create_app


class TestUserEndpoints(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()

    def test_create_user(self):
        response = self.client.post(
            "/api/v1/users/",
            json={
                "first_name": "Jane",
                "last_name": "Doe",
                "email": "jane.doe@example.com",
            },
        )
        self.assertEqual(response.status_code, 201)
        data = response.get_json()
        self.assertIn("id", data)
        self.assertEqual(data["first_name"], "Jane")
        self.assertEqual(data["last_name"], "Doe")
        self.assertEqual(data["email"], "jane.doe@example.com")

    def test_create_user_invalid_data(self):
        response = self.client.post(
            "/api/v1/users/",
            json={"first_name": "", "last_name": "", "email": "invalid-email"},
        )
        self.assertEqual(response.status_code, 400)
        data = response.get_json()
        self.assertIn("error", data)

    def test_get_all_users(self):
        response = self.client.get("/api/v1/users/")
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertIsInstance(data, list)
        # At least the first test user should exist
        self.assertGreaterEqual(len(data), 1)

    def test_get_user_by_id(self):
        # First, create a user
        response = self.client.post(
            "/api/v1/users/",
            json={
                "first_name": "Test",
                "last_name": "User",
                "email": "test.user@example.com",
            },
        )
        self.assertEqual(response.status_code, 201)
        user_id = response.get_json()["id"]

        # Now, retrieve the user by ID
        response = self.client.get(f"/api/v1/users/{user_id}")
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertEqual(data["id"], user_id)
        self.assertEqual(data["first_name"], "Test")
        self.assertEqual(data["last_name"], "User")
        self.assertEqual(data["email"], "test.user@example.com")

    def test_update_user(self):
        # Create a user
        response = self.client.post(
            "/api/v1/users/",
            json={
                "first_name": "Update",
                "last_name": "Me",
                "email": "update.me@example.com",
            },
        )
        self.assertEqual(response.status_code, 201)
        user_id = response.get_json()["id"]

        # Update the user
        response = self.client.put(
            f"/api/v1/users/{user_id}",
            json={
                "first_name": "Updated",
                "last_name": "User",
                "email": "updated.user@example.com",
            },
        )
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertEqual(data["first_name"], "Updated")
        self.assertEqual(data["last_name"], "User")
        self.assertEqual(data["email"], "updated.user@example.com")


class TestAmenitiesEndpoints(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()

    def test_create_amenity(self):
        response = self.client.post(
            "/api/v1/amenity/",
            json={
                "name": "Wi-Fi",
                "description": "The place have wireless Dial-Up connection",
            },
        )
        self.assertEqual(response.status_code, 201)
        data = response.get_json()
        self.assertIn("id", data)
        self.assertEqual(data["name"], "Wi-Fi")
        self.assertEqual(
            data["description"], "The place have wireless Dial-Up connection"
        )

    def test_create_amenity_invalid_data(self):
        response = self.client.post(
            "/api/v1/amenity/",
            json={"name": "", "description": ""},
        )
        self.assertEqual(response.status_code, 400)
        data = response.get_json()
        self.assertIn("error", data)

    def test_get_all_amenities(self):
        response = self.client.get("/api/v1/amenity/")
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertIsInstance(data, list)
        # At least the first test amenity should exist
        self.assertGreaterEqual(len(data), 1)

    def test_get_amenity_by_id(self):
        # First, create an Amenity
        response = self.client.post(
            "/api/v1/amenity/",
            json={
                "name": "Test",
                "description": "n/a",
            },
        )
        self.assertEqual(response.status_code, 201)
        amenity_id = response.get_json()["id"]

        # Now, retrieve the amenity by ID
        response = self.client.get(f"/api/v1/amenity/{amenity_id}")
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertEqual(data["id"], amenity_id)
        self.assertEqual(data["name"], "Test")
        self.assertEqual(data["description"], "n/a")

    def test_update_amenity(self):
        # Create a user
        response = self.client.post(
            "/api/v1/amenity/",
            json={
                "name": "Update",
                "description": "Me",
            },
        )
        self.assertEqual(response.status_code, 201)
        amenity_id = response.get_json()["id"]

        # Update the user
        response = self.client.put(
            f"/api/v1/users/{amenity_id}",
            json={
                "name": "Updated",
                "description": "Amenity",
            },
        )
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertEqual(data["name"], "Updated")
        self.assertEqual(data["description"], "Amenity")


if __name__ == "__main__":
    unittest.main()
