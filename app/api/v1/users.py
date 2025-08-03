# fmt: off
from flask_restx import Namespace, Resource, fields
from app.services import facade
from sqlalchemy.exc import IntegrityError
from flask_jwt_extended import jwt_required, get_jwt_identity, get_jwt, create_access_token
from app.utils import check_api_payload

api = Namespace("users", description="User operations")

user_model = api.model(
    "UserInput",
    {
        "first_name":   fields.String(
            required=True, description="First name of the user"
        ),
        "last_name":    fields.String(required=True, description="Last name of the user"),
        "email":        fields.String(required=True, description="Email of the user"),
        "password":     fields.String(required=True, description="User Password"),
    },
)

response_user_model = api.model(
    "UserResponse",
    {
        "id":           fields.String(required=True, description="Id of the user"),
        "first_name":   fields.String(
            required=True, description="First name of the user"
        ),
        "last_name":    fields.String(required=True, description="Last name of the user"),
        "email":        fields.String(required=True, description="Email of the user"),
        "is_admin":     fields.Boolean(required=True, description="Verifies if the user is administrator"),
    },
)


@api.route("/")
class UserList(Resource):
    @api.expect(user_model, validate=True)
    @api.response(201, "User successfully created")
    @api.response(403, "Admin privileges required")
    @jwt_required()
    def post(self):
        """Register a new user"""
        user_data = api.payload
        claims = get_jwt()
        is_admin = claims.get("is_admin", False)

        if "is_admin" in user_data and not is_admin: # this prevents manual is_admin injection
            return {"error": "You can't do that boy."}, 403

        try:
            new_user = facade.create_user(user_data)
            access_token = create_access_token(identity=new_user.id)
        except IntegrityError as error:
            return {"error": str(error)}, 409
        except (TypeError, ValueError) as error:
            return {"error": str(error)}, 400

        return {
            "id": new_user.id,
            "access_token": access_token
        }, 201

    @api.marshal_with(response_user_model, as_list=True)
    @api.response(200, "List of users retrieved successfully")
    def get(self):
        """Get all users"""
        users = facade.get_all_users()
        return [user.to_dict() for user in users]


@api.route("/<user_id>")
class UserResource(Resource):
    @api.doc(params={"user_id": "The unique ID of the user"})
    @api.marshal_with(response_user_model)
    @api.response(200, "User details retrieved successfully")
    @api.response(404, "User not found")
    def get(self, user_id):
        """Get user details by ID"""
        user = facade.get_user(user_id)
        if not user:
            return {"error": "User not found"}, 404

        return user.to_dict(), 200

    @api.expect(user_model, validate=True)
    @api.doc(params={"user_id": "The unique ID of the user"})
    @api.marshal_with(response_user_model)
    @api.response(200, "User successfully updated")
    @api.response(400, "Invalid input data or email already registered")
    @jwt_required()
    def put(self, user_id):
        """Update user information by ID"""
        user_new_data = api.payload
        if not check_api_payload(user_new_data, user_model):
            return {"error": "Invalid input data"}, 400

        current_user = get_jwt_identity()
        user = facade.get_user(user_id)
        if not user:
            return {"error": "User not found"}, 404
        
        claims = get_jwt()
        is_admin = claims.get("is_admin", False)
        if not is_admin:
            email = user_new_data["email"]
            if user_id != current_user:
                return {"error": "Unauthorized action."}
            if (
                user.email != email
                or not user.verify_password(user_new_data["password"])
                or user_new_data["is_admin"]
            ):
                return {"error": "Admin privileges required"}, 403

        try:
            facade.update_user(user_id, user_new_data)
        except (TypeError, ValueError) as e:
            return {"error": str(e)}, 400

        return user.to_dict(), 200
