from base_model import BaseModel

class Amenity(BaseModel):
    def __init__(self, id_amenity: str, name: str = "n/a", description: str = "n/a"):
        self.__id_amenity = id_amenity
        self.__name = name
        self.__description = description


    def create(self, id_amenity):
        pass
    def update(self, id_amenity):
        pass
    def delete(self):
        pass