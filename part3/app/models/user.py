from email_validator import validate_email, EmailNotValidError
from app.models.base_model import BaseModel
from app.extensions import bcrypt

# SQLAlchemy stuff
from app import db
from sqlalchemy import String, Boolean
from sqlalchemy.orm import Mapped, mapped_column, validates


class User(db.Model, BaseModel):
    __tablename__ = "users"

    first_name: Mapped[str] = mapped_column(String(50), nullable=False)
    last_name: Mapped[str] = mapped_column(String(50), nullable=False)
    email: Mapped[str] = mapped_column(String(254), nullable=False, unique=True)
    password: Mapped[str] = mapped_column(String(60), nullable=False)
    is_admin: Mapped[bool] = mapped_column(Boolean, nullable=False, default=False)

    # max length of 50 chars.
    def validate_string(self, value, field_name):
        value = super().validate_string(value, field_name)
        if field_name == "First Name" or field_name == "Last Name":
            if not value.isalpha():
                raise ValueError(f"{field_name} is not a valid name")
            if len(value) > 50:
                raise ValueError(f"{field_name} must not exceed 50 characters.")
        return value

    # First Name
    @validates("first_name")
    def first_name(self, key, value):
        return self.validate_string(value, "First Name")

    # Last Name
    @validates("last_name")
    def last_name(self, key, value):
        return self.validate_string(value, "Last Name")

    # Email
    @validates("email")
    def email(self, key, value):
        try:
            valid = validate_email(value, check_deliverability=True)
        except EmailNotValidError as e:
            raise ValueError(f"Invalid email: {e}")

        return valid.email.lower()

    # Password
    @validates("password")
    def password(self, key, value):
        if not isinstance(value, str):
            raise TypeError("Password must be a string!")
        return bcrypt.generate_password_hash(value).decode("utf-8")

    def verify_password(self, password):
        """Verifies if the provided password matches the hashed password."""
        return bcrypt.check_password_hash(self.password, password)

    # Is Admin
    @validates("is_admin")
    def is_admin(self, key, value: bool):
        if not isinstance(value, bool):
            raise TypeError("Is Admin must be a boolean!")
        return value

    def to_dict(self):
        data = super().export_data()
        data.update(
            first_name=self.first_name,
            last_name=self.last_name,
            email=self.email,
            is_admin=self.is_admin,
        )
        return data
