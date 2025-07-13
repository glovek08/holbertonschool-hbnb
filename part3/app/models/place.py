# fmt: off
from app.models.base_model import BaseModel
from app.services import facade
from typing import Optional, List

# SQLAlchemy crap.
from sqlalchemy import Float, String, ForeignKey, Table, Column
from sqlalchemy.orm import Mapped, mapped_column, validates, relationship

from app.extensions import db


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
    description: Mapped[Optional[str]] = mapped_column(String(500), nullable=True)
    price:       Mapped[float] = mapped_column(Float, nullable=False)
    latitude:    Mapped[float] = mapped_column(Float, nullable=False)
    longitude:   Mapped[float] = mapped_column(Float, nullable=False)
    
    # Relationships
    amenities: Mapped[List["Amenity"]] = relationship(
        "Amenity",
        secondary = place_amenities,
        back_populates = "places",
        overlaps = "places",
    )
    reviews: Mapped[List["Review"]] = relationship(
        "Review",
        back_populates='place',
        cascade="all, delete-orphan"
    )
    owner: Mapped["User"] = relationship(
        "User",
        back_populates="places"
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

    def __repr__(self):
        return f"<Place name={self.title!r}, id={self.id}>"
