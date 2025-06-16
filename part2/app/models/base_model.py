from abc import ABC

class BaseModel(ABC):
    @property
    @abstractmethod
    def creation_date(self) -> datetime:
        pass
    @property
    @abstractmethod
    def update_date(self) -> datetime:
        pass

    @abstractmethod
    def create(self):
        pass
    @abstractmethod
    def update(self):
        pass
    @abstractmethod
    def delete(self):
        pass
