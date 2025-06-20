from app.persistence.respository import InMemoryRepository
from app.models.place import Place
from app.models.user import User
from app.models.amenity import Amenity
from app.models.review import Review


class HBnBFacade:
    def __init__(self):
        self.user_repo = InMemoryRepository()
        self.place_repo = InMemoryRepository()
        self.amenity_repo = InMemoryRepository()
        self.review_repo = InMemoryRepository()

    # **************** USER CRAP *****************
    def create_user(self, user_data):
        user = User(**user_data)
        self.user_repo.add(user)
        return user

    def get_user(self, user_id):
        return self.user_repo.get(user_id)

    def get_all_users(self):
        return self.user_repo.get_all()

    def get_user_by_email(self, email):
        return self.user_repo.get_by_attribute("email", email)

    # ************* PLACE CRAP ********************
    def create_place(self, place_data):
        place = Place(**place_data)
        self.place_repo.add(place)
        return place

    def get_place(self, place_id):
        return self.place_repo.get(place_id)

    def get_all_places(self):
        return self.place_repo.get_all()

    def update_place(self, place_id, place_data):
        self.place_repo.update(place_id, place_data)

    # ************** AMENITY CRAP ******************
    def create_amenity(self, amenity_data):
        new_amenity = Amenity(**amenity_data)
        self.amenity_repo.add(new_amenity)
        return new_amenity

    def get_amenity(self, amenity_id):
        return self.amenity_repo.get(amenity_id)

    def get_all_amenities(self):
        return self.amenity_repo.get_all()

    def update_amenity(self, amenity_id, amenity_data):
        self.amenity_repo.update(amenity_id, amenity_data)

    # *************** REVIEW CRAP *******************
    def create_review(self, review_data):
        user = self.get_user(review_data.get("user_id"))
        if not user:
            raise ValueError("User does not exist")
        place = self.get_place(review_data.get("place_id"))
        if not place:
            raise ValueError("Place does not exist")
        # Both ID exist. Now we create the review.
        new_review = Review(**review_data)
        self.review_repo.add(new_review)
        # add the review to its corresponding pleis
        place.add_review(new_review)
        return new_review

    def get_review(self, review_id):
        return self.review_repo.get(review_id)

    def get_all_reviews(self):
        return self.review_repo.get_all()

    def get_reviews_by_place(self, place_id):
        place = self.place_repo.get(place_id)
        if not place:
            raise ValueError("Place doesn't exist")
        return place.reviews

    def update_review(self, review_id, review_data):
        self.review_repo.update(review_id, review_data)

    def delete_review(self, review_id):
        # Placeholder for logic to delete a review
        pass
