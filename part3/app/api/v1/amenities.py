from flask_restx import Namespace, Resource, fields
from app.services import facade
from flask_jwt_extended import jwt_required, get_jwt_identity, get_jwt

api = Namespace("amenities", description="Amenity operations")

# Define the amenity model for input validation and documentation
amenity_model = api.model(
    "AmenityInput",
    {
        "name": fields.String(required=True, description="Name of the amenity"),
        "description": fields.String(
            required=False, description="Short description of the amenity"
        ),
    },
)

response_amenity_model = api.model(
    "AmenityResponse",
    {
        "id": fields.String(requiered=True, description="ID of the amenity"),
        "name": fields.String(required=True, description="Name of the amenity"),
        "description": fields.String(
            required=False, description="Short description of the amenity"
        ),
    },
)


@api.route("/")
class AmenityList(Resource):
    @api.expect(amenity_model, validate=True)
    @api.response(201, "Amenity successfully created", response_amenity_model)
    @api.response(400, "Invalid input data")
    @jwt_required
    def post(self):
        """Register a new amenity"""
        amenity_data = api.payload
        claims = get_jwt()
        is_admin = claims.get("is_admin", False)
        if not is_admin:
            return {"error": "Admin privileges required"}, 403
        try:
            new_amenity = facade.create_amenity(amenity_data)
        except (TypeError, ValueError) as error:
            return {"error": str(error)}, 400
        return {
            "id": new_amenity.id,
            "name": new_amenity.name,
            "description": new_amenity.description,
        }, 201

    @api.response(
        200, "List of amenities retrieved successfully", [response_amenity_model]
    )
    def get(self):
        """Retrieve a list of all amenities"""
        amenities = facade.get_all_amenities()
        return [
            {"id": amenity.id, "name": amenity.name, "description": amenity.description}
            for amenity in amenities
        ], 200


@api.route("/<amenity_id>")
class AmenityResource(Resource):
    @api.doc(params={"amenity_id": "The unique ID of the amenity"})
    @api.response(200, "Amenity details retrieved successfully", response_amenity_model)
    @api.response(404, "Amenity not found")
    def get(self, amenity_id):
        """Get amenity details by ID"""
        my_amenity = facade.get_amenity(amenity_id)
        if not amenity:  # type: ignore
            return {"error": "Amenity not found"}, 404

        return {
            "id": my_amenity.id,  # type: ignore
            "name": my_amenity.name,  # type: ignore
            "description": my_amenity.description,  # type: ignore
        }, 200

    @api.expect(amenity_model, validate=True)
    @api.doc(params={"amenity_id": "The unique ID of the amenity"})
    @api.response(200, "Amenity updated successfully", response_amenity_model)
    @api.response(404, "Amenity not found")
    @api.response(400, "Invalid input data")
    def put(self, amenity_id):
        """Update an amenity's information"""
        amenity_data = api.payload
        my_amenity = facade.get_amenity(amenity_id)
        if not my_amenity:
            return {"error": "Amenity not found"}, 404

        try:
            facade.update_amenity(amenity_id, amenity_data)
        except (TypeError, ValueError) as error:
            return {"error": str(error)}, 400

        return {
            "id": my_amenity.id,
            "name": my_amenity.name,
            "description": my_amenity.description,
        }, 200
