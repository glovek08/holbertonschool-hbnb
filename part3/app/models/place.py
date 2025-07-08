from typing import Optional, List
from app.models.base_model import BaseModel
from app.models.amenity import Amenity
from app.models.user import User
from app.services import facade


class Place(BaseModel):
    def __init__(
        self,
        owner_id: str,
        title: str,
        description: str,
        price: float,
        latitude: float,
        longitude: float,
        amenities: Optional[List[Amenity]] = None,
        reviews: Optional[list] = None,
    ):
        super().__init__()
        self.owner_id = owner_id
        self.title = title
        self.description = description
        self.price = price
        self.latitude = latitude
        self.longitude = longitude
        self.amenities = amenities if amenities is not None else []
        self.reviews = reviews if reviews is not None else []

    # Owner ID
    @property
    def owner_id(self):
        return self.__owner_id

    @owner_id.setter
    def owner_id(self, value: str):
        if not isinstance(value, str):
            raise TypeError("Owner ID must be a string")
        if not value:
            raise ValueError("Owner ID cannot be empty")

        user = facade.get_user(value)
        if not user:
            raise ValueError("User does not exist")

        self.__owner_id = value

    # Title
    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, value: str):
        value = super().validate_string(value, "Title")
        if len(value) > 100:
            raise ValueError(f"Title must not exceed 100 characters.")
        self.__title = value

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
        if value <= 0:
            raise ValueError("Price must be positive")
        self.__price = float(value)

    # Latitude
    @property
    def latitude(self):
        return self.__latitude

    @latitude.setter
    def latitude(self, value: float):
        value = super().validate_number(value, "Latitude")
        if not -90 <= value <= 90:
            raise ValueError("Latitude must be between -90 and 90")
        self.__latitude = value

    # Longitude
    @property
    def longitude(self):
        return self.__longitude

    @longitude.setter
    def longitude(self, value: float):
        value = super().validate_number(value, "Longitude")
        if not -180 <= value <= 180:
            raise ValueError("Longitude must be between -180 and 180")
        self.__longitude = value

    # Amenities
    @property
    def amenities(self):
        return self.__amenities.copy()

    @amenities.setter
    def amenities(self, value: list):
        if not isinstance(value, list):
            raise TypeError("Amenities must be a list")

        amenity_objs = []
        for amenity_id in value:
            amenity = facade.get_amenity(amenity_id)
            if amenity:
                amenity_objs.append(amenity)

        self.__amenities = amenity_objs.copy()

    def add_amenity(self, amenity: Amenity):
        """Add an amenity to the place"""
        if not isinstance(amenity, Amenity):
            raise TypeError("Value must be an Amenity")
        if amenity not in self.__amenities:
            self.__amenities.append(amenity)

    def remove_amenity(self, amenity):
        """Remove an amenity from the place"""
        if amenity in self.__amenities:
            self.__amenities.remove(amenity)

    @property
    def reviews(self):
        return self.__reviews.copy()

    @reviews.setter
    def reviews(self, value: list):
        if not isinstance(value, list):
            raise TypeError("Reviews must be a list")
        self.__reviews = value

    def add_review(self, review):
        if review not in self.__reviews:
            self.__reviews.append(review)

    def remove_review(self, review):
        if review in self.__reviews:
            self.__reviews.remove(review)
