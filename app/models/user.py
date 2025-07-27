# fmt: off
from email_validator import validate_email, EmailNotValidError
from app.models.base_model import BaseModel
from app.extensions import bcrypt
from typing import List

# SQLAlchemy stuff
from sqlalchemy import String, Boolean
from sqlalchemy.orm import Mapped, mapped_column, validates, relationship


class User(BaseModel):
    __tablename__ = "users"

    first_name: Mapped[str] = mapped_column(String(50), nullable=False)
    last_name:  Mapped[str] = mapped_column(String(50), nullable=False)
    email:      Mapped[str] = mapped_column(String(254), nullable=False, unique=True)
    password:   Mapped[str] = mapped_column(String(60), nullable=False)
    is_admin:   Mapped[bool] = mapped_column(Boolean, nullable=False, default=False)
    places:     Mapped[List["Place"]] = relationship(back_populates="owner", cascade="all, delete-orphan")
    reviews:    Mapped[List["Review"]] = relationship(back_populates="user", cascade="all, delete-orphan")

    def validate_string(self, value, field_name):
        value = super().validate_string(value, field_name)
        if field_name in ("First Name", "Last Name"):
            if not value.isalpha():
                raise ValueError(f"{field_name} is not a valid name")
            if len(value) > 50:
                raise ValueError(f"{field_name} must not exceed 50 characters.")
        return value

    # FIRST NAME
    @validates("first_name")
    def validate_first_name(self, key: str, value: str):
        return self.validate_string(value, "First Name")

    # LAST NAME
    @validates("last_name")
    def validate_last_name(self, key: str, value: str):
        return self.validate_string(value, "Last Name")

    # EMAIL
    @validates("email")
    def validate_new_email(self, key: str, value: str):
        try:
            valid = validate_email(value, check_deliverability=True)
        except EmailNotValidError as e:
            raise ValueError(f"Invalid email: {e}")

        return valid.email.lower()

    # PASSWORD
    @validates("password")
    def validate_password(self, key: str, value: str):
        if not isinstance(value, str):
            raise TypeError("Password must be a string!")
        return bcrypt.generate_password_hash(value).decode("utf-8")

    # PASSWORD
    def verify_password(self, password: str):
        """Verifies if the provided password matches the hashed password."""
        return bcrypt.check_password_hash(self.password, password)

    # IS ADMIIN
    @validates("is_admin")
    def validate_is_admin(self, key: str, value: bool):
        if not isinstance(value, bool):
            raise TypeError("Is Admin must be a boolean!")
        return value

    def to_dict(self):
        data = super().to_dict()
        data.update(
            first_name=self.first_name,
            last_name=self.last_name,
            email=self.email,
            is_admin=self.is_admin,
        )
        return data

    def __repr__(self):
        return f"<User name={self.first_name!r}, email={self.email!r}>"
