from app.models.base_model import BaseModel
from app.services import facade

from sqlalchemy import Float, String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, validates, relationship

# from app.models.user import User
# from app.models.place import Place


class Review(BaseModel):
    __tablename__ = "reviews"

    owner_id: Mapped[str] = mapped_column(
        String(36), ForeignKey("users.id"), nullable=False
    )
    place_id: Mapped[str] = mapped_column(
        String(36), ForeignKey("places.id"), nullable=False
    )
    rating: Mapped[Float] = mapped_column(Float, nullable=False, default=0)
    comment: Mapped[str] = mapped_column(String(500), nullable=False)

    # Relationships
    user: Mapped["User"] = relationship("User", back_populates="reviews")
    place: Mapped["Place"] = relationship("Place", back_populates="reviews")

    @validates("owner_id")
    def validate_owner_id(self, key: str, value: str):
        if not isinstance(value, str):
            raise TypeError("owner_id must be a string!")
        if not value.strip():
            raise ValueError("owner_id cannot be empty!")
        return value

    # PLACE IDD
    @validates("place_id")
    def validate_place_id(self, key: str, value: str) -> str:
        if not isinstance(value, str):
            raise TypeError("place_id must be a string!")
        return value

    # RATING
    @validates("rating")
    def validate_rating(self, key: str, value: float):
        if not isinstance(value, (int, float)):
            raise TypeError("Rating must be a number!")
        if not (0 <= value <= 5):
            raise ValueError("Incorrect Rating value")
        return value

    # COMMENT
    @validates("comment")
    def validate_comment(self, key: str, value: str):
        return self.validate_string(value, "Comment")

    def to_dict(self):
        data = super().to_dict()
        data.update(
            owner_id=self.owner_id,
            place_id=self.place_id,
            rating=self.rating,
            comment=self.comment,
            author_first_name=self.user.first_name if self.user else None,
            author_last_name=self.user.last_name if self.user else None,
        )
        return data

    def __repr__(self):
        return f"<Review author_id={self.owner_id}>"
