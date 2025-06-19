from typing import Optional
from base_model import BaseModel
from user import User


class Place(BaseModel):
    def __init__(
        self,
        owner: User,
        title: str,
        description: str,
        price: float,
        latitude: float,
        longitude: float,
        amenities: Optional[list] = None,
    ):
        super().__init__()
        self.owner = owner
        self.title = title
        self.description = description
        self.price = price
        self.latitude = latitude
        self.longitude = longitude
        self.amenities = amenities if amenities is not None else []

    def update(self, option: str, value):
        """Update a specific attribute of the place"""
        if hasattr(self, option):
            setattr(self, option, value)
        else:
            raise AttributeError(f"Place has no attribute '{option}'")

    # Owner
    @property
    def owner(self):
        return self.__owner

    @owner.setter
    def owner(self, value: User):
        if not isinstance(value, User):
            raise TypeError("Owner must be a User instance")
        if value is None:
            raise ValueError("Owner cannot be None")
        self.__owner = value

    # Title
    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, value: str):
        if not isinstance(value, str):
            raise TypeError("Title must be a string")
        if not value.strip():
            raise ValueError("Title cannot be empty")
        self.__title = value.strip()

    # Description
    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, value: str):
        if not isinstance(value, str):
            raise TypeError("Description must be a string")
        self.__description = value.strip()

    # Price
    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value: float):
        if not isinstance(value, (int, float)):
            raise TypeError("Price must be a number")
        if value < 0:
            raise ValueError("Price cannot be negative")
        self.__price = float(value)

    # Latitude
    @property
    def latitude(self):
        return self.__latitude

    @latitude.setter
    def latitude(self, value: float):
        if not isinstance(value, (int, float)):
            raise TypeError("Latitude must be a number")
        if not -90 <= value <= 90:
            raise ValueError("Latitude must be between -90 and 90")
        self.__latitude = float(value)

    # Longitude
    @property
    def longitude(self):
        return self.__longitude

    @longitude.setter
    def longitude(self, value: float):
        if not isinstance(value, (int, float)):
            raise TypeError("Longitude must be a number")
        if not -180 <= value <= 180:
            raise ValueError("Longitude must be between -180 and 180")
        self.__longitude = float(value)

    # Amenities
    @property
    def amenities(self):
        return self.__amenities.copy()

    @amenities.setter
    def amenities(self, value: list):
        if not isinstance(value, list):
            raise TypeError("Amenities must be a list")
        self.__amenities = value.copy()

    def add_amenity(self, amenity):
        """Add an amenity to the place"""
        if amenity not in self.__amenities:
            self.__amenities.append(amenity)

    def remove_amenity(self, amenity):
        """Remove an amenity from the place"""
        if amenity in self.__amenities:
            self.__amenities.remove(amenity)
