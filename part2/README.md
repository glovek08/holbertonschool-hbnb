# Holberton School - hbnb (Part 2)

This project is part of the Holberton School curriculum and focuses on building the backend of an AirBnB clone. It extends the previous work by adding new features and improving the codebase.

## Features

- **Data Storage:** Supports both file and database storage engines.
- **Command Interpreter:** Allows management of objects via a command-line interface.
- **Models:** Includes User, Place, State, City, Amenity, and Review models.
- **RESTful API:** Provides endpoints for CRUD operations.
- **Web Framework:** Integrates with Flask for web-based interfaces.

## Requirements

- Ubuntu 24.04 LTS
- Python 3.8+
- pip (for installing dependencies)
- In-Memory Persistance (For now)

## Installation

1. Clone the repository:
    ```bash
    git clone <https://github.com/glovek08/holbertonschool-hbnb>
    cd holbertonschool-hbnb/part2
    ```

2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Set up environment variables as needed (see `.env.example`).

## Usage

- **Command Interpreter:**
  ```bash
  ./console.py
  ```

- **Start Web Server:**
  ```bash
  python3 -m app.py.<module>
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