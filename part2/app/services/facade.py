from app.persistence.respository import InMemoryRepository
from app.models.place import Place
from app.models.user import User


class HBnBFacade:
    def __init__(self):
        self.user_repo = InMemoryRepository()
        self.place_repo = InMemoryRepository()
        self.review_repo = InMemoryRepository()
        self.amenity_repo = InMemoryRepository()

    def create_user(self, user_data):
        user = User(**user_data)
        self.user_repo.add(user)
        return user

    def get_user(self, user_id):
        user = self.user_repo.get(user_id)
        if not user:
            return None
        return User(**user)

    def get_all_users(self):
        return self.user_repo.get_all()

    def get_user_by_email(self, email):
        return self.user_repo.get_by_attribute("email", email)

    def create_place(self, place_data):
        # place = Place(**place_data)
        # self.user_repo.add(place)
        # return place
        required_fields = [
            "owner_id",
            "title",
            "description",
            "price",
            "latitude",
            "longitude",
            "amenities",
        ]
        for field in required_fields:
            if field not in place_data:
                raise ValueError(f"Missing required field: {field}")

        owner = self.user_repo.get(place_data["owner_id"])
        if not owner:
            raise ValueError(f"Owner with ID {place_data['owner_id']} not found")

        amenities = place_data.get("amenities", [])

        new_place = Place(
            owner=owner,
            title=place_data["title"],
            description=place_data["description"],
            amenities=amenities,
        )

        try:
            new_place.price = place_data["price"]
            new_place.latitude = place_data["latitude"]
            new_place.longitude = place_data["longitude"]
        except (TypeError, ValueError) as error:
            raise error

        self.place_repo.add(new_place)
        return new_place

    def get_place(self, place_id):
        return self.place_repo.get(place_id)

    def get_all_places(self):
        return self.place_repo.get_all()

    def update_place(self, place_id, place_data):
        self.place_repo.update(place_id, place_data)
