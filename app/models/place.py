# fmt: off
from app.extensions import db
from app.models.base_model import BaseModel
from app.services import facade
# If problems arise, try importing models.
# from app.models.amenity import Amenity
# from app.models.review import Review
# from app.models.user import User
from typing import Optional, List
from sqlalchemy import Float, String, ForeignKey, Table, Column, Text, Integer
from sqlalchemy.orm import Mapped, mapped_column, validates, relationship

"""
August 8, 2025.
SQLAlchemy model for the Place entity in the HBnB application.

Represents a rental place with attributes such as title, image, description, price,
location (latitude and longitude), and relationships to amenities, reviews, and owner.

Relationships:
    - Many-to-many with Amenity via place_amenities association table.
    - One-to-many with Review.
    - Many-to-one with User (owner).

Includes validation for all fields and a property for calculating the average rating.

Attributes:
    owner_id (str): ID of the user who owns the place.
    title (str): Title of the place.
    image (str): URL of the place's image.
    image_author (str): Author of the image.
    description (str): Description of the place.
    price (float): Price per day.
    latitude (float): Latitude coordinate.
    longitude (float): Longitude coordinate.
    amenities (List[Amenity]): Amenities available at the place.
    reviews (List[Review]): Reviews for the place.
    owner (User): The user who owns the place.

Author: Federico Paganini, Gabriel Barn.
"""


# Table Many-to-many relationship.
# Many Amenities can have many Places,
# Many Places can have many Amenities.
place_amenities = Table(
    "place_amenities",
    db.metadata,
    Column("place_id", ForeignKey("places.id"), primary_key=True),
    Column("amenity_id", ForeignKey("amenities.id"), primary_key=True)
)

class Place(BaseModel):
    __tablename__ = "places"

    owner_id:    Mapped[str] = mapped_column(
        String(36), ForeignKey("users.id"), nullable=False
    )
    title:       Mapped[str] = mapped_column(String(100), nullable=False)
    image:       Mapped[str] = mapped_column(String(300), nullable=False)
    image_author: Mapped[str] = mapped_column(String(45), nullable=False)
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    price:       Mapped[float] = mapped_column(Float, nullable=False)
    latitude:    Mapped[float] = mapped_column(Float, nullable=False)
    longitude:   Mapped[float] = mapped_column(Float, nullable=False)
    
    # Relationships
    amenities: Mapped[List["Amenity"]] = relationship(
        "Amenity",
        secondary = place_amenities,
        back_populates = "places",
        lazy="selectin",
        overlaps = "places",
    )
    reviews: Mapped[List["Review"]] = relationship(
        "Review",
        back_populates='place',
        cascade="all, delete-orphan"
    )
    owner: Mapped["User"] = relationship(
        "User",
        back_populates="places",
        lazy="joined"
    )

    # OWNER ID
    @validates("owner_id")
    def validate_owner_id(self, key: str, value: str):
        if not isinstance(value, str):
            raise TypeError("Owner ID must be a string")
        if not value:
            raise ValueError("Owner ID cannot be empty")
        return value


    # TITLE
    @validates("title")
    def validate_title(self, key: str, value: str):
        value = super().validate_string(value, "Title")
        if len(value) > 100:
            raise ValueError(f"Title must not exceed 100 characters.")
        return value

    # PLACE IMAGE
    @validates("image")
    def validate_image(self, key: str, value: str):
        value = super().validate_string(value, "Image")
        if len(value) > 300:
            raise ValueError(f"Image source must not exceed 300 characters.")
        return value

    # DESCRIPTION
    @validates("description")
    def validate_description(self, key: str, value: Optional[str]):
        if not isinstance(value, str):
            raise TypeError("Description must be a string")
        return value.strip()


    # PRICE
    @validates("price")
    def validate_price(self, key: str, value: float):
        if not isinstance(value, (int, float)):
            raise TypeError("Price must be a number")
        if value <= 0:
            raise ValueError("Price must be positive")
        return float(value)


    # LATITUDE
    @validates("latitude")
    def validate_latitude(self, key: str, value: float):
        value = super().validate_number(value, "Latitude")
        if not -90 <= value <= 90:
            raise ValueError("Latitude must be between -90 and 90")
        return value


    # LONGITUDE
    @validates("longitude")
    def validate_longitude(self, key: str, value: float):
        value = super().validate_number(value, "Longitude")
        if not -180 <= value <= 180:
            raise ValueError("Longitude must be between -180 and 180")
        return value


    @property
    def average_rating(self):
        if not self.reviews:
            return 0
        return sum(review.rating for review in self.reviews) / len(self.reviews)

    def to_dict(self):
        data = super().to_dict()
        data.update(
            owner_id=self.owner_id,
            owner={
                "first_name": self.owner.first_name,
                "last_name": self.owner.last_name
            } if self.owner else None,
            title=self.title,
            image=self.image,
            description=self.description,
            price=self.price,
            latitude=self.latitude,
            longitude=self.longitude,
            rating=self.average_rating,
            amenities=[
            {
                "id": amenity.id,
                "name": amenity.name,
                "description": amenity.description
            } for amenity in self.amenities
            ] if self.amenities else []
        )
        return data

    def __repr__(self):
        return f"<Place name={self.title!r}, id={self.id}>"
