![HolbertonBnB_Banner](https://github.com/user-attachments/assets/dbab0855-bd6f-461d-a316-ecb34d77987b)

# 
<div align="center">
  <h1>HOLBERTON BnB</h1>
  <h2>An AirBnB-like project.</h2>
</div>

Project Participants:

* [Federico Paganini Vanoli.](https://github.com/federico-paganini)  
* [Gabriel Baez Barnada.](https://github.com/glovek08)

## **Introduction:**

The purpose of this document is to guide you through the design process of our AirBnB-like application.   
In this documentation you can find UML diagrams.

### **What you'll find in this document:** 

* High-level system architecture diagrams  
* Detailed class relationships and data models   
* Business logic flow documentation  
* Component interaction specifications

## **High-Level Architecture:**

### **Layered Architecture Overview**

This AirBnB-like project follows a three-tier layered architecture pattern that guarantees separation of concerns, maintainability and scalability.

Each layer has responsibilities and communicates through defined interfaces.

### **Layers**

* #### **Presentation Layer:**

  * User interface and user experience.  
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

  * Manages data storage and operations.  
  * Provides data access.  
  * Persistence operations.  
  * JSON processing.

### **Facade Pattern Implementation:**

The [Facade Pattern](https://refactoring.guru/design-patterns/facade/python/example) is an interface between the Presentation and Business Logic layers.  
The fundamental purpose is don’t expose entities (User, Place, Review, Amenities) providing high-level operation (functions).  
This approach ensures that the presentation layer doesn't need to understand the details of business logic implementation, promoting low coupling and easier maintenance.

##  **High-Level Package Diagram**

For this project, we developed a three-layer architecture implementing the Facade pattern for separation of concern and scalability. *Also because it’s the only one we know enough about.*
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

  * **Requests:** Manage user requests to the application.  
  * **Responses:** Parse response from the lower level layers back to the user.  
  * **HTTP Status Management:** HTTP codes and error handling.

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
  * **Logic Operations:** This item includes all the verifications for every entity, functionalities and necessary calcs.  
    For example: Performs pricing calculations, booking conflicts, calculates commission profit, handles cancellations and so on. *\[WIP\]Logic operations combined produces a basic workflow; for example could be: check availability \> validate client \> calculate price \> reserve property \> send confirmations.*  
  * **Relation Management:** validates relationships, for example: one client per booking, multiple amenities per place. Prevent orphaned entities and broken references, handles entity operations like: deleting a client affects their bookings, reviews, and listings.

### **Persistence Layer**

Data storage and retrieval, data integrity maintenance.

* #### **Storage:**

  * **Client Data:** User information storage.  
  * **Place Data:** Place information storage.  
  * **JSON Processing**: data serialization.

**Data flow example:**

1. User registers.  
2. API handles this request to facade.  
3. Request is processed.  
4. Data is validated.  
5. Data is stored.  
6. JSON serialization.

###

## **ER Diagram**
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
* **title**: listing’s title.
* **description**: a short description made by the *User* who owns it.  
* **price**: rent price per day.  
* **longitude**: longitude of this place.
* **latitude**: latitude of this place.
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

- One amenity can be shared across many *Places*.  
- \[not implemented yet\] One amenity can be classified as one of 3 grades: basic, extra and premium. Which in turn will give a *Place* part of its rating.  
- Can be created, updated and deleted by the Admin Users.

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
