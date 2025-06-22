from flask_restx import Namespace, Resource, fields
from app.services import facade

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
    @api.expect(review_model)
    @api.response(201, "Review successfully created", response_review_model)
    @api.response(400, "Invalid input data")
    def post(self):
        """Create a new review"""
        review_data = api.payload

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
    @api.marshal_with(response_review_model, as_list=True, code=200)
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
        try:
            review = facade.get_review(review_id)
        except ValueError as e:
            return {"error": str(e)}, 404

        return {
            "id": review.id,
            "owner_id": review.owner_id,
            "place_id": review.place_id,
            "rating": review.rating,
            "comment": review.comment,
        }, 200

    @api.expect(review_model)
    @api.doc(params={"review_id": "The unique ID of the review"})
    @api.response(200, "Review updated successfully", response_review_model)
    @api.response(404, "Review not found")
    @api.response(400, "Invalid input data")
    def put(self, review_id):
        """Update a review's information"""
        review_new_data = api.payload

        try:
            review = facade.get_review(review_id)
        except ValueError as e:
            return {"error": str(e)}, 404

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
    def delete(self, review_id):
        """Delete a review"""
        try:
            facade.delete_review(review_id)
        except ValueError as e:
            return {"error": str(e)}, 404

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
        try:
            reviews = facade.get_reviews_by_place(place_id)
        except ValueError as e:
            return {"error": str(e)}, 404

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
