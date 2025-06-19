from typing import Optional
from base_model import BaseModel
from user import User


class Place(BaseModel):
    def __init__(
        self,
        owner: User,
        title: str,
        description: str = "n/a",
        price: float,
        latitude: float,
        longitude: float,
        amenities: Optional[list] = None,
    ):
        self.owner = owner
        self.title = title
        self.description = description
        self.price = price
        self.latitude = latitude
        self.longitude = longitude
        self.amenities = amenities if amenities is not None else []

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
    def owner(self):
        return self.__owner
    
    @owner.setter
    def owner(self, value):
        # owner = fetch(vaule) ?
        if owner == None:
            raise 

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
    def latitude(self):
        return self.__latitude

    @coordinates.setter
    def coordinates(self, value):
        self.__longitude = value

    # Amenities
    @property
    def amenities(self):
        return self.__amenities

    @amenities.setter
    def amenities(self, value):
        if value not in self.__amenities:
            self.__amenities.add(value)
