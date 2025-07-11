# from app.persistence.repository import InMemoryRepository # Uncomment to use in-memory repository for testing purporses.
from app.persistence.repository import SQLAlchemyRepository
from app.persistence.user_repo import UserRepository
from app.models.user import User
from app.models.review import Review
from app.models.place import Place
from app.models.amenity import Amenity


class HBnBFacade:
    def __init__(self):
        self.user_repo = UserRepository(User)
        self.place_repo = SQLAlchemyRepository(Place)
        self.amenity_repo = SQLAlchemyRepository(Amenity)
        self.review_repo = SQLAlchemyRepository(Amenity)

    # ************ IN-MEMORY REPO ******************
    # self.user_repo = InMemoryRepository()
    # self.place_repo = InMemoryRepository()
    # self.amenity_repo = InMemoryRepository()
    # self.review_repo = InMemoryRepository()

    # **************** USER DATA MANAGEMENT *****************
    def create_user(self, user_data):
        # from app.models.user import User ***** IF RANDOM ERROR OCCURS, UNCOMMENT THIS AND IMPORT EACH MODEL INSIDE LOCAL SCOPE. ****

        user = User(**user_data)
        self.user_repo.add(user)
        return user

    def get_user(self, user_id):
        return self.user_repo.get(user_id)

    def get_all_users(self):
        return self.user_repo.get_all()

    def get_user_by_email(self, email):
        return self.user_repo.get_by_attribute("email", email)

    def update_user(self, user_id, user_data):
        self.user_repo.update(user_id, user_data)

    # ************* PLACE DATA MANAGEMENT ********************
    def create_place(self, place_data):
        from app.models.place import Place

        place = Place(**place_data)
        self.place_repo.add(place)
        return place

    def get_place(self, place_id):
        return self.place_repo.get(place_id)

    def get_all_places(self):
        return self.place_repo.get_all()

    def update_place(self, place_id, place_data):
        self.place_repo.update(place_id, place_data)

    def delete_place(self, place_id):
        self.place_repo.delete(place_id)

    # ************** AMENITY DATA MANAGEMENT ******************
    def create_amenity(self, amenity_data):
        from app.models.amenity import Amenity

        new_amenity = Amenity(**amenity_data)
        self.amenity_repo.add(new_amenity)
        return new_amenity

    def get_amenity(self, amenity_id):
        return self.amenity_repo.get(amenity_id)

    def get_all_amenities(self):
        return self.amenity_repo.get_all()

    def update_amenity(self, amenity_id, amenity_data):
        self.amenity_repo.update(amenity_id, amenity_data)

    # *************** REVIEW DATA MANAGEMENT *******************
    def create_review(self, review_data):
        from app.models.review import Review

        new_review = Review(**review_data)
        self.review_repo.add(new_review)
        place = self.get_place(review_data.get("place_id"))
        place.add_review(new_review)  # type: ignore
        return new_review

    def get_review(self, review_id):
        return self.review_repo.get(review_id)

    def get_all_reviews(self):
        return self.review_repo.get_all()

    def get_reviews_by_place(self, place_id):
        return self.place_repo.get(place_id).reviews  # type: ignore

    def update_review(self, review_id, review_data):
        self.review_repo.update(review_id, review_data)

    def delete_review(self, review_id):
        self.review_repo.delete(review_id)

    def get_review_of_place_by_author(self, author_id, place_id):
        return self.review_repo.get_by_attribute("owner_id", author_id)
