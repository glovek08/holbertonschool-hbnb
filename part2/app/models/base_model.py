from abc import ABC, abstractmethod
from datetime import datetime
import uuid


class BaseModel(ABC):
    def __init__(self):
        self._id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    @staticmethod
    def validate_string(value, field_name):
        if not isinstance(value, str):
            raise TypeError(f"{field_name} must be a string!")
        value = value.strip()
        if len(value) == 0:
            raise ValueError(f"{field_name} cannot be empty!")
        return value

    @staticmethod
    def validate_number(value, field_name):
        if type(value) is not int and type(value) is not float:
            raise TypeError(f"{field_name} must be a number!")
        return float(value)  # Return float to prevent loss of shit.

    @property
    def id(self):
        return self._id

    def save(self):
        """Update the updated_at timestamp whenever the object is modified"""
        self.updated_at = datetime.now()

    def update(self, data: dict):
        for key, value in data.items():
            if hasattr(self, key) and key not in ["id", "created_at"]:
                current_value = getattr(self, key)
                if current_value != value:
                    setattr(self, key, value)
        self.save()

    def export_data(self):
        data = {
            "id": self.id,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
        }
        return data
