from base_model import BaseModel


class User(BaseModel):
    def __init__(self, id_user: str,
                 first_name: str = "n/a",
                 last_name: str = "n/a",
                 email: str = "n/a",
                 password: str = "n/a",
                 is_admin: bool = False):
        pass # for now

    
    def create(self, id_user):
        pass
    def update(self, id_user):
        pass
    def delete():
        pass
