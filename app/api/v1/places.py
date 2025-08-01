# fmt: off
from flask_restx import Namespace, Resource, fields
from flask import request
from app.services import facade
from app.utils import check_api_payload
from sqlalchemy.exc import IntegrityError
from flask_jwt_extended import jwt_required, get_jwt_identity, get_jwt

api = Namespace("places", description="Place operations")


owner_model = api.model(
    "Owner",
    {
        "first_name": fields.String(description="First name of the owner"),
        "last_name":  fields.String(description="Last name of the owner"),
    }
)

amenity_model = api.model(
    "Amenity",
    {
        "id":          fields.String(description="ID of the amenity"),
        "name":        fields.String(description="Name of the amenity"),
        "description": fields.String(description="Description of the amenity"),
    }
)
review_model = api.model(
    "Review",
    {
        "id":          fields.String(description="ID of the review"),
        "owner_id":    fields.String(description="ID of the user who wrote the review"),
        "rating":      fields.Float(description="Rating given by the user"),
        "comment":     fields.String(description="Comment provided by the user"),
    }
)


place_model = api.model(
    "Place",
    {
        "title":        fields.String(required=True, description="Title of the place"),
        "description":  fields.String(description="Description of the place"),
        "price":        fields.Float(required=True, description="Price per night"),
        "latitude":     fields.Float(required=True, description="Latitude of the place"),
        "longitude":    fields.Float(required=True, description="Longitude of the place"),
        "owner_id":     fields.String(required=True, description="ID of the owner"),
        "amenities":    fields.List(
            fields.Nested(amenity_model), description="List of amenities"
        ),
    },
)

place_response_model = api.model(
    "Place_Response",
    {
        "id":           fields.String(required=True, description="Unique ID of the place"),
        "title":        fields.String(required=True, description="Title of the place"),
        "description":  fields.String(description="Description of the place"),
        "price":        fields.Float(required=True, description="Price per night"),
        "latitude":     fields.Float(required=True, description="Latitude of the place"),
        "longitude":    fields.Float(required=True, description="Longitude of the place"),
        "owner_id":     fields.String(required=True, description="ID of the owner"),
        "owner":        fields.Nested(owner_model, description="Owner of the place"),
        "amenities":    fields.List(
            fields.Nested(amenity_model), description="List of amenities"
        ),
        "reviews":      fields.List(
            fields.Nested(review_model), description="List of reviews for the place"
        ),
    }
)

@api.route("/")
class PlaceList(Resource):
    @api.expect(place_model, validate=True)
    @api.marshal_with(place_response_model, code=201) # type: ignore
    @api.response(201, "Place successfully created")
    @api.response(400, "Invalid input data")
    @api.response(403, "Cannot create place for another user")
    @api.response(404, "User doesn't exists")
    @api.doc(security="Bearer")
    @jwt_required()
    def post(self):
        """Register a new place"""
        place_data = api.payload
        current_user = get_jwt_identity()
        claims = get_jwt()

        if not (claims.get("is_admin", False) or place_data["owner_id"] == current_user):
            return {"error": "Unauthorized: cannot create place for another user"}, 403

        try:
            new_place = facade.create_place(place_data)
        except IntegrityError as error:
            return {"error": str(error)}, 404
        except (TypeError, ValueError) as error:
            return {"error": str(error)}, 400

        return new_place.to_dict(), 201

    @api.marshal_with(place_response_model, as_list=True)
    @api.response(200, "List of places retrieved successfully")
    def get(self):
        """Retrieve a list of places with reviews"""
        places = facade.get_all_places()
        place_list = []
        for place in places:
            place_dict = place.to_dict()
            reviews = facade.get_reviews_by_place(place.id)
            place_dict["reviews"] = [review.to_dict() for review in reviews]
            place_list.append(place_dict)
        return place_list


@api.route("/<place_id>")
class PlaceResource(Resource):
    @api.doc(params={"place_id": "The unique ID of the place"})
    @api.marshal_with(place_response_model)
    @api.response(200, "Place details retrieved successfully")
    @api.response(404, "Place not found")
    def get(self, place_id):
        """Get place details by ID"""
        place = facade.get_place(place_id)
        if not place:
            return {"error": "Place not found"}, 404
        reviews = facade.get_reviews_by_place(place_id)
        place_dict = place.to_dict()
        place_dict["reviews"] = [review.to_dict() for review in reviews]

        return place_dict, 200

    @api.expect(place_model, validate=True)
    @api.doc(params={"place_id": "The unique ID of the place"})
    @api.marshal_with(place_model)
    @api.response(200, "Place updated successfully")
    @api.response(400, "Invalid input data")
    @api.response(403, "Unauthorized action")
    @api.response(404, "Place not found")
    @api.doc(security="Bearer")
    @jwt_required()
    def put(self, place_id):
        """Update place information by ID"""
        place_new_data = api.payload
        current_user = get_jwt_identity()
        claims = get_jwt()
        is_admin = claims.get("is_admin", False)

        if not check_api_payload(place_new_data, place_model):
            return {"error": "Invalid input data"}, 400

        place = facade.get_place(place_id)
        if not place:
            return {"error": "Place not found"}, 404

        if not is_admin and (
            place.owner_id != current_user or 
            place_new_data["owner_id"] != current_user
        ):
            return {"error": "Unauthorized action"}, 403

        try:
            facade.update_place(place_id, place_new_data)
        except (TypeError, ValueError) as error:
            return {"error": str(error)}, 400

        return place.to_dict(), 200

    @api.doc(params={"place_id": "The unique ID of the place"})
    @api.response(200, "Place deleted successfully")
    @api.response(404, "Place not found")
    @jwt_required()
    def delete(self, place_id):
        """Delete a place"""
        current_user = get_jwt_identity()
        claims = get_jwt()
        is_admin = claims.get("is_admin", False)

        place = facade.get_place(place_id)
        if not place:
            return {"error": "Place not found"}, 404

        if not (is_admin or place.owner_id == current_user):
            return {"error": "Unauthorized action"}, 403

        facade.delete_place(place_id)

        return {"message": "Place deleted successfully"}, 200
