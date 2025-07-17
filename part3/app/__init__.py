from flask import Flask, send_from_directory
from flask_restx import Api

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


# Inject admin user for testing purposes
def seed_admin():
    if not User.query.filter_by(is_admin=True).first():
        admin = User(
            first_name="Admin",
            last_name="Root",
            email="admin@gmail.com",
            password="admin123",
            is_admin=True,
        )
        db.session.add(admin)
        db.session.commit()
        print("Admin user created ✅")
    else:
        print("Admin user already exists 🧙‍♂️")


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

    # This overrides Swagger UI template to include custom CSS, currently it's dirty af.
    @api.documentation
    def swagger_ui():
        return custom_ui(api)

    api.add_namespace(users_ns, path="/api/v1/users")
    api.add_namespace(places_ns, path="/api/v1/places")
    api.add_namespace(amenity_ns, path="/api/v1/amenities")
    api.add_namespace(reviews_ns, path="/api/v1/reviews")
    api.add_namespace(auth_ns, path="/api/v1/auth")

    with app.app_context():
        db.create_all()
        seed_admin()
    return app
