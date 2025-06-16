from base_model import BaseModel


class User(BaseModel):
    def __init__(self, id_user: str,
                 first_name: str = "n/a",
                 last_name: str = "n/a",
                 email: str = "n/a",
                 password: str = "n/a",
                 is_admin: bool = False):
        self.__id_user = id_user
        self.__first_name = first_name
        self.__last_name = last_name
        self.__email = email
        self.__password = password
        self.__is_admin = is_admin


    def create(self, id_user):
        pass
    def update(self, id_user):
        pass
    def delete():
        pass
