from abc import ABC
from datetime import datetime
import uuid

# SQLAlchemy stuff
from app import db
from sqlalchemy import DateTime
from sqlalchemy.orm import Mapped, mapped_column


class BaseModel(db.Model, ABC):
    __abstract__ = True

    id: Mapped[str] = mapped_column(
        db.String(36), primary_key=True, default=lambda: str(uuid.uuid4())
    )
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(
        DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
    )
    # self._id = str(uuid.uuid4())
    # self.created_at utc= etime.now()
    # self.updated_at = datetime.now()

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

    # @property
    # def id(self):
    #     return self._id

    def save(self):
        """Update the updated_at timestamp whenever the object is modified"""
        # IF CHANGES ARE NOT MADE, USE COMMIT DELETE OTHERWISE
        self.updated_at = datetime.utcnow()

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
