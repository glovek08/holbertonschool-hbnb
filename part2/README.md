# Holberton School - hbnb (Part 2)

This project is part of the Holberton School curriculum and focuses on building the backend of an AirBnB clone. It extends the previous work by adding new features and improving the codebase.

## Authors

- [Gabriel Barnada](https://github.com/glovek08/)
- [Federico Paganin Vanoli](https://github.com/federico-paganini)

## Features

- **Data Storage:** In-memory persistance. (For Now)
- **Models:** Includes User, Place, Amenity, and Review models. All inherit from a Base Model.
- **RESTful API:** Provides endpoints for CRUD operations.
- **Web Framework:** Integrates with Flask for web-based interfaces.

## Requirements

- Ubuntu 22.04
- Python 3.8+
- pip (for installing dependencies)

## Installation

1. Clone the repository using SSH:
    ```bash
    git clone git@github.com:glovek08/holbertonschool-hbnb.git
    cd holbertonschool-hbnb/part2
    ```

2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Set up environment variables as needed (see `.env.example`).

## Usage

- **Start Web Server:**
  ```bash
  python3 app.py
  ```

## Project Structure

* The `app/` directory contains the core application code.
* The `api/` subdirectory houses the API endpoints, organized by version (v1/).
* The `models/` subdirectory contains the business logic classes (e.g., user.py, place.py).
* The `services/` subdirectory is where the Facade pattern is implemented, managing the interaction between layers.
* The `persistence/` subdirectory is where the in-memory repository is implemented. This will later be replaced by a database-backed solution using SQL Alchemy.
* `app.py` is the entry point for running the Flask application.
* `config.py` will be used for configuring environment variables and application settings.
* `requirements.txt` will list all the Python packages needed for the project.

# Business Logic Layer

The Business Logic Layer is responsible for implementing the core rules and workflows of the application. It defines the main entities and their interactions, ensuring data integrity and encapsulating the application's functionality.

## Entities

- **User:** Represents a user of the platform. Handles user-specific actions and validation (e.g., name and email format).
- **Place:** Represents a property listed on the platform. Manages attributes like location, description, price, amenities, and reviews. Provides methods to add/remove amenities and reviews.
- **Amenity:** Represents features or services available at a place (e.g., Wi-Fi, pool). Handles amenity-specific data and validation.
- **Review:** Represents user feedback for a place, including ratings and comments. Ensures ratings are within valid bounds and links reviews to both users and places.
- **BaseModel:** Abstract base class providing common attributes (e.g., `id`, `created_at`, `updated_at`) and methods for serialization and updating.

## Example Usage

```python
from app.models.user import User
from app.models.place import Place
from app.models.amenity import Amenity
from app.models.review import Review

# Create a new user
user = User(first_name="Jane", last_name="Doe", email="jane@example.com")
print(user.id, user.first_name, user.email)

# Create amenities
wifi = Amenity(name="Wi-Fi", description="Fast wireless internet")
pool = Amenity(name="Pool", description="Outdoor swimming pool")

# Create a new place
place = Place(
    owner_id=user.id,
    title="Cozy Apartment",
    description="A nice place to stay",
    price=120,
    latitude=48.8566,
    longitude=2.3522,
    amenities=[wifi, pool]
)

# Add an amenity after creation
gym = Amenity(name="Gym", description="Fitness center")
place.add_amenity(gym)

# Leave a review
review = Review(owner_id=user.id, place_id=place.id, rating=5, comment="Great stay!")
place.add_review(review)

# Access reviews and amenities
for rev in place.reviews:
    print(f"Review by {rev.owner_id}: {rev.comment}")

for amenity in place.amenities:
    print(f"Amenity: {amenity.name} - {amenity.description}")

# Update place details
place.title = "Modern Cozy Apartment"
place.price = 130
place.save()
```

**Key Methods and Responsibilities:**

- `User`: Validates names and emails, stores user data.
- `Place`: Manages amenities and reviews, validates location and price, provides methods `add_amenity`, `remove_amenity`, `add_review`, `remove_review`.
- `Amenity`: Stores amenity details, validates input.
- `Review`: Validates rating and comment, links to user and place.
- `BaseModel`: Provides unique ID, timestamps, and update/serialization helpers.

Each model provides methods for creating, updating, deleting, and serializing instances, ensuring a clean separation between business logic and data storage.

## Endpoints!

The project provides a RESTful API for managing users, places, amenities, and reviews. All endpoints are documented and accessible via Swagger UI at `/api/v1/` when the server is running.

### Example Endpoints

- `POST /api/v1/users/` — Create a new user
- `GET /api/v1/users/` — List all users
- `GET /api/v1/users/<user_id>` — Retrieve a user by ID
- `PUT /api/v1/users/<user_id>` — Update a user

- `POST /api/v1/places/` — Create a new place
- `GET /api/v1/places/` — List all places
- `GET /api/v1/places/<place_id>` — Retrieve a place by ID
- `PUT /api/v1/places/<place_id>` — Update a place

- `POST /api/v1/amenity/` — Create a new amenity
- `GET /api/v1/amenity/` — List all amenities
- `GET /api/v1/amenity/<amenity_id>` — Retrieve an amenity by ID
- `PUT /api/v1/amenity/<amenity_id>` — Update an amenity

- `POST /api/v1/reviews/` — Create a new review
- `GET /api/v1/reviews/` — List all reviews
- `GET /api/v1/reviews/<review_id>` — Retrieve a review by ID
- `PUT /api/v1/reviews/<review_id>` — Update a review

---

# Testing the API

Unit and integration tests are provided to ensure the correctness of the API endpoints and business logic. The main test file for endpoint testing is:

- `app/api/v1/test_endpoints.py`

## Running the Tests

From the `part2` directory, run:

```bash
python3 -m unittest app/api/v1/test_endpoints.py
```

## What is Tested

- **User endpoints:** Creation, validation, retrieval, and update of users.
- **Place endpoints:** (Extendable) Creation, retrieval, and update of places.
- **Error handling:** Ensures proper error messages and status codes are returned for invalid input.

## Example Test (from `test_endpoints.py`)

```python
def test_create_user(self):
    response = self.client.post(
        "/api/v1/users/",
        json={
            "first_name": "Jane",
            "last_name": "Doe",
            "email": "jane.doe@example.com",
        },
    )
    self.assertEqual(response.status_code, 201)
    data = response.get_json()
    self.assertIn("id", data)
    self.assertEqual(data["first_name"], "Jane")
    self.assertEqual(data["last_name"], "Doe")
    self.assertEqual(data["email"], "jane.doe@example.com")
```

## Extending the Tests

You can add more tests for places, amenities, and reviews by following the structure in `test_endpoints.py`. Each test should:

- Use the Flask test client to make requests to the API.
- Assert the expected status code and response data.
- Optionally, chain requests (e.g., create a user, then create a place for that user).

---

## License

This project is licensed under the MIT License.