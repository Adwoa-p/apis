# **API DOCUMENTATION**

## **Project Overview**
<p>This API project is designed to provide secure access to various resources via RESTful endpoints. The project uses SQLite as its database, providing a lightweight and efficient solution for local storage during development. For production environments, switching to a robust database like PostgreSQL is recommended. The project leverages Django for backend management and Django Rest Framework (DRF) for building the API, with an authentication layer implemented to enhance security and control user access.</p>

` BASE_URL: http://127.0.0.1:8000/ `

---

## **Table of Contents**
1. [Authentication Management](#authentication-management)
   - [Signup](#signup)
   - [Signin](#signin)
   - [Test Token](#test-token)
2. [User Details](#user-details)
   - [Retrieve User Details](#retrieve-user-details)
   - [Edit User Details](#edit-user-details)
3. [General Endpoints](#general-endpoints)
   - [Retrieving All Books](#retrieving-all-books)
   - [Retrieving Book Details By ID](#retrieving-book-details-by-id)
   - [Retrieving A Particular Book’s Reviews](#retrieving-a-particular-books-reviews)
   - [Retrieving A Review Of A Particular Book](#retrieving-a-review-of-a-particular-book)
4. [User Endpoints](#user-endpoints)
    - [Retrieve All Reviews](#retrieve-all-reviews)
    - [Add A Review](#add-a-review)
    - [Update Review Visibility](#update-review-visibilty)
    - [Update A Review](#update-a-review)
    - [Delete Review](#delete-review)
5. [Admin Endpoints](#admin-endpoints)
    - [Add Book](#add-book)
    - [Update Book](#update-book)
    - [Delete Book](#delete-book)
    - [Delete Review Of A Book](#delete-review-of-a-book)
---


## **AUTHENTICATION MANAGEMENT**

### **Signup**
**Method:** POST  
**URL:** `BASE_URL/signup/`  
**Authentication:** False  
**Description:** Allows new users to register.

#### Sample Request
```http
   POST http://127.0.0.1:8000/signup/
```
```json
{
    "first_name": "Maame",
    "last_name": "Naa",
    "username": "maame",
    "email": "maame@example.com",
    "password": "123password",
    "phone_number": "27783674"
}
```

#### Sample Response
```json
{
    "message": "User registration successful."
}
```

### **Signin**
**Method:** POST  
**URL:** `BASE_URL/login/`  
**Authentication:** False  
**Description:** Allows existing users to log in.

#### Sample Request
```http
    POST http://127.0.0.1:8000/login/
```
```json
{
    "username": "maame",
    "password": "123password"
}
```

#### Sample Response
```json
{
    "message": "User login successful.",
    "token": "fbf32dc0321d15f8509eaa99c33afe26abb00e17"
}
```

### **Test Token**
**Method:** GET  
**URL:** `BASE_URL/test_token/`  
**Authentication:** True  
**Description:** Validates the token of the authenticated user.

#### Sample Request
```http
GET http://127.0.0.1:8000/test_token/
Authorization: Bearer fbf32dc0321d15f8509eaa99c33afe26abb00e17
```

#### Sample Response
```json
{
    "message": "Passed for maame@example.com"
}
```

---

## **USER DETAILS**

### **Retrieve User Details**
**Method:** GET  
**URL:** `BASE_URL/user/`  
**Authentication:** True  
**Description:** Retrieves the details of the authenticated user.

#### Sample Request
```http
GET http://127.0.0.1:8000/user/
Authorization: Bearer fbf32dc0321d15f8509eaa99c33afe26abb00e17
```

#### Sample Response
```json
{
    "user_id": 1,
    "first_name": "Maame",
    "last_name": "Naa",
    "username": "maame",
    "email": "maame@example.com",
    "password": "123password",
    "phone_number": "27783674",
    "date_joined": "2024-12-01T14:23:00Z"
}
```
### **Edit User Details**
**Method:** PUT  
**URL:** `BASE_URL/user/`  
**Authentication:** True  
**Description:** Allows authenticated users to update their profile details.

#### Sample Request
```http
PUT http://127.0.0.1:8000/user/
Authorization: Bearer fbf32dc0321d15f8509eaa99c33afe26abb00e17
```
```json
{
    "first_name": "Maame",
    "last_name": "Naa",
    "username": "naa", 
    "email": "maame.naa@example.com", 
    "phone_number": "27783674"
}
```

#### Sample Response
```json
{
    "message": "User details updated successfully.",
    "updated_user": {
        "user_id": 1,
        "first_name": "Maame",
        "last_name": "Naa",
        "username": "maame",
        "email": "maame@example.com",
        "phone_number": "27783674",
        "date_joined": "2024-12-01T14:23:00Z"
    }
}
```

---

## **GENERAL ENDPOINTS**

### **Retrieving All Books**

**Method:** GET  
**URL:** `BASE_URL/books/` </br>
**Authentication:** False  
**Description:** Allows admin, users, and non-users to retrieve all books.

#### Sample Request
```http
GET http://127.0.0.1:8000/books/
```

#### Sample Response
```json
[ 
     {
        "book_id": 1,
        "book_title": "Maame",
        "book_author": "Naa",
        "genre": "naa",
        "book_content": "lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. Nulla consequat massa quis enim.",
        "book_summary": "lorem ipsum dolor sit amet, consectetuer adipiscing elit.",
        "created": "2024-12-01T14:23:00Z"
    }
]
```

### **Retrieving Book Details By ID**

**Method:** GET  
**URL:** `BASE_URL/books/{id}/`</br>
**Authentication:** False  
**Description:** Allows users and non-users to retrieve details of a particular book by ID.

#### Sample Request
```http
GET http://127.0.0.1:8000/books/1/
```

#### Sample Response
```json
{
    "book_id": 1,
    "book_title": "Maame",
    "book_author": "Naa",
    "genre": "naa",
    "book_content": "lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. Nulla consequat massa quis enim.",
    "book_summary": "lorem ipsum dolor sit amet, consectetuer adipiscing elit.",
    "created": "2024-12-01T14:23:00Z"
}
```

### **Retrieving A Particular Book’s Reviews**

**Method:** GET  
**URL:** `BASE_URL/books/{id}/reviews/` </br>
**Authentication:** False  
**Description:** Allows admins, users, and non-users to retrieve all reviews of a particular book

#### Sample Request
```http
GET http://127.0.0.1:8000/books/1/reviews/
```

#### Sample Response
```json
[
    {
        "review_text": "Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. Nulla consequat massa quis enim.",
        "rating": "8"
        },
        {
        "review_text": "Nulla consequat massa quis enim.",
        "rating": "5"
    }
]
```

### **Retrieving A Review Of A Particular Book**

**Method:** GET  
**URL:** `BASE URL/books/{id}/reviews/{id}/`  
**Authentication:** False  
**Description:** Allows users, admins, and non-users to get a particular review of a book by ID.

#### Sample Request
```http
GET http://127.0.0.1:8000/books/1/reviews/2/
```

#### Sample Response
```json
{
    "review_id": 2,
    "review_text": "Nulla consequat massa quis enim.",
    "rating": "5",
    "date_posted": "2024-12-01T14:23:00Z"
}
```

---

## **USER ENDPOINTS**

### **Retrieve All User Reviews**

**Method:** GET  
**URL:** `BASE URL/user/reviews/` </br>
**Authentication:** True  
**Description:** Allows users to get all reviews they’ve ever posted.

#### Sample Request
```http
GET http://127.0.0.1:8000/user/reviews/
Authorization: Bearer fbf32dc0321d15f8509eaa99c33afe26abb00e17
```

#### Sample Response
```json
[
    {
        "review_id": 1,
        "review_text": "Donec quam felis, ultricies nec, pellentesque eu,  pretium quis, sem. Nulla consequat massa quis enim.",
        "rating": "8",
        "date_posted": "2024-11-01T14:23:00Z"
    },
    {
        "review_id": 2,
        "review_text": "Nulla consequat massa quis enim.",
        "rating": "5",
        "date_posted": "2024-12-01T14:23:00Z"
    }
]
```

### **Add A Review**

**Method:** POST  
**URL:** `BASE URL/user/reviews/`  
**Authentication:** True  
**Description:** Allows users to add a review to a book.

#### Sample Request
```http
POST http://127.0.0.1:8000/user/reviews/
Authorization: Bearer fbf32dc0321d15f8509eaa99c33afe26abb00e17
```
```json
{
 "review_text": "Nulla consequat massa quis enim.",
 "rating": "6",
 "visibility": "Public"
}
```

#### Sample Response
```json
{
    "review_id": 3,
    "review_text": "Nulla consequat massa quis enim.",
    "rating": "6",
    "visibility": "Public",
    "date_posted": "2024-14-08T14:23:08Z"
}
```

### **Update Review Visibility**

**Method:** PATCH  
**URL:** `BASE_URL/user/reviews/{id}/public/` and `BASE_URL/user/reviews/{id}/private/` </br>
**Authentication:** True  </br>
**Description:** Allows users to edit their visibility detail.

#### Sample Request
```http
PATCH http://127.0.0.1:8000/user/reviews/3/public/
Authorization: Bearer fbf32dc0321d15f8509eaa99c33afe26abb00e17
```
```json
{
 "review_text": "Nulla consequat massa quis enim.",
 "rating": "6",
 "visibility": "Public"
}
```

#### Sample Response
```json
{
    "review_id": 3,
    "review_text": "Nulla consequat massa quis enim.",
    "rating": "6",
    "visibility": "Public",
    "date_posted": "2024-14-08T14:23:08Z"
}
```

### **Update A Review**

**Method:** POST  
**URL:** `BASE_URL/user/reviews/{id}/` </br>
**Authentication:** True  
**Description:** Allows users to edit the details of a particular review posted.

#### Sample Request
```http
POST http://127.0.0.1:8000/user/reviews/3/
Authorization: Bearer fbf32dc0321d15f8509eaa99c33afe26abb00e17
```
```json
{
 "review_text": "Nulla massa quis enim.",
 "rating": "7",
 "visibility": "Private"
}
```

#### Sample Response
```json
{
    "review_id": 3,
    "review_text": "Nulla massa quis enim.",
    "rating": "7",
    "visibility": "Private",
    "date_posted": "2024-14-08T14:23:08Z"
}
```

### **Delete Review**

**Method:** DELETE  
**URL:** `BASE_URL/user/reviews/{id}/`  
**Authentication:** True  
**Description:** Allows users to delete a review posted.

#### Sample Request
```http
DELETE http://127.0.0.1:8000/user/reviews/3/
Authorization: Bearer fbf32dc0321d15f8509eaa99c33afe26abb00e17
```

#### Sample Response
```json
{
    "message": "Review deleted successfully."
}
```

---

## **ADMIN ENDPOINTS**

### **Add Book**

**Method:** POST  
**URL:** `BASE_URL/books/` </br> 
**Authentication:** True </br> 
**Description:** Allows admin to add a book

#### Sample Request
```http
POST http://127.0.0.1:8000/books/
Authorization: Bearer fbf32dc0321d15f8509eaa99c33afe26abb00e17
```
```json
{
 "book_title": "Lion of Judah",
 "book_author": "Zen Dee", 
 "genre": "Christian", 
 "book_content": "Curabitur ullamcorper ultricies nisi. Nam eget dui. Etiam rhoncus. Maecenas tempus, tellus eget condimentum rhoncus, sem quam semper libero, sit amet adipiscing sem neque sed ipsum.", 
 "book_summary": " Nam quam nunc, blandit vel, luctus pulvinar, hendrerit id, lorem. "
}
```

#### Sample Response
```json
{
  "book_id": 2,
  "book_title": "Lion of Judah",
  "book_author": "Zen Dee", 
  "genre": "Christian Literature", 
  "book_content": "Curabitur ullamcorper ultricies nisi. Nam eget dui. Etiam rhoncus. Maecenas tempus, tellus eget condimentum rhoncus, sem quam semper libero, sit amet adipiscing sem neque sed ipsum.",
  "book_summary": " Nam quam nunc, blandit vel, luctus pulvinar, hendrerit id, lorem. ",
  "created": "2024-12-01T14:23:00Z"
}
```

### **Update Book**

**Method:** POST  
**URL:** `BASE_URL/books/{id}/` </br> 
**Authentication:** True </br> 
**Description:** Allows admin to update the details of a book.

#### Sample Request
```http
POST http://127.0.0.1:8000/books/2/
Authorization: Bearer fbf32dc0321d15f8509eaa99c33afe26abb00e17
```
```json
{
 "book_title": "Lion of Judah",
 "book_author": "Zen Dee", 
 "genre": "Christian", 
 "book_content": "Curabitur ullamcorper ultricies nisi. Nam eget dui. Etiam rhoncus. Maecenas tempus", 
 "book_summary": " Nam quam nunc, blandit vel, luctus pulvinar, hendrerit id, lorem. "
}
```

#### Sample Response
```json
{
  "book_id": 2,
  "book_title": "Lion of Judah",
  "book_author": "Zen Dee", 
  "genre": "Christian Literature", 
  "book_content": "Curabitur ullamcorper ultricies nisi. Nam eget dui. Etiam rhoncus. Maecenas tempus",
  "book_summary": " Nam quam nunc, blandit vel, luctus pulvinar, hendrerit id, lorem.",
  "created": "2024-12-01T14:23:00Z"

}
```

### **Delete Book**

**Method:** DELETE </br>
**URL:** `BASE_URL/books/{id}/` </br>
**Authentication:** True  
**Description:** Allows admin to delete a book.

#### Sample Request
```http
DELETE http://127.0.0.1:8000/books/2/
Authorization: Bearer fbf32dc0321d15f8509eaa99c33afe26abb00e17
```

#### Sample Response
```json
{
  "message": "Book deleted successfully."
}
```

### **Delete Review Of A Book**

**Method:** POST  
**URL:** `BASE_URL/books/{id}/reviews/{id}/` </br> 
**Authentication:** True  
**Description:** Allows admin to delte a book's review by permanently making it private

#### Sample Request
```http
DELETE	 http://127.0.0.1:8000/books/1/reviews/1/
Authorization: Bearer fbf32dc0321d15f8509eaa99c33afe26abb00e17
```

#### Sample Response
```json
{
  "message": "Review successully deleted."
}
```