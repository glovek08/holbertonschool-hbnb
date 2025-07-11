from app.models.base_model import BaseModel
from app.services import facade

from sqlalchemy import Float, String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, validates, relationship


class Review(BaseModel):
    __tablename__ = "reviews"

    owner_id: Mapped[str] = mapped_column(
        String(36), ForeignKey("user.id"), nullable=False
    )
    place_id: Mapped[str] = mapped_column(
        String(36), ForeignKey("place.id"), nullable=False
    )
    rating: Mapped[Float] = mapped_column(Float, nullable=False)
    comment: Mapped[str] = mapped_column(String(500), nullable=False)

    @validates("owner_id")
    def owner_id(self, key: str, value: str):
        if not isinstance(value, str):
            raise TypeError("owner_id must be a string!")
        if not value.strip():
            raise ValueError("owner_id cannot be empty!")
        try:
            facade.get_user(value)
        except ValueError:
            raise ValueError("User does not exist!")
        return value

    @validates("place_id")
    def place_id(self, key: str, value: str) -> str:
        if not isinstance(value, str):
            raise TypeError("place_id must be a string!")
        return value

    @validates("ration")
    def rating(self, key: str, value: str):
        if not isinstance(value, (int, float)):
            raise TypeError("Rating must be a number!")
        if not (0 <= value <= 5):
            raise ValueError("Incorrect Rating value")
        return value

    @validates("comment")
    def comment(self, key: str, value: str):
        if self.validate_string(value, "comment"):
            return value

    # self.__name = self.validate_string(value, "name").isalpha()
