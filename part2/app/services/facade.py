from app.persistence.respository import InMemoryRepository
from models.place import Place


class HBnBFacade:
    def __init__(self):
        self.user_repo = InMemoryRepository()
        self.place_repo = InMemoryRepository()
        self.review_repo = InMemoryRepository()
        self.amenity_repo = InMemoryRepository()

    # Placeholder method for creating a user
    def create_user(self, user_data):
        # Logic will be implemented in later tasks
        pass

    def create_place(self, place_data):
        required_fields = [
            "owner",
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
        # No se como manejar el owner. Que llamo? Que le pongo?
        # Como controlar que el owner exista? fijarse si la id existe en la persistence?
        # Lo mismo para amenities.

        return Place(
            owner=place_data["owner"],
            title=place_data["title"],
            description=place_data["description"],
            price=place_data["price"],
            latitude=place_data["latitude"],
            longitude=place_data["longitude"],
            amenities=place_data["amenities"],
        )

    def get_place(self, place_id):
        # Placeholder for logic to retrieve a place by ID, including associated owner and amenities
        pass

    def get_all_places(self):
        # Placeholder for logic to retrieve all places
        pass

    def update_place(self, place_id, place_data):
        # Placeholder for logic to update a place
        pass
