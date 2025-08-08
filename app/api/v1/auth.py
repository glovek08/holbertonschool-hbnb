from urllib import response
from app.services import facade
from flask_restx import Namespace, Resource, fields
from datetime import timedelta
from flask import make_response
from flask_jwt_extended import (
    create_access_token,
    jwt_required,
    set_access_cookies,
    unset_jwt_cookies,
    get_jwt_identity,
)

"""
August 8, 2025.
API endpoints for authentication in the HBnB application.

This module provides endpoints to:
- Log in a user and set a JWT token in an HttpOnly cookie.
- Log out a user and clear authentication cookies.
- Check if a user is currently authenticated.

Endpoints:
    POST   /api/v1/auth/login         - Authenticate user and set JWT cookie
    POST   /api/v1/auth/logout        - Log out user and clear cookies
    POST   /api/v1/auth/check_status  - Check if user is authenticated
"""


api = Namespace("auth", description="Authentication operations")

login_model = api.model(
    "Login",
    {
        "email": fields.String(required=True, description="User email"),
        "password": fields.String(required=True, description="User password"),
        "stay_logged": fields.Boolean(
            required=False, description="User checks 'Stay Logged In'"
        ),
    },
)


@api.route("/login")
@api.doc(response={401: "Invalid credentials"})
@api.doc(response={200: "Access token created"})
class Login(Resource):
    @api.expect(login_model)
    def post(self):
        """Authenticate user and return a JWT token in an HttpOnly cookie"""
        credentials = api.payload
        user = facade.get_user_by_email(credentials["email"])
        if not user or not user.verify_password(credentials["password"]):
            return {"error": "INVALID CREDENTIALS"}, 401

        if credentials.get("stay_logged"):
            expires = timedelta(days=30)
            access_token = create_access_token(
                identity=str(user.id),
                additional_claims={"is_admin": user.is_admin},
                expires_delta=expires,
            )
            response = make_response(
                {"id": str(user.id), "access_token": access_token}, 200
            )
            set_access_cookies(
                response,
                access_token,
                max_age=int(expires.total_seconds()),
            )
            print("Stay Logged In")
            return response
        else:
            access_token = create_access_token(
                identity=str(user.id),
                additional_claims={"is_admin": user.is_admin},
                # expires_delta=timedelta(minutes=15), if shit gets wild uncomment.
            )
            response = make_response(
                {"id": str(user.id), "access_token": access_token}, 200
            )
            set_access_cookies(response, access_token)
            print("Session Log In.")
            return response


@api.route("/logout")
@api.doc(response={200: "Logout successful"})
class Logout(Resource):
    def post(self):
        """Logout authenticated user and clean cookies"""
        response = make_response({"msg": "Logout successful"}, 200)
        unset_jwt_cookies(response)

        # Cross-site request forgery? maybe later :D
        response.set_cookie(
            "csrf_access_token", "", expires=0, path="/", samesite="Lax"
        )

        response.set_cookie(
            "access_token_cookie",
            "",
            expires=0,
            path="/",
            httponly=True,
            samesite="Lax",
        )
        return response


@api.route("/check_status")
@api.doc(response={200: "User logged in"})
class CheckStatus(Resource):
    @jwt_required()
    def post(self):
        """Checks if the user is already logged in"""
        user_id = get_jwt_identity()
        return {"msg": "User logged in", "user": {"id": user_id}}, 200
