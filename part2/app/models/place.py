from base_model import BaseModel

class Place(BaseModel):
    def __init__(self, id_place: str, title: str="n/a",
                description: str="n/a",
                price: float=0.00,
                longitude: tuple=(0, 0),
                amenities: list=None):
        self.__id_place = id_place
        self.__title = title
        self.__description = description
        self.__price = price
        self.__longitude = longitude
        self.__amenities = amenities if amenities is not None else []
