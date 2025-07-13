from app.models.base_model import BaseModel
from app.services import facade


from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, validates, relationship


# test_stuff
from typing import List, TYPE_CHECKING
from app.models.place import place_amenities


class Amenity(BaseModel):

    __tablename__ = "amenities"

    name: Mapped[str] = mapped_column(String(100), nullable=False, unique=True)
    description: Mapped[str] = mapped_column(String(500), nullable=True)
    # if TYPE_CHECKING:
    #   from app.models.place import Place    If circular import put again.
    places: Mapped[List["Place"]] = relationship(
        "Place",
        secondary=place_amenities,
        back_populates="amenities",
        overlaps="amenities",
    )

    # NAME
    @validates("name")
    def name(self, key: str, value: str):
        value = super().validate_string(value, "Name")
        return value

    # DESCRIPTION
    @validates("description")
    def description(self, key: str, value: str):
        if not isinstance(value, str):
            raise TypeError("Description must be a string!")
        return value

    def __repr__(self):
        return f"<Amenity id={self.id} name={self.name!r}>"
