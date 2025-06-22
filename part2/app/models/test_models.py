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

    def test_amenity_class(self):
        amenity = Amenity(name="Wi-Fi")
        self.assertEqual(amenity.name, "Wi-Fi")
        print("Amenity creation test passed!")


if __name__ == "__main__":
    unittest.main()
