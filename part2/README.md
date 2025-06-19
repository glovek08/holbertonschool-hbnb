# Holberton School - hbnb (Part 2)

This project is part of the Holberton School curriculum and focuses on building the backend of an AirBnB clone. It extends the previous work by adding new features and improving the codebase.

## Features

- **Data Storage:** In-memory persistance.
- **Models:** Includes User, Place, Amenity, and Review models. All inherit from a Base Model.
- **RESTful API:** Provides endpoints for CRUD operations.
- **Web Framework:** Integrates with Flask for web-based interfaces.

## Requirements

- Ubuntu 24.04 LTS
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

- `models/` - Data models
- `persistance/` - Storage engine
- `app/` - Flask web application

## Authors

- [Gabriel Barnada](https://github.com/glovek08/)
- [Federico Paganin Vanoli](https://github.com/federico-paganini)

## License

This project is licensed under the MIT License.
