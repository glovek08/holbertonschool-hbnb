from app.models.base_model import BaseModel
from app.services import facade

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, validates, relationship


class Amenity(BaseModel):

    __tablename__ = "amenities"

    name: Mapped[str] = mapped_column(String(100), nullable=False, unique=True)
    description: Mapped[str] = mapped_column(String(500), nullable=True)
    places = relationship(
        secondary=place_amenities, back_populates="amenities", overlaps="places"
    )

    @validates("name")
    def name(self, key: str, value: str):
        value = super().validate_string(value, "Name")
        return value

    @validates("description")
    def description(self, key: str, value: str):
        if not isinstance(value, str):
            raise TypeError("Description must be a string!")
        return value
