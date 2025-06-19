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
