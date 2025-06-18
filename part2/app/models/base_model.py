from abc import ABC, abstractmethod
from datetime import datetime
import uuid


class BaseModel(ABC):
    def __init__(self):
        self.__id = str(uuid.uuid4())
        self.__creation_date = datetime.today()
        self.__update_date = datetime.today()

    @staticmethod
    def validate_string(value, field_name):
        if not isinstance(value, str):
            raise TypeError(f"{field_name} must be a string!")
        value = value.strip()
        if len(value) == 0:
            raise ValueError(f"{field_name} cannot be empty!")
        return value

    @staticmethod
    def validate_integer(value, field_name):
        if type(value) is not int:
            raise TypeError(f"{field_name} must be an integer!")
        return float(value)  # Return float to prevent loss of shit.

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
