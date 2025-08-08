from flask import Flask, send_from_directory
from flask_restx import Api
from flask_cors import CORS

from config import DevelopmentConfig
from app.extensions import bcrypt, jwt, db

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
from app.api.v1.unsplash import unsplash_ns


def create_app(config_class="config.DevelopmentConfig"):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # It allows the frontend to communicate with the backend
    CORS(app, supports_credentials=True, origins=["http://localhost:5173"])

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

    @api.documentation
    def swagger_ui():
        return custom_ui(api)

    api.add_namespace(users_ns, path="/api/v1/users")
    api.add_namespace(places_ns, path="/api/v1/places")
    api.add_namespace(amenity_ns, path="/api/v1/amenities")
    api.add_namespace(reviews_ns, path="/api/v1/reviews")
    api.add_namespace(auth_ns, path="/api/v1/auth")
    api.add_namespace(unsplash_ns, path="/api/v1/unsplash")

    with app.app_context():
        db.create_all()
        print("CREATED DB!")

    return app
