from flask import Flask
from flask_restx import Api

from app.api.v1.users import api as users_ns
from app.api.v1.places import api as places_ns
from app.api.v1.amenities import api as amenity_ns
from app.services import facade
from app.models.amenity import Amenity
from app.models.place import Place
from app.models.user import User


def create_app():
    app = Flask(__name__)
    api = Api(
        app,
        version="1.0",
        title="HBnB API",
        description="HBnB Application API",
        doc="/api/v1/",
    )

    api.add_namespace(users_ns, path="/api/v1/users")
    api.add_namespace(places_ns, path="/api/v1/places")
    api.add_namespace(amenity_ns, path="/api/v1/amenity")

    # --- TEST DATA START ---
    # Add users
    user1 = User(first_name="Alice", last_name="Smith", email="alice@example.com")
    user2 = User(first_name="Bob", last_name="Brown", email="bob@example.com")
    facade.user_repo.add(user1)
    facade.user_repo.add(user2)

    # Add amenities
    amenity1 = Amenity(name="WiFi", description="Wireless Internet")
    amenity2 = Amenity(name="Pool", description="Swimming Pool")
    facade.amenity_repo.add(amenity1)
    facade.amenity_repo.add(amenity2)

    # Add places
    place1 = Place(
        owner_id=user1.id,
        title="Cozy Cottage",
        description="A small, cozy cottage.",
        price=100.0,
        latitude=40.7128,
        longitude=-74.0060,
        amenities=[amenity1, amenity2],
    )
    place2 = Place(
        owner_id=user2.id,
        title="Modern Apartment",
        description="A stylish apartment in the city.",
        price=150.0,
        latitude=34.0522,
        longitude=-118.2437,
        amenities=[amenity1],
    )
    facade.place_repo.add(place1)
    facade.place_repo.add(place2)
    # --- TEST DATA END ---

    return app
