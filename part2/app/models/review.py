from app.models.base_model import BaseModel


class Review(BaseModel):
    def __init__(self, owner_id: str, place_id: str, rating: float, comment: str):
        super().__init__()
        self.owner_id = owner_id
        self.place_id = place_id
        self.rating = rating
        self.comment = comment

    @property
    def owner_id(self):
        return self.__owner_id

    @owner_id.setter
    def owner_id(self, value):
        if not isinstance(value, str):
            raise TypeError("owner_id must be a string!")
        self.__owner_id = value

    @property
    def place_id(self):
        return self.__place_id

    @place_id.setter
    def place_id(self, value):
        if not isinstance(value, str):
            raise TypeError("place_id must be a string!")
        self.__place_id = value

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
