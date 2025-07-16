from app.models.base_model import BaseModel
from app.services import facade


from sqlalchemy import String, Text
from sqlalchemy.orm import Mapped, mapped_column, validates, relationship

# If circular import arises, import places inside Amenity.
from app.models.place import place_amenities


class Amenity(BaseModel):

    __tablename__ = "amenities"

    name: Mapped[str] = mapped_column(String(100), nullable=False, unique=True)
    description: Mapped[str] = mapped_column(Text, nullable=True)

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

    def to_dict(self):
        data = super().to_dict()
        data.update(
            name=self.name,
            description=self.description,
        )
        return data

    def __repr__(self):
        return f"<Amenity id={self.id} name={self.name!r}>"
