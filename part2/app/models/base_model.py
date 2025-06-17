from abc import ABC, abstractmethod
import datetime
import uuid


class BaseModel(ABC):
    def __init__(self):
        self.__id = str(uuid.uuid4())
        self.__creation_date = datetime.today()
        self.__update_date = datetime.today()

    @property
    def id(self):
        return self.__id

    @property
    def creation_date(self) -> datetime:
        return self.__creation_date

    @property
    def update_date(self) -> datetime:
        return self.__update_date

    @abstractmethod
    def create(self):
        pass

    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def delete(self):
        pass
