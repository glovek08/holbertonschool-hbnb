from app.models.base_model import BaseModel
from app.services import facade
from typing import List
from sqlalchemy import String, Text
from sqlalchemy.orm import Mapped, mapped_column, validates, relationship

# If circular import arises, import places inside Amenity.
from app.models.place import place_amenities

"""
August 8, 2025.
SQLAlchemy model for the Amenity entity in the HBnB application.

Represents an amenity that can be associated with one or more places.
Includes validation for name and description fields, and supports a many-to-many
relationship with the Place model via the place_amenities association table.

Attributes:
    name (str): The name of the amenity (unique, required).
    description (str): A description of the amenity (optional).
    icon (str): An optional icon representing the amenity.
    places (List[Place]): List of places associated with this amenity.

Author: Federico Paganini, Gabriel Barn
"""


class Amenity(BaseModel):

    __tablename__ = "amenities"

    name: Mapped[str] = mapped_column(String(100), nullable=False, unique=True)
    description: Mapped[str] = mapped_column(Text, nullable=True)
    icon: Mapped[str] = mapped_column(String(100), nullable=True)
    places: Mapped[List["Place"]] = relationship(
        "Place",
        secondary=place_amenities,
        back_populates="amenities",
        overlaps="amenities",
    )

    # NAME
    @validates("name")
    def validate_name(self, key: str, value: str):
        value = super().validate_string(value, "Name")
        return value

    # DESCRIPTION
    @validates("description")
    def validate_description(self, key: str, value: str):
        if not isinstance(value, str):
            raise TypeError("Description must be a string!")
        return value

    # def to_dict(self):
    #     data = super().to_dict()
    #     data.update(
    #         name=self.name,
    #         description=self.description,
    #     )
    #     return data

    def __repr__(self):
        return f"<Amenity id={self.id} name={self.name!r}>"
