import unittest
from app.models.user import User
from app.models.review import Review
from app.models.place import Place
from app.models.amenity import Amenity


class TestModels(unittest.TestCase):
    def test_user_creation(self):
        user = User(first_name="John", last_name="Doe", email="john.doe@example.com")
        self.assertEqual(user.first_name, "John")
        self.assertEqual(user.last_name, "Doe")
        self.assertEqual(user.email, "john.doe@example.com")
        self.assertFalse(user.is_admin)  # Default value

    def test_user_invalid_email(self):
        with self.assertRaises(ValueError):
            User(first_name="Jane", last_name="Doe", email="invalid-email")

    def test_user_invalid_name(self):
        with self.assertRaises(ValueError):
            User(first_name="John123", last_name="Doe", email="john.doe@example.com")

    def test_place_creation(self):
        owner = User(
            first_name="Alice", last_name="Smith", email="alice.smith@example.com"
        )
        place = Place(
            owner_id=owner.id,
            title="Cozy Apartment",
            description="A nice place to stay",
            price=100,
            latitude=37.7749,
            longitude=-122.4194,
            amenities=[],
            reviews=[],
        )

        # Create a review and add to place
        review = Review(
            owner_id=owner.id, place_id=place.id, rating=5, comment="Great stay!"
        )
        place.add_review(review)

        self.assertEqual(place.title, "Cozy Apartment")
        self.assertEqual(place.price, 100)
        self.assertEqual(len(place.reviews), 1)
        self.assertEqual(place.reviews[0].comment, "Great stay!")

    def test_place_invalid_latitude(self):
        owner = User(
            first_name="Alice", last_name="Smith", email="alice.smith@example.com"
        )
        with self.assertRaises(ValueError):
            Place(
                owner_id=owner.id,
                title="Invalid Place",
                description="Bad latitude",
                price=50,
                latitude=200,  # Invalid latitude
                longitude=0,
                amenities=[],
            )

    def test_place_add_remove_amenity(self):
        owner = User(
            first_name="Alice", last_name="Smith", email="alice.smith@example.com"
        )
        wifi = Amenity(name="Wi-Fi")
        place = Place(
            owner_id=owner.id,
            title="Test Place",
            description="Test",
            price=10,
            latitude=0,
            longitude=0,
            amenities=[],
        )
        place.add_amenity(wifi)
        self.assertIn(wifi, place.amenities)
        place.remove_amenity(wifi)
        self.assertNotIn(wifi, place.amenities)

    def test_amenity_class(self):
        amenity = Amenity(name="Wi-Fi")
        self.assertEqual(amenity.name, "Wi-Fi")
        print("Amenity creation test passed!")

    def test_review_creation_and_validation(self):
        user = User(first_name="Bob", last_name="Lee", email="bob.lee@example.com")
        place = Place(
            owner_id=user.id,
            title="Nice Place",
            description="Nice",
            price=80,
            latitude=10,
            longitude=10,
            amenities=[],
        )
        review = Review(
            owner_id=user.id, place_id=place.id, rating=4.5, comment="Very good!"
        )
        self.assertEqual(review.rating, 4.5)
        self.assertEqual(review.comment, "Very good!")
        with self.assertRaises(ValueError):
            Review(
                owner_id=user.id, place_id=place.id, rating=6, comment="Too high!"
            )  # Invalid rating

    def test_review_invalid_owner_id(self):
        place = Place(
            owner_id="fakeid",
            title="Test",
            description="Test",
            price=10,
            latitude=0,
            longitude=0,
            amenities=[],
        )
        with self.assertRaises(TypeError):
            Review(
                owner_id=123, place_id=place.id, rating=3, comment="Bad owner id"
            )  # owner_id as str

    def test_review_invalid_comment(self):
        user = User(first_name="Bob", last_name="Lee", email="bob.lee@example.com")
        place = Place(
            owner_id=user.id,
            title="Nice Place",
            description="Nice",
            price=80,
            latitude=10,
            longitude=10,
            amenities=[],
        )
        with self.assertRaises(TypeError):
            Review(
                owner_id=user.id, place_id=place.id, rating=4, comment=123
            )  # comment not str


if __name__ == "__main__":
    unittest.main()
