from typing import Optional
from base_model import BaseModel


class Place(BaseModel):
    def __init__(
        self,
        id_owner: str,
        title: str = "n/a",
        description: str = "n/a",
        price: float = 0.00,
        coordinates: Optional[tuple] = None,
        amenities: Optional[list] = None,
    ):
        self.__id_owner = id_owner
        self.__title = title
        self.__description = description
        self.__price = price
        self.__coordinates = coordinates
        self.__amenities = amenities if amenities is not None else []

    # new_place.update(option, value)
    #     if hasattr(self, option):
    #         setattr(self, option, value)
    #     if (option == "description")
    #         new_place.description == value
    #     elif option == "title":
    #         self.title = value

    # def set_id(self, value):
    #     self.__id_place = value

    @property
    def id_owner(self):
        return self.__id_owner

    # Title
    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, value: str):
        if not isinstance(value, str) or None:
            raise TypeError("Title must be a string!")
        self.__title = value

    # Description
    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, value):
        self.__description = value

    # Price
    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        self.__price = value

    # Coordinates
    @property
    def coordinates(self):
        return self.__coordinates

    @coordinates.setter
    def coordinates(self, value):
        self.__coordinates = value

    # Amenities
    @property
    def amenities(self):
        return self.__amenities

    @amenities.setter
    def amenities(self, value):
        self.__amenities = value
