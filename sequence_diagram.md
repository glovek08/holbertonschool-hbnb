[DIAGRAM SVG](https://www.mermaidchart.com/raw/4783d30e-e5d4-41df-bbde-f378a90b705f?theme=light&version=v0.1&format=svg)

---
config:
  theme: redux
---
sequenceDiagram
  participant ClientApp as Client App
  participant API as API
  participant BusinessLogic as Business Logic
  participant Database as Database
  ClientApp ->> API: Create Listing request
  API ->> BusinessLogic: createListing(data)
  BusinessLogic ->> BusinessLogic: Validate Listing Data
  alt Listing Data Valid
    BusinessLogic ->> Database: Save Listing Data
    Database -->> BusinessLogic: Listing Saved Confirmation
    BusinessLogic -->> API: Listing Created Successfully
    API -->> ClientApp: HTTP 201 Created (Listing ID)
  else Listing Data Invalid
    BusinessLogic -->> API: Invalid Listing Data Error
    API -->> ClientApp: HTTP 400 Bad Request (Error Details)
  end
  ClientApp ->> API: Fetch Place List
  API ->> BusinessLogic: getPlaceList()
  BusinessLogic ->> Database: Query All Listings
  Database -->> BusinessLogic: Return List of Listings
  BusinessLogic -->> API: Return Place List
  API -->> ClientApp: HTTP 200 OK (List of Places)
 %% HTTP 201 -> Request Created
 %% HTTP 400 -> Bad Request
 %% HTTP 200 -> OK