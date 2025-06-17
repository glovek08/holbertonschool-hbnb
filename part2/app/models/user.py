from base_model import BaseModel


class User(BaseModel):
    def __init__(
        self,
        first_name: str = "n/a",
        last_name: str = "n/a",
        email: str = "n/a",
        password: str = "n/a",
        is_admin: bool = False,
    ):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__email = email
        self.__password = password
        self.__is_admin = is_admin

    # First Name
    @property
    def first_name(self):
        return self.__first_name

    @first_name.setter
    def first_name(self, value):
        if not isinstance(value, str) or None:
            raise TypeError("First Name must be a string!")
        self.__first_name = value

    # Last Name
    @property
    def last_name(self):
        return self.__last_name

    @last_name.setter
    def last_name(self, value):
        if not isinstance(value, str) or None:
            raise TypeError("Last Name must be a string!")
        self.__last_name = value

    # Email
    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, value):
        if not isinstance(value, str) or None:
            raise TypeError("Email must be a string!")
        self.__email = value

    # Password
    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, value):
        # use werkzug.security for password hash here??
        if not isinstance(value, str) or None:
            raise TypeError("Password must be a string!")
        self.__password = value

    # Is Admin
    @property
    def is_admin(self):
        return self.__is_admin

    @is_admin.setter
    def is_admin(self, value: bool):
        # Since is admin is either true or false, should be handled differently?
        if not isinstance(value, bool):
            raise TypeError("Is Admin must be Bool!")
        self.__is_admin = bool(value)
        # Maybe wrap this ^ in try-except block
