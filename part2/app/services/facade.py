from app.persistence.respository import InMemoryRepository
from app.models.place import Place


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
        return self.user_repo.get(user_id)

    def get_user_by_email(self, email):
        return self.user_repo.get_by_attribute("email", email)

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
        # No se como manejar el owner. Que llamo? Que le pongo?, llamar al user_repo con el id del user y pasarle la instancia
        # que retorna a new_place?
        # Como controlar que el owner exista? fijarse si la id existe en la persistence?
        # Lo mismo para amenities.

        new_place = Place(
            owner=place_data["owner"],  # Placeholder
            title=place_data["title"],
            description=place_data["description"],
            amenities=place_data["amenities"],  # Placeholder
        )
        # price, longitude and latitude validation handled in setters. read task_04_place.
        try:
            new_place.price = place_data["price"]
            new_place.latitude = place_data["longitude"]
            new_place.longitude = place_data["latitude"]
        except TypeError as t_error:
            raise t_error
        except ValueError as v_error:
            raise v_error
        except Exception as error:
            raise error
        self.place_repo.add(new_place)

    def get_place(self, place_id):
        return self.place_repo.get(place_id)

    def get_all_places(self):
        return self.place_repo.get_all()

    def update_place(self, place_id, place_data):
        self.place_repo.update(place_id, place_data)
