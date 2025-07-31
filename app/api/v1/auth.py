from app.services import facade
from flask_restx import Namespace, Resource, fields
from flask_jwt_extended import (
    create_access_token,
    set_access_cookies,
)

from flask import make_response

api = Namespace("auth", description="Authentication operations")

login_model = api.model(
    "Login",
    {
        "email": fields.String(required=True, description="User email"),
        "password": fields.String(required=True, description="User password"),
    },
)


@api.route("/login")
class Login(Resource):
    @api.expect(login_model)
    def post(self):
        """Authenticate user and return a JWT token in an HttpOnly cookie"""
        credentials = api.payload
        user = facade.get_user_by_email(credentials["email"])
        if not user or not user.verify_password(credentials["password"]):
            return {"error": "Invalid credentials"}, 401
        access_token = create_access_token(
            identity=str(user.id),
            additional_claims={"is_admin": user.is_admin},
        )
        response = make_response({"access_token": access_token}, 200)
        set_access_cookies(response, access_token)
        return response
