# fmt: off
from app.models.base_model import BaseModel
from app.models.user import User
from app.services import facade
from typing import (
    Optional,
    List,
)  # For type hints, will probably be removed after sqlalchemy

# SQLAlchemy crap.
from sqlalchemy import Float, String, ForeignKey, Table, Column
from sqlalchemy.orm import Mapped, mapped_column, validates, relationship

#test_stuff
from app.extensions import db

place_amenities = Table(
    "place_amenities",
    db.metadata,
    Column("place_id", ForeignKey("place.owner_id"), primary_key=True),
    Column("amenity_id", ForeignKey("amenity.id"), primary_key=True)
)


class Place(BaseModel):
    __tablename__ = "places"

    owner_id: Mapped[str] = mapped_column(
        String(36), ForeignKey("user.id"), nullable=False
    )
    title:       Mapped[str] = mapped_column(String(100), nullable=False)
    description: Mapped[str] = mapped_column(String(500), nullable=True)
    price:       Mapped[float] = mapped_column(Float, nullable=False)
    latitude:    Mapped[float] = mapped_column(Float, nullable=False)
    longitude:   Mapped[Float] = mapped_column(Float, nullable=False)
    amenities = relationship(
        secondary= place_amenities, back_populates="places", overlaps="amenities"
    )
    # revies:     Mapped[List["Review"]] = relationship(
    #     secondary= place_reviews, back_populates="review"
    # )
    

    # def __init__(
    #     self,
    #     # owner_id: str,
    #     title: str,
    #     description: str,
    #     price: float,
    #     latitude: float,
    #     longitude: float,
    #     amenities: Optional[List[Amenity]] = None,
    #     reviews: Optional[list] = None,
    # ):
    #     super().__init__()
    #     self.owner_id = owner_id
    #     self.title = title
    #     self.description = description
    #     self.price = price
    #     self.latitude = latitude
    #     self.longitude = longitude
    #     self.amenities = amenities if amenities is not None else []
    #     self.reviews = reviews if reviews is not None else []

    # OWNER ID
    # @property
    # def owner_id(self):
    #     return self.__owner_id

    @validates("owner_id")
    def owner_id(self, value: str):
        if not isinstance(value, str):
            raise TypeError("Owner ID must be a string")
        if not value:
            raise ValueError("Owner ID cannot be empty")

        user = facade.get_user(value)
        if not user:
            raise ValueError("User does not exist")

        return value # shouldn we return the value, since owner id is handled by the ORM now.
        # self.__owner_id = value

    # TITLE
    # @property
    # def title(self):
    #     return self.__title

    @validates("title")
    def title(self, value: str):
        value = super().validate_string(value, "Title")
        if len(value) > 100:
            raise ValueError(f"Title must not exceed 100 characters.")
        return value

    # DESCRIPTION
    # @property
    # def description(self):
    #     return self.__description

    @validates("description")
    def description(self, value: str):
        if not isinstance(value, str):
            raise TypeError("Description must be a string")
        return value.strip()

    # PRICE
    # @property
    # def price(self):
    #     return self.__price

    @validates("price")
    def price(self, value: float):
        if not isinstance(value, (int, float)):
            raise TypeError("Price must be a number")
        if value <= 0:
            raise ValueError("Price must be positive")
        return float(value)

    # LATITUDE
    # @property
    # def latitude(self):
    #     return self.__latitude

    @validates("latitude")
    def latitude(self, value: float):
        value = super().validate_number(value, "Latitude")
        if not -90 <= value <= 90:
            raise ValueError("Latitude must be between -90 and 90")
        return value

    # LONGITUDE
    # @property
    # def longitude(self):
    #     return self.__longitude

    @validates("longitude")
    def longitude(self, value: float):
        value = super().validate_number(value, "Longitude")
        if not -180 <= value <= 180:
            raise ValueError("Longitude must be between -180 and 180")
        return value

    # AMENITIES
    # @property
    # def amenities(self):
    #     return self.__amenities.copy()

    @validates("amenities")
    def amenities(self, value: list):
        if not isinstance(value, list):
            raise TypeError("Amenities must be a list")

        amenity_objs = []
        for amenity_id in value:
            amenity = facade.get_amenity(amenity_id)
            if amenity:
                amenity_objs.append(amenity)

        return amenity_objs
        # self.__amenities = amenity_objs.copy()

    # def add_amenity(self, amenity: Amenity):
    #     """Add an amenity to the place"""
    #     if not isinstance(amenity, Amenity):
    #         raise TypeError("Value must be an Amenity")
    #     if amenity not in self.__amenities:
    #         self.__amenities.append(amenity)

    # def remove_amenity(self, amenity):
    #     """Remove an amenity from the place"""
    #     if amenity in self.__amenities:
    #         self.__amenities.remove(amenity)

    # REVIEWS
    # @property
    # def reviews(self):
    #     return self.__reviews.copy()

    @validates("reviews")
    def reviews(self, value: list):
        if not isinstance(value, list):
            raise TypeError("Reviews must be a list")
        return value

    # def add_review(self, review):
    #     if review not in self.__reviews:
    #         self.__reviews.append(review)

    # def remove_review(self, review):
    #     if review in self.__reviews:
    #         self.__reviews.remove(review)
