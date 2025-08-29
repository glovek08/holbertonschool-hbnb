![HolbertonBnB_Banner](https://github.com/user-attachments/assets/dbab0855-bd6f-461d-a316-ecb34d77987b)

<div align="center">
  <h1>Holberton BnB</h1>
  <p>A modern, full-stack accommodation booking platform inspired by AirBnB</p>
</div>

## About

Holberton BnB is a comprehensive web application that enables users to discover, list, and review accommodation properties. Built with modern web technologies, it features a robust three-tier architecture that ensures scalability, maintainability, and optimal user experience. The platform allows property owners to showcase their listings with detailed information, amenities, and ratings, while providing guests with an intuitive interface to explore available accommodations.

## Key Features

- **Property Management**: Create, update, and manage accommodation listings with detailed descriptions and geolocation
- **Star Rating System**: 5-star rating system for places with visual star indicators and rating validation
- **User Authentication & Authorization**: JWT-based authentication with bcrypt password hashing and admin privileges
- **Amenity Integration**: Comprehensive amenity management with many-to-many relationships
- **Review System**: Users can leave reviews and ratings with proper validation and relationship management
- **Database Persistence**: MySQL database with SQLAlchemy ORM and comprehensive data relationships
- **Repository Pattern**: Specialized repositories for different entities with abstract base classes
- **RESTful API**: Well-structured API endpoints with Swagger documentation and CORS support
- **Responsive Design**: Modern, mobile-friendly interface built with Svelte and custom styling
- **Testing Suite**: Comprehensive unit and integration tests for models and API endpoints
- **Database Seeding**: Automated database seeding with test data for development

## Technology Stack

### Backend
![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python&style=for-the-badge)
![Flask](https://img.shields.io/badge/Flask-Framework-black?logo=flask&style=for-the-badge)
![Flask-RESTX](https://img.shields.io/badge/Flask--RESTX-API-green?logo=flask&style=for-the-badge)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-2.0+-blue?logo=sqlalchemy&style=for-the-badge)
![MySQL](https://img.shields.io/badge/MySQL-Database-yellow?logo=mysql&style=for-the-badge)
![PyMySQL](https://img.shields.io/badge/PyMySQL-Connector-orange?logo=mysql&style=for-the-badge)
![JWT](https://img.shields.io/badge/JWT-Authentication-black?logo=jsonwebtokens&style=for-the-badge)
![Bcrypt](https://img.shields.io/badge/Bcrypt-Password_Hashing-red?logo=letsencrypt&style=for-the-badge)

### Frontend
![Svelte](https://img.shields.io/badge/Svelte-4-orange?style=for-the-badge&logo=svelte)
![Routify 3.5](https://img.shields.io/badge/Routify-v3.5.1-blue?style=for-the-badge&logo=roxi)
![Vite 6.3.5](https://img.shields.io/badge/Vite-v6.3.5-purple?style=for-the-badge&logo=vite)
![Node.js](https://img.shields.io/badge/Node.js-v20.19.4-green?style=for-the-badge&logo=node.js)

### Development Tools
![Docker](https://img.shields.io/badge/Docker-Containerization-blue?style=for-the-badge&logo=docker)
![Git](https://img.shields.io/badge/Git-Version_Control-red?style=for-the-badge&logo=git)
![Swagger](https://img.shields.io/badge/Swagger-API_Documentation-green?style=for-the-badge&logo=swagger)
![Pytest](https://img.shields.io/badge/Pytest-Testing-blue?style=for-the-badge&logo=pytest)

<!-- License -->
![License](https://img.shields.io/github/license/glovek08/holbertonschool-hbnb?style=flat-square)

<!-- Repo stats -->
![Last Commit](https://img.shields.io/github/last-commit/glovek08/holbertonschool-hbnb?style=flat-square)
![Repo Size](https://img.shields.io/github/repo-size/glovek08/holbertonschool-hbnb?style=flat-square)

## Contributors

[![glovek08](https://img.shields.io/badge/GitHub-glovek08-blue?logo=github)](https://github.com/glovek08)
[![federico-paganini](https://img.shields.io/badge/GitHub-federico--paganini-blue?logo=github)](https://github.com/federico-paganini)

## Table of Contents

- [About](#about)
- [Key Features](#key-features)
- [Technology Stack](#technology-stack)
- [Architecture](#high-level-architecture)
- [Database Design](#er-diagram)
- [API Workflows](#sequence-diagrams)
- [Contributors](#contributors)

## **High-Level Architecture:**

### **Layered Architecture Overview**

This AirBnB-like project follows a three-tier layered architecture pattern that guarantees separation of concerns, maintainability and scalability.

Each layer has responsibilities and communicates through defined interfaces.

### **Layers**

* #### **Presentation Layer:**

  * UI/UX 
  * Client-side interactions.  
  * Request/Responses formatting.  
  * HTTP status management.  
  * API Controllers.

* #### **Business Logic Layer:**

  * Contains core application logic and business rules.  
  * Manages data models and their relationships.  
  * Validation, processing and business operations.  
  * Components: User, Place, Review, Amenity.

* #### **Persistence Layer:**

  * MySQL database with SQLAlchemy ORM integration
  * Repository pattern with specialized repositories for different entities
  * Database relationship management and foreign key constraints
  * Automated database migrations and seeding capabilities

### **Facade Pattern Implementation:**

The [Facade Pattern](https://refactoring.guru/design-patterns/facade/python/example) is an interface between the Presentation and Business Logic layers.  
The fundamental purpose is don’t expose entities (User, Place, Review, Amenities) providing high-level operation (functions).  
This approach ensures that the presentation layer doesn't need to understand the details of business logic implementation, promoting low coupling and easier maintenance.

##  **High-Level Package Diagram**

For this project, we developed a three-layer architecture implementing the Facade pattern for separation of concern and scalability.
###

<p align="center">
  <img src="https://github.com/user-attachments/assets/00f70623-1ce4-4f9f-b239-7069fd4ee644" alt="Banner">
</p>

### 

### **Presentation Layer:**

User-System communication, this represents the application GUI’s and the higher level logic in our app.

* #### **Front-End:**

  * **Login:** User log-in/sign-in authentication.  
  * **User Management:**  Where the user can customize its profile, change user settings, see user-related information.  
  * **Publish Offer:** Manage places, create/update user listings.  
  * **Rent a Place:** Showcase listings available for rent.

* #### **API:**

  * **Authentication Endpoints:** JWT-based login and registration with secure cookie handling
  * **CRUD Operations:** Complete REST API for users, places, amenities, and reviews
  * **Swagger Documentation:** Interactive API documentation with authentication support
  * **CORS Support:** Cross-origin resource sharing for frontend-backend communication
  * **HTTP Status Management:** Comprehensive HTTP status codes and error handling

### **Business Logic Layer:**

Main design and logic of our application, this is where the facade pattern takes form.  
The facade pattern gives the components of the business logic layer a straightforward way to communicate with higher level components.

* #### **Core:**

  * **Client:** User-related operations. (create user, update user information, validate information, manage user-user interactions)  
  * **Places:** Place-related operations. (create/update place, validate place information, manage status like; available, rented, hidden, etc)  
  * **Reviews:** Review moderation, calculate place rating (imagine a 5-star system based on the number of starts where each review can be 1-5 stars).  
  * **Amenities**: Create/Update/Delete amenity, categorize amenities based on their level of comfort (a jacuzzi is a premium amenity.)

* #### **Rules:**

  * **Validate Data:** Ensures data integrity and enforces business rules before processing. Validates input information like; data type, required fields. validates email, phone and dates. Cleans up data. Handles relationship logic like: *review target place exists* and *user rented that place within a time-frame.*  
  * **Logic Operations:** Performs comprehensive validation for every entity, including data type validation, business rule enforcement, and relationship integrity checks. Handles complex operations like user authentication, password hashing, rating calculations, and amenity associations.  
  * **Relation Management:** Validates and manages relationships between entities, such as user-place ownership, place-amenity associations, and user-review authorship. Prevents orphaned entities and maintains referential integrity through proper foreign key constraints.

### **Persistence Layer**

Database storage and retrieval with comprehensive relationship management and data integrity.

* #### **Repository Pattern:**

  * **SQLAlchemyRepository:** Base repository with common CRUD operations
  * **UserRepository:** Specialized user data management with email uniqueness
  * **PlaceRepository:** Place data management with amenity and review relationships
  * **ReviewRepository:** Review management with place and user associations

* #### **Database Features:**

  * **MySQL Integration:** Full MySQL database with PyMySQL connector
  * **ORM Relationships:** SQLAlchemy relationships with lazy loading and cascade operations
  * **Data Seeding:** Automated database seeding with comprehensive test data
  * **Migration Support:** Database schema management and automated table creation

**Data flow example:**

1. User registration request received
2. API delegates to HBnBFacade
3. Facade creates User model instance with validation
4. UserRepository persists data to MySQL database
5. Database confirms successful storage
6. Response serialized and returned to client

###

## **ER Diagram && Class Diagram**
<p align="center">
  <picture>
    <source srcset="https://i.ibb.co/mV12DYwM/ERDiagram-dark.png" media="(prefers-color-scheme: light)">
    <source srcset="https://i.ibb.co/JTq6sXY/ERDiagram-white.png" media="(prefers-color-scheme: dark)">
    <img src="https://i.ibb.co/mV12DYwM/ERDiagram-dark.png" alt="ER Diagram">
  </picture>
</p>

### **User:**

Represents a client using the app.

* **id**: Primary Key.  
* **first\_name**: User’s first name.  
* **last\_name**: User’s last name.  
* **email**: User’s email.  
* **is\_admin**: if *True*, this instance of *User* has elevated privileges.
* **created_at**: auto-generated creation date.
* **updated_at**: auto-generated update date.

Characteristics and relations:

- One user can have none or many places listed.  
- An user can be either regular or administrator.  
- Can create, update and delete his account.  
- One user can author one reviews for each place he rented.

### **Place:**

Represents asset locations, whatever a *User* registers as a listing that can be rented and be rated according to its amenities.

* **id**: Primary Key.
* **owner_id**: Foreign Key of user who created the place.
* **title**: listing's title.
* **description**: a short description made by the *User* who owns it.  
* **price**: rent price per day.  
* **longitude**: longitude of this place.
* **latitude**: latitude of this place.
* **rating**: numerical rating from 0-5 stars for the place.
* **created_at**: auto-generated creation date.
* **updated_at**: auto-generated update date.

Characteristics and relations:

- One place can have one *User* who owns it.  
- The owner can create, update and delete this place.  
- One place can have many reviews by many *Users* who rented it.  
- Each place is rated according to *User* reviews, *amenities*’ quality and quantity.

### **Amenity:**

Can be features or services registered to a specific place like; WiFi, free parking, a jacuzzi and so on.   
Amenities are created and managed only by Admin Users.  
After the amenities are created, normal users can select them from a list to append it to places.

* **id**: Primary Key.  
* **name**: the name of the amenity  
* **description**: a short description.
* **created_at**: auto-generated creation date.
* **updated_at**: auto-generated update date.

Characteristics and relations:

- One amenity can be shared across many *Places* through many-to-many relationships.  
- Amenities enhance place attractiveness and can influence user booking decisions.
- Can only be created, updated and deleted by Admin Users with elevated privileges.

### **Review:**

It’s the feedback a *User* who rented a *Place* gave it.

* **id**: Primary Key.  
* **rating**: the user’s rating of a place he rented. 
* **comment**: a public comment that will describe the rating’s reason to other users.
* **created_at**: auto-generated creation date.
* **updated_at**: auto-generated update date.

Characteristics and relations:

- One *User* can author many reviews.  
- One review can rate one *Place*.  
- One *Place* can have many reviews from different users.  
- Can be created, updated and deleted by the author.

### **Place-Amenity:**

Relational Many-To-Many table between places and amenities.

* **place_id**: Foreign key of place.
* **amenity_id**: Foreign key of amenity.

## **Sequence Diagrams**

### **API Interaction Flow**

#### 

#### Overview:

The following diagrams illustrates the core operations of our AirBnB-like implementation.  
The purpose is to demonstrate the interaction flow between system layers, capturing the four primary workflows (listing creation, user registration, listings retrieval and review submission).

### **User Registration sequence**

<p align="center">
  <img src="https://github.com/user-attachments/assets/89013a4f-bed7-47d5-a0db-3ecbb659c161" alt="Banner">
</p>

Process:

1. A new user fills the registration form and submits the request.  
2. API receives the request and delegates to Business Logic through create\_user().  
3. Business logic operations (data integrity, required fields, and business rules check)  
4. Valid data is saved into a database, the confirmation flows back to the client with HTTP 201 Created response.

On failure:

1. Business Logic determines that the data is invalid.  
2. Business Logic responds “Invalid user data request” back to the API.  
3. API returns HTTP 400 Bad Request status to the Client App.

### **Place Creation sequence**

<p align="center">
  <img src="https://github.com/user-attachments/assets/bde858af-c929-4bf1-b1c3-90954769591a" alt="Banner">
</p>

Process:

1. Listing creation request.  
2. API receives request and calls create\_listing(data)  
3. Business logic operation (Ensures data integrity and business rules compliance)  
4. Valid data is saved in the database with HTTP 201 Created response.

On failure:

1. Business Logic determines that the listing data is invalid.  
2. Business Logic responds “Invalid data request” back to the API.  
3. API returns HTTP 400 Bad Request status to the Client App.

### **Review Submission sequence**

<p align="center">
  <img src="https://github.com/user-attachments/assets/4d4e757c-a230-45a5-9be3-a93ca30ae2df" alt="Banner">
</p>

Process:

1. Client App initiates a "Review Submission" request to the API.  
2. API calls the post\_review() function on the Business Logic layer.  
3. Business Logic validates the review data internally.  
4. Business Logic commands the Database for review storing.  
5. Database confirms the review storage with "Review stored confirmation".  
6. Business Logic responds "Review posted successfully" back to the API.  
7. API returns HTTP 201 Created response to the Client App.

On failure:

4. Business Logic determines that the data is invalid.  
5. Business Logic responds “Review not valid” back to the API.  
6. API returns HTTP 400 Bad Request status to the Client App.

### **Fetching a List of Places**

<p align="center">
  <img src="https://github.com/user-attachments/assets/af3fad2a-d029-43fa-91ab-093553f06dad" alt="Banner">
</p>

Process:

1. Available places list request.  
2. API receives requests and calls get\_places() from Business Logic.  
3. Business Logic queries database for listing.  
4. Results returned with HTTP 200 OK Response. If no matches are found, an empty list is returned. Front-end is then refreshed with returned listings.
