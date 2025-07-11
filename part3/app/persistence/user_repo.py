from app.models.user import User
from app.persistence.repository import SQLAlchemyRepository


class UserRepository(SQLAlchemyRepository):
    def __init__(self):
        super().__init__(User)

    # might throw typing error in that case
    # add Optional[User] and import Optional from typing
    def get_user_by_email(self, email):
        return self.model.query.filter_by(email=email).first()
