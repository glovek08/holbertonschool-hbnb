from flask import Flask, send_from_directory
from flask_restx import Api

# from sqlalchemy.orm import DeclarativeBase # not used in flask_sqlalchemy (I think)


from config import DevelopmentConfig
from app.extensions import bcrypt
from app.extensions import jwt

# from app.extensions import db

from app.api.v1.users import api as users_ns
from app.api.v1.places import api as places_ns
from app.api.v1.amenities import api as amenity_ns
from app.api.v1.reviews import api as reviews_ns
from app.api.v1.auth import api as auth_ns
from app.api.v1.users import api as admin_ns
from app.services import facade
from app.models.amenity import Amenity
from app.models.place import Place
from app.models.user import User
from app.models.review import Review
from app.custom_ui import custom_ui
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app(config_class="config.DevelopmentConfig"):
    app = Flask(__name__)
    app.config.from_object(config_class)
    bcrypt.init_app(app)
    jwt.init_app(app)
    db.init_app(app)

    # JWT configuration so Swagger can send tokens
    authorizations = {
        "Bearer": {
            "type": "apiKey",
            "in": "header",
            "name": "Authorization",
            "description": "Add a JWT token to the header and remember to append 'Bearer' to the JWT token to authorize the current session user",
        }
    }
    api = Api(
        app,
        version="1.0",
        title="HBnB API",
        description="HBnB Application API",
        doc="/swag/",
        authorizations=authorizations,
        security="Bearer",
        default="HBnB",
        default_label="HBnB API Operations",
    )

    # This overrides Swagger UI template to include custom CSS currently it's dirty af,
    # eventually when we know how, we'll switch to a proper swagger HTML template.
    @api.documentation
    def swagger_ui():
        return custom_ui(api)

    # Custom route to serve custom Swagger UI CSS
    # This will be used to apply a completely custom swagger template
    # @app.route('/swaggerui/<path:filename>')
    # def swagger_ui_static(filename):
    #     return send_from_directory('../swaggerui', filename)

    api.add_namespace(users_ns, path="/api/v1/users")
    api.add_namespace(places_ns, path="/api/v1/places")
    api.add_namespace(amenity_ns, path="/api/v1/amenities")
    api.add_namespace(reviews_ns, path="/api/v1/reviews")
    api.add_namespace(auth_ns, path="/api/v1/auth")

    # region TestData

    # --- TEST DATA START ---

    # Add users
    # user1 = User(
    #     first_name="Alice",
    #     last_name="Smith",
    #     email="alice@live.com",
    #     password="23425",
    #     is_admin=True,
    # )
    # user2 = User(
    #     first_name="Bob", last_name="Brown", email="bob@gmail.com", password="2323"
    # )
    # facade.user_repo.add(user1)
    # facade.user_repo.add(user2)

    # # Add amenities

    # amenity1 = Amenity(name="WiFi", description="Wireless Internet")
    # amenity2 = Amenity(name="Pool", description="Swimming Pool")
    # facade.amenity_repo.add(amenity1)
    # facade.amenity_repo.add(amenity2)

    # # Add places

    # place1 = Place(
    #     owner_id=user1.id,
    #     title="Cozy Cottage",
    #     description="A small, cozy cottage.",
    #     price=100.0,
    #     latitude=40.7128,
    #     longitude=-74.0060,
    #     amenities=[amenity1, amenity2],
    # )

    # place2 = Place(
    #     owner_id=user2.id,
    #     title="Modern Apartment",
    #     description="A stylish apartment in the city.",
    #     price=150.0,
    #     latitude=34.0522,
    #     longitude=-118.2437,
    #     amenities=[amenity1],
    # )
    # place3 = Place(
    #     owner_id=user2.id,
    #     title="Test1",
    #     description="Testest",
    #     price=1520.0,
    #     latitude=34.0522,
    #     longitude=-118.2437,
    #     amenities=[amenity1],
    # )
    # facade.place_repo.add(place1)
    # facade.place_repo.add(place2)
    # facade.place_repo.add(place3)

    # # Add some reviews

    # review1 = Review(
    #     owner_id=user1.id,
    #     place_id=place1.id,
    #     rating=4.5,
    #     comment="Lovely cottage, very cozy and clean!",
    # )

    # review2 = Review(
    #     owner_id=user2.id,
    #     place_id=place1.id,
    #     rating=4.0,
    #     comment="Great location, but the WiFi was a bit slow.",
    # )

    # review3 = Review(
    #     owner_id=user1.id,
    #     place_id=place2.id,
    #     rating=5.0,
    #     comment="Amazing apartment, would stay again!",
    # )
    # facade.review_repo.add(review1)
    # facade.review_repo.add(review2)
    # facade.review_repo.add(review3)

    # [Optional] add reviews to the place objects:
    # place1.reviews.extend([review1, review2])
    # place2.reviews.append(review3)

    # --- TEST DATA END ---
    # endregion

    return app
