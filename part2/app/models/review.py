from base_model import BaseModel

class Review(BaseModel):
    def __init__(self, id_review: str, rating: int=0, comment: str="n/a"):
        self.__id_review = id_review
        self.__rating = rating
        self.__comment = comment