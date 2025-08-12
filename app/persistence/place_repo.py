from app.models.place import Place
from app.persistence.repository import SQLAlchemyRepository


class PlaceRepository(SQLAlchemyRepository):
    def __init__(self):
        super().__init__(Place)

    def get_all(self, limit=None):
        query = self.model.query
        if limit:
            query = query.limit(limit)
        return query.all()

    def get_by_user_id(self, user_id):
        """Get all places owned by a specific user"""
        return self.model.query.filter(Place.owner_id == user_id).all()
