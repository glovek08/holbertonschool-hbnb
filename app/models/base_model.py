from datetime import datetime
import uuid

# SQLAlchemy stuff
from sqlalchemy import DateTime, String
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase
from sqlalchemy.ext.declarative import as_declarative
from sqlalchemy.inspection import inspect
from app.extensions import db


@as_declarative()
class BaseModel(db.Model):
    __abstract__ = True

    id: Mapped[str] = mapped_column(
        String(36), primary_key=True, default=lambda: str(uuid.uuid4())
    )
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(
        DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
    )

    def validate_string(self, value, field_name):
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

    def update(self, data: dict):
        for key, value in data.items():
            if hasattr(self, key) and key not in ["id", "created_at"]:
                current_value = getattr(self, key)
                if current_value != value:
                    setattr(self, key, value)
                    print(f"{self.to_dict} Updated")

    def to_dict(self):
        """Serialize the model to a dictionary."""
        return {c.key: getattr(self, c.key) for c in inspect(self).mapper.column_attrs}

    def __repr__(self):
        return f"<{self.__class__.__name__} id={self.id}>"
