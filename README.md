# API Project
This API project is designed to provide access to various resources via RESTful endpoints. Each endpoint allows users to interact with the data through operations such as creating, reading, updating, and deleting entries.
The project leverages SQLite as its database, providing a lightweight and efficient solution for local storage during development. The database schema is automatically managed by Django's ORM, making it easy to migrate changes and maintain consistency in data storage.
This project uses a Django backend to handle requests, process data, and manage the database and Django Rest Framework for building the API. The API is structured to support the following:
  - **Create**: Add new entries to the database.
  - **Read**: Retrieve data from the database for display or analysis.
  - **Update**: Modify existing records within the database.
  - **Delete**: Remove records from the database as needed.

This API project provides endpoints for various functions, tested and run using Postman.
## Requirements
- [Python 3.x](https://www.python.org/downloads/) 
- [Postman](https://www.postman.com/downloads/)

## Setup Instructions

1. **Clone the Repository**
    ```bash
   git clone https://github.com/your-username/your-api-project.git
   cd your-api-project
   
2. **Install Dependencies Install the required packages by running:**
   ```bash
   pip install -r requirements.txt

3. **Start the Server Run the following command to start the server:**
   ```bash
   python manage.py runserver

4. Launch the Postman application.

5. Create a New Collection.

6. Add Requests:
  - For each endpoint create a request under the collection.
  - Set the request type (GET, POST, PUT, DELETE).
  - Enter the URL (eg: http://127.0.0.1:8000/books).
  - Input parameters in the body or URL as needed.
  - Click "Send" to test each endpoint.
  - Review the responses and check for successful requests and any error messages.
  - Save Responses: For future reference, save the responses in Postman or export the collection




# API Documentation
This API provides access to a database of resources with the following endpoints. Each endpoint uses JSON format for requests and responses.

**Endpoints**
1. GET All Data
  Endpoint: /books/
  Method: GET
  Description: Fetches all records in the database.
*Example Request*
GET   http://127.0.0.1:8000/books
*Example Response*
Status: 200 OK
Body:
    [
        {
            "book_id": 1,
            "book_title": "The Personality",
            "book_author": "Jenny Hinn"
        },
        {
            "book_id": 2,
            "book_title": "Thor",
            "book_author": "Marvel"
        }
       ]
   
2. GET Data by ID
  Endpoint: /books/{id}/
  Method: GET
  Description: Fetches a single record by its ID.
*Example Request*
GET   http://127.0.0.1:8000/books/1
*Example Response*
Status: 200 OK
Body:
    [
        {
            "book_id": 1,
            "book_title": "The Personality",
            "book_author": "Jenny Hinn"
        }
       ]

3. POST Add Data
  Endpoint: /books/
  Method: POST
  Description: Adds a new record to the database.
*Example Request*
POST   http://127.0.0.1:8000/books/
Body:
     {
            "book_title": "The Annointing",
            "book_author": "Benny Hinn"
        }
*Example Response*
Status: 201 CREATED
Body:
    [
        {
            "book_id": 3,
            "book_title": "The Annointing",
            "book_author": "Benny Hinn"
        }
       ]

4. PUT Update Data by ID
  Endpoint: /books/{id}/
  Method: PUT
  Description: Updates an existing record by its ID.
*Example Request*
POST   http://127.0.0.1:8000/books/2
Body:
     {
            "book_title": "Spiderman",
            "book_author": "Marvel"
        }
*Example Response*
Status: 200 OK
Body:
    [
        {
            "book_id": 2,
            "book_title": "The Spiderman",
            "book_author": "Marvel"
        }
       ]
   
5. DELETE Data by ID
  Endpoint: /books/{id}/
  Method: DELETE
  Description: Deletes a record by its ID.
*Example Request*
DELETE   http://127.0.0.1:8000/books/1
*Example Response*
Status: 204 No Content
