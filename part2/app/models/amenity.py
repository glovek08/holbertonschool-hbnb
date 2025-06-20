from app.models.base_model import BaseModel


class Amenity(BaseModel):
    def __init__(self, id_amenity: str, name: str = "n/a", description: str = "n/a"):
        self.id_amenity = id_amenity
        self.name = name
        self.description = description
        # self.__icon = icon

    @property
    def id_amenity(self):
        return self.__id_amenity

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value: str):
        if not isinstance(value, str) or None:
            raise TypeError("Name must be a string!")
        self.__name = value

    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, value: str):
        if not isinstance(value, str):
            raise TypeError("Description must be a string!")
        self.__description = value

    def update(self, id_amenity):
        pass

    # def __del__(self):
    #    erase_db(self.__dict__)
