from flask_restx import Namespace, Resource, fields
from app.services import facade
from flask_jwt_extended import jwt_required, get_jwt_identity

api = Namespace("users", description="User operations")

# Define the user model for input validation and documentation
user_model = api.model(
    "UserInput",
    {
        "first_name": fields.String(
            required=True, description="First name of the user"
        ),
        "last_name": fields.String(required=True, description="Last name of the user"),
        "email": fields.String(required=True, description="Email of the user"),
        "password": fields.String(required=True, description="User Password"),
    },
)

response_user_model = api.model(
    "UserResponse",
    {
        "id": fields.String(required=True, description="Id of the user"),
        "first_name": fields.String(
            required=True, description="First name of the user"
        ),
        "last_name": fields.String(required=True, description="Last name of the user"),
        "email": fields.String(required=True, description="Email of the user"),
    },
)


@api.route("/")
class UserList(Resource):
    @api.expect(user_model, validate=True)
    @api.response(201, "User successfully created")
    @api.response(400, "Email already registered")
    @api.response(400, "Invalid input data")
    @jwt_required()
    def post(self):
        """Register a new user"""
        user_data = api.payload

        try:
            new_user = facade.create_user(user_data)
        except (TypeError, ValueError) as e:
            return {"error": str(e)}, 400

        return {
            "id": new_user.id,
            # "first_name": new_user.first_name,
            # "last_name": new_user.last_name,
            # "email": new_user.email,
        }, 201

    @api.marshal_with(response_user_model, as_list=True, code=200)  # type: ignore
    @api.response(200, "List of users retrieved successfully")
    def get(self):
        """Get all users"""
        users = facade.get_all_users()
        return [
            {
                "id": user.id,
                "first_name": user.first_name,
                "last_name": user.last_name,
                "email": user.email,
            }
            for user in users
        ]


@api.route("/<user_id>")
class UserResource(Resource):
    @api.doc(params={"user_id": "The unique ID of the user"})
    @api.response(200, "User details retrieved successfully", response_user_model)
    @api.response(404, "User not found")
    def get(self, user_id):
        """Get user details by ID"""
        try:
            user = facade.get_user(user_id)
        except ValueError as e:
            return {"error": str(e)}, 404

        return {
            "id": user.id,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "email": user.email,
        }, 200

    @api.doc(params={"user_id": "The unique ID of the user"})
    @api.expect(user_model, validate=True)
    @api.response(200, "User successfully updated", response_user_model)
    @api.response(400, "Invalid input data or email already registered")
    @jwt_required()
    def put(self, user_id):
        """Update user information by ID"""
        user_new_data = api.payload

        try:
            user = facade.get_user(user_id)
        except ValueError as e:
            return {"error": str(e)}, 404

        try:
            facade.update_user(user_id, user_new_data)
        except (TypeError, ValueError) as e:
            return {"error": str(e)}, 400

        return {
            "id": user.id,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "email": user.email,
        }, 200
