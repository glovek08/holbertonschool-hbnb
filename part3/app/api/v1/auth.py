from flask_restx import Namespace, Resource, fields
from flask_jwt_extended import create_access_token
from app.services import facade
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_jwt_extended import get_jwt

api = Namespace("auth", description="Authentication operations")

# Model for input validation
login_model = api.model(
    "Login",
    {
        "email": fields.String(required=True, description="User email"),
        "password": fields.String(required=True, description="User password"),
    },
)


@api.route("/protected")
class ProtectedResource(Resource):
    @jwt_required()
    def get(self):
        """A protected endpoint that requires a valid JWT token"""
        current_user_id = get_jwt_identity()
        claims = get_jwt()
        is_admin = claims.get("is_admin", False)

        return {"message": f"Hello, user {current_user_id}", "is_admin": is_admin}, 200


@api.route("/login")
class Login(Resource):
    @api.expect(login_model)
    def post(self):
        """Authenticate user and return a JWT token"""
        credentials = api.payload
        user = facade.get_user_by_email(credentials["email"])
        if not user or not user.verify_password(credentials["password"]):
            return {"error": "Invalid credentials"}, 401
        access_token = create_access_token(
            identity=str(user.id),
            additional_claims={"is_admin": user.is_admin},
        )
        return {"access_token": access_token}, 200
