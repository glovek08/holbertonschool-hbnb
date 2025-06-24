from flask import Flask, send_from_directory
from flask_restx import Api

from app.api.v1.users import api as users_ns
from app.api.v1.places import api as places_ns
from app.api.v1.amenities import api as amenity_ns
from app.api.v1.reviews import api as reviews_ns
from app.services import facade
from app.models.amenity import Amenity
from app.models.place import Place
from app.models.user import User
from app.models.review import Review


def create_app():
    app = Flask(__name__)
    
    # Configure Flask-RESTX with custom Swagger UI
    api = Api(
        app,
        version="1.0",
        title="HBnB API",
        description="HBnB Application API",
        doc="/api/v1/",
        default="HBnB",
        default_label="HBnB API Operations"
    )

    # Override Swagger UI template to include custom CSS
    @api.documentation
    def custom_ui():
        return '''
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="UTF-8">
            <title>HBnB API Documentation</title>
            <link rel="stylesheet" type="text/css" href="https://unpkg.com/swagger-ui-dist@3.25.0/swagger-ui.css" />
            <style>
                /* Custom Swagger UI Styling */
                * {
                    color: white !important;
                }
                .model-box {
                    width: 80%;
                }
                .swagger-ui .opblock.opblock-get .opblock-summary {
                    background-color: transparent !important;
                }
                body, #swagger-ui, p {
                    background: #1a1a1a !important;
                    color: #ffffff !important;
                }

                /* Header styling */
                .swagger-ui .topbar {
                    background: #2d2d2d !important;
                    border-bottom: 1px solid #444 !important;
                }

                .swagger-ui .topbar .topbar-wrapper {
                    padding: 10px 0 !important;
                }

                /* Main content area */
                .swagger-ui .wrapper {
                    background: #1a1a1a !important;
                }

                /* Operation sections */
                .swagger-ui .opblock {
                    background: #2d2d2d !important;
                    border: 1px solid #444 !important;
                    border-radius: 6px !important;
                    margin-bottom: 10px !important;
                }
                svg {
                    filter: invert(100%);
                }
                .swagger-ui .opblock.opblock-put {
                    border-color: #b97623 !important;
                }
                .version {
                    background: green !important;
                }
                ..swagger-ui .info .title small pre {
                    background-color: green !important;
                }
                .model-toggle {
                    filter: invert(100%);
                }
                select {
                    color: black !important;
                }

                .swagger-ui .opblock.opblock-post {
                    border-color: #499551 !important;
                }
                .swagger-ui .opblock.opblock-get {
                    border-color: #1896ec !important;
                }
                .swagger-ui .opblock.opblock-delete {
                    border-color: #ad3e15 !important;
                }

                /* Headers and text */
                .swagger-ui .opblock .opblock-summary {
                    color: #ffffff !important;
                }

                .swagger-ui .opblock-description-wrapper p,
                .swagger-ui .opblock-external-docs-wrapper p,
                .swagger-ui .opblock-title_normal p {
                    color: #ffffff !important;
                }
                
                .swagger-ui .opblock.opblock-post .opblock-summary-method {
                    background: #2c5130 !important;
                    color: #ffffff !important;
                    font-weight: bold !important;
                    border-radius: 3px !important;
                    padding: 2px 6px !important;
                    border-color: #66e173 !important;
}
                .swagger-ui .opblock.opblock-get .opblock-summary-method {
                    background: #146fad !important;
                    color: #ffffff !important;
                    font-weight: bold !important;
                    border-radius: 3px !important;
                    padding: 2px 6px !important;
                    border-color: #9e31c4 !important;
}
                .swagger-ui .opblock.opblock-put .opblock-summary-method {
                    background: #595117 !important;
                    color: #ffffff !important;
                    font-weight: bold !important;
                    border-radius: 3px !important;
                    padding: 2px 6px !important;
                    border-color: #cfbd35 !important;
}
                .swagger-ui .opblock.opblock-delete .opblock-summary-method {
                    background: #591b17 !important;
                    color: #ffffff !important;
                    font-weight: bold !important;
                    border-radius: 3px !important;
                    padding: 2px 6px !important;
                    border-color: #da3025 !important;
}
                
                .opblock-section-header {
                    background: black !important;
                }

                /* Response section */
                .swagger-ui .responses-wrapper {
                    background: #2d2d2d !important;
                }

                /* Input fields */
                .swagger-ui .parameters-col_description input,
                .swagger-ui .parameters-col_description select,
                .swagger-ui textarea {
                    background: #383838 !important;
                    color: #ffffff !important;
                    border: 1px solid #555 !important;
                }

                /* Buttons */
                .swagger-ui .btn {
                    color: #ffffff !important;
                    border: none !important;
                }

                .swagger-ui .btn:hover {
                    background: #4e90d9 !important;
                }

                /* Models section */
                .swagger-ui .model-box {
                    background: #2d2d2d !important;
                    border: 1px solid #444 !important;
                }

                .swagger-ui .model .property {
                    color: #ffffff !important;
                }

                /* Additional dark theme improvements */
                .swagger-ui .info {
                    color: #ffffff !important;
                }

                .swagger-ui .info .title {
                    color: #ffffff !important;
                }

                .swagger-ui .scheme-container {
                    background: #2d2d2d !important;
                    border: 1px solid #444 !important;
                }

                .swagger-ui .tab li {
                    color: #ffffff !important;
                }

                .swagger-ui .opblock-summary-path {
                    color: #ffffff !important;
                }
            </style>
        </head>
        <body>
            <div id="swagger-ui"></div>
            <script src="https://unpkg.com/swagger-ui-dist@3.25.0/swagger-ui-bundle.js"></script>
            <script>
                window.onload = function() {
                    const ui = SwaggerUIBundle({
                        url: "''' + api.base_url + '''swagger.json",
                        dom_id: '#swagger-ui',
                        deepLinking: true,
                        presets: [
                            SwaggerUIBundle.presets.apis,
                            SwaggerUIBundle.presets.standalone
                        ],
                        layout: "BaseLayout"
                    });
                };
            </script>
        </body>
        </html>
        '''

    # Custom route to serve custom Swagger UI CSS
    # @app.route('/swaggerui/<path:filename>')
    # def swagger_ui_static(filename):
    #     return send_from_directory('../swaggerui', filename)

    api.add_namespace(users_ns, path="/api/v1/users")
    api.add_namespace(places_ns, path="/api/v1/places")
    api.add_namespace(amenity_ns, path="/api/v1/amenities")
    api.add_namespace(reviews_ns, path="/api/v1/reviews")

      # --- TEST DATA START ---

    # Add users
    user1 = User(first_name="Alice", last_name="Smith", email="alice@example.com")
    user2 = User(first_name="Bob", last_name="Brown", email="bob@example.com")Add commentMore actions
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

    # Add some reviews

    review1 = Review(
        owner_id=user1.id,
        place_id=place1.id,
        rating=4.5,
        comment="Lovely cottage, very cozy and clean!",
    )

    review2 = Review(
        owner_id=user2.id,
        place_id=place1.id,
        rating=4.0,
        comment="Great location, but the WiFi was a bit slow.",
    )

    review3 = Review(
        owner_id=user1.id,
        place_id=place2.id,
        rating=5.0,
        comment="Amazing apartment, would stay again!",
    )
    facade.review_repo.add(review1)
    facade.review_repo.add(review2)
    facade.review_repo.add(review3)

    # [Optional] add reviews to the place objects:
    # place1.reviews.extend([review1, review2])
    # place2.reviews.append(review3)

    # --- TEST DATA END ---


    return app
