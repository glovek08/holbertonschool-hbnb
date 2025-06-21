from app.models.base_model import BaseModel


class Review(BaseModel):
    def __init__(self, rating: float, comment: str):
        super().__init__()
        self.rating = rating
        self.comment = comment

    @property
    def rating(self):
        return self.__rating

    @rating.setter
    def rating(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("Rating must be a number!")
        if not (0 <= value <= 5):
            raise ValueError("Incorrect Rating value")
        self.__rating = value

    @property
    def comment(self):
        return self.__comment

    @comment.setter
    def comment(self, value):
        self.__comment = self.validate_string(value, "comment")

    # self.__name = self.validate_string(value, "name").isalpha()

    def update(self, data: dict):
        """Update review attributes with new data"""
        for key, value in data.items():
            if hasattr(self, key) and key not in ["id", "created_at"]:
                setattr(self, key, value)
        self.save()
