from app.persistence.repository import InMemoryRepository


class HBnBFacade:
    def __init__(self):
        self.user_repo = InMemoryRepository()
        self.place_repo = InMemoryRepository()
        self.amenity_repo = InMemoryRepository()
        self.review_repo = InMemoryRepository()

    # **************** USER CRAP *****************
    def create_user(self, user_data):
        from app.models.user import User

        user = User(**user_data)
        self.user_repo.add(user)
        return user

    def get_user(self, user_id):
        user = self.user_repo.get(user_id)
        if not user:
            raise ValueError("User not found")
        return user

    def get_all_users(self):
        return self.user_repo.get_all()

    def get_user_by_email(self, email):
        return self.user_repo.get_by_attribute("email", email)

    def update_user(self, user_id, user_data):
        self.user_repo.update(user_id, user_data)

    # ************* PLACE CRAP ********************
    def create_place(self, place_data):
        from app.models.place import Place

        # add validation for existance of user.
        amenity_objs = []
        for amenity_id in place_data.get("amenities", []):
            amenity = self.get_amenity(amenity_id)
            if amenity:
                amenity_objs.append(amenity)
        place_data["amenities"] = amenity_objs

        place = Place(**place_data)
        self.place_repo.add(place)
        return place

    def get_place(self, place_id):
        place = self.place_repo.get(place_id)
        if not place:
            raise ValueError("Place does not exist")
        return place

    def get_all_places(self):
        return self.place_repo.get_all()

    def update_place(self, place_id, place_data):
        self.get_user(place_data["owner_id"])
        self.place_repo.update(place_id, place_data)

    # ************** AMENITY CRAP ******************
    def create_amenity(self, amenity_data):
        from app.models.amenity import Amenity

        new_amenity = Amenity(**amenity_data)
        self.amenity_repo.add(new_amenity)
        return new_amenity

    def get_amenity(self, amenity_id):
        amenity = self.amenity_repo.get(amenity_id)
        if not amenity:
            # don't know how to handle outside the facade.
            raise ValueError("Amenity does not exist")
        return amenity

    def get_all_amenities(self):
        return self.amenity_repo.get_all()

    def update_amenity(self, amenity_id, amenity_data):
        amenity = self.get_amenity(amenity_id)
        self.amenity_repo.update(amenity_id, amenity_data)
        return amenity

    # *************** REVIEW CRAP *******************
    def create_review(self, review_data):
        from app.models.review import Review

        new_review = Review(**review_data)
        self.review_repo.add(new_review)
        place = self.get_place(review_data.get("place_id"))
        place.add_review(new_review)
        return new_review

    def get_review(self, review_id):
        review = self.review_repo.get(review_id)
        if not review:
            raise ValueError("Review does not exist")
        return review

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
        self.get_review(review_id)
        self.review_repo.delete(review_id)
