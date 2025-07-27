from app.models.user import Review
from app.persistence.repository import SQLAlchemyRepository


class ReviewRepository(SQLAlchemyRepository):
    def __init__(self):
        super().__init__(Review)

    def get_reviews_by_author(self, author_id):
        return self.model.query.filter_by(owner_id=author_id).first()
