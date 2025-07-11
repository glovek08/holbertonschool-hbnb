from flask_restx import Namespace, Resource, fields
from app.services import facade
from http import HTTPStatus
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.utils import check_api_payload

api = Namespace("reviews", description="Review operations")

# Define the review model for input validation and documentation
review_model = api.model(
    "ReviewInput",
    {
        "owner_id": fields.String(required=True, description="ID of the user"),
        "place_id": fields.String(required=True, description="ID of the place"),
        "rating": fields.Integer(
            required=True, description="Rating of the place (1-5)"
        ),
        "comment": fields.String(required=True, description="Text of the review"),
    },
)
update_review_model = api.model(
    "ReviewUpdate",
    {
        "rating": fields.Integer(
            required=True, description="Rating of the place (1-5)"
        ),
        "comment": fields.String(required=True, description="Text of the review"),
    },
)
response_review_model = api.model(
    "ReviewResponse",
    {
        "id": fields.String(required=True, description="ID of the review"),
        "owner_id": fields.String(required=True, description="ID of the user"),
        "place_id": fields.String(required=True, description="ID of the place"),
        "rating": fields.Integer(
            required=True, description="Rating of the place (1-5)"
        ),
        "comment": fields.String(required=True, description="Text of the review"),
    },
)


@api.route("/")
class ReviewList(Resource):
    @api.expect(review_model, validate=True)
    @api.response(201, "Review successfully created", response_review_model)
    @api.response(400, "Invalid input data")
    @api.response(403, "Not Authorized")
    @jwt_required()
    def post(self):
        """Create a new review"""
        current_user = get_jwt_identity()
        review_data = api.payload
        # user is authenticated
        if review_data["owner_id"] != current_user:
            return {"error": "Not Authorized"}, 403
        # place exists
        review_target_place = facade.get_place(review_data["place_id"])
        if not review_target_place:
            return {"error": "Place doesn't exist"}, 400
        # user is not the owner of the place
        if review_target_place.owner_id == current_user:
            return {"error": "You cannot review your own place"}, 400
        # user has already review this place
        for review in review_target_place.reviews:
            if review.owner_id == current_user:
                return {"error": "You have already reviewed this place"}, 400

        try:
            new_review = facade.create_review(review_data)
        except (TypeError, ValueError) as e:
            return {"error": str(e)}, 400

        return {
            "id": new_review.id,
            "owner_id": new_review.owner_id,
            "place_id": new_review.place_id,
            "rating": new_review.rating,
            "comment": new_review.comment,
        }, 201

    @api.response(200, "List of reviews retrieved successfully")
    @api.marshal_with(response_review_model, as_list=True)
    def get(self):
        """Retrieve a list of all reviews"""
        reviews = facade.get_all_reviews()
        return [
            {
                "id": review.id,
                "owner_id": review.owner_id,
                "place_id": review.place_id,
                "rating": review.rating,
                "comment": review.comment,
            }
            for review in reviews
        ]


@api.route("/<review_id>")
class ReviewResource(Resource):
    @api.doc(params={"review_id": "The unique ID of the review"})
    @api.response(200, "Review details retrieved successfully", response_review_model)
    @api.response(404, "Review not found")
    def get(self, review_id):
        """Get review details by ID"""
        review = facade.get_review(review_id)
        if not review:
            return {"error": "Review not found"}, 404

        return {
            "id": review.id,
            "owner_id": review.owner_id,
            "place_id": review.place_id,
            "rating": review.rating,
            "comment": review.comment,
        }, 200

    @api.expect(update_review_model, validate=True)
    @api.doc(params={"review_id": "The unique ID of the review"})
    @api.response(200, "Review updated successfully", response_review_model)
    @api.response(404, "Review not found")
    @api.response(400, "Invalid input data")
    @jwt_required()
    def put(self, review_id):
        """Update a review's information"""
        review_new_data = api.payload

        if not check_api_payload(review_new_data, update_review_model):
            return {"error": "Invalid input data"}, 400

        current_user = get_jwt_identity()
        claims = get_jwt()
        is_admin = claims.get("is_admin", False)
        review = facade.get_review(review_id)

        if not review:
            return {"error": "Review not found"}, 404

        if not is_admin or review.owner_id != current_user:
            return {"error": "Unauthorized action."}, 403

        try:
            facade.update_review(review_id, review_new_data)
        except (TypeError, ValueError) as e:
            return {"error": str(e)}, 400

        return {
            "id": review.id,
            "owner_id": review.owner_id,
            "place_id": review.place_id,
            "rating": review.rating,
            "comment": review.comment,
        }, 200

    @api.doc(params={"review_id": "The unique ID of the review"})
    @api.response(200, "Review deleted successfully")
    @api.response(404, "Review not found")
    @jwt_required()
    def delete(self, review_id):
        """Delete a review"""
        current_user = get_jwt_identity()
        review = facade.get_review(review_id)

        if not review:
            return {"error": "Review not found"}, 404

        claims = get_jwt()
        is_admin = claims.get("is_admin", False)

        if not is_admin and review.owner_id != current_user:
            return {"error": "Unauthorized action."}, 403

        facade.delete_review(review_id)

        return {"message": "Review deleted successfully"}, 200


@api.route("/places/<place_id>/reviews")
class PlaceReviewList(Resource):
    @api.doc(params={"place_id": "The unique ID of the place to retrieve reviews"})
    @api.response(
        200,
        "List of reviews for the place retrieved successfully",
        [response_review_model],
    )
    @api.response(404, "Place not found")
    def get(self, place_id):
        """Get all reviews for a specific place"""
        if not facade.get_place(place_id):
            return {"error": "Place not found"}, 404

        reviews = facade.get_reviews_by_place(place_id)

        return [
            {
                "id": review.id,
                "owner_id": review.owner_id,
                "place_id": review.place_id,
                "rating": review.rating,
                "comment": review.comment,
            }
            for review in reviews
        ], 200
