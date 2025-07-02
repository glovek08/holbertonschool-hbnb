# from werkzeug.security import generate_password_hash, check_password_hash
# from email_validator import validate_email, EmailNotValidError
import re
from datetime import datetime
from app.models.base_model import BaseModel


class User(BaseModel):
    def __init__(
        self,
        first_name: str,
        last_name: str,
        email: str,
        password: str,
        is_admin: bool = False,
    ):
        super().__init__()
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.is_admin = is_admin

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
    @property
    def first_name(self):
        return self.__first_name

    @first_name.setter
    def first_name(self, value):
        self.__first_name = self.validate_string(value, "First Name")

    # Last Name
    @property
    def last_name(self):
        return self.__last_name

    @last_name.setter
    def last_name(self, value):
        self.__last_name = self.validate_string(value, "Last Name")

    # Email
    @property
    def email(self):
        return self.__email

    # @email.setter
    # def email(self, value):
    #     try:
    #         valid = validate_email(value, check_deliverability=True)
    #         self.__email = valid.email.lower()
    #     except EmailNotValidError as e:
    #         raise ValueError(f"Invalid email: {e}")
    @email.setter
    def email(self, value):
        if not isinstance(value, str):
            raise TypeError("Email must be a string")
        email_pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
        if not re.match(email_pattern, value):
            raise ValueError("Invalid email format")

        self.__email = value.lower().strip()

    # Password
    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, value):
        if not isinstance(value, str):
            raise TypeError("Password must be a string!")
        self.__password = bcrypt.generate_password_hash(value).decode("utf-8")

    def hash_password(self, password):
        """Hashes the password before storing it."""
        self.password = bcrypt.generate_password_hash(password).decode("utf-8")

    def verify_password(self, password):
        """Verifies if the provided password matches the hashed password."""
        return bcrypt.check_password_hash(self.password, password)

    # Is Admin
    @property
    def is_admin(self):
        return self.__is_admin

    @is_admin.setter
    def is_admin(self, value: bool):
        if not isinstance(value, bool):
            raise TypeError("Is Admin must be a boolean!")
        self.__is_admin = value

    def to_dict(self):
        data = super().export_data()
        data.update(
            first_name=self.first_name,
            last_name=self.last_name,
            email=self.email,
            is_admin=str(self.is_admin),
        )
        return data
