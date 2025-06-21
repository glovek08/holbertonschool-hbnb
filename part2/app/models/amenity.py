from app.models.base_model import BaseModel


class Amenity(BaseModel):
    def __init__(self, name: str = "n/a", description: str = "n/a"):
        super().__init__()
        self.name = name
        self.description = description
        # self.__icon = icon

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value: str):
        if not isinstance(value, str):
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
