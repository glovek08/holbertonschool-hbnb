# Holberton School - hbnb (Part 2)

This project is part of the Holberton School curriculum and focuses on building the backend of an AirBnB clone. It extends the previous work by adding new features and improving the codebase.

## Features

- **Data Storage:** In-memory persistance.
- **Models:** Includes User, Place, Amenity, and Review models. All inherit from a Base Model.
- **RESTful API:** Provides endpoints for CRUD operations.
- **Web Framework:** Integrates with Flask for web-based interfaces.

## Requirements

- Ubuntu 22.04
- Python 3.8+
- pip (for installing dependencies)
- In-Memory Persistance (For now)

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

## Authors

- [Gabriel Barnada](https://github.com/glovek08/)
- [Federico Paganin Vanoli](https://github.com/federico-paganini)

## License

This project is licensed under the MIT License.

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