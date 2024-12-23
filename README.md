# API Documentation

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

---

# API Documentation

## **Authentication Management**

### **Signup**
**Method:** POST  
**URL:** `BASE_URL/signup/`  
**Authentication:** False  
**Description:** Allows new users to register.

#### Sample Request
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
**URL:** `BASE_URL/signin/`  
**Authentication:** False  
**Description:** Allows existing users to log in.

#### Sample Request
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
Authorization: Token fbf32dc0321d15f8509eaa99c33afe26abb00e17
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
**URL:** `BASE_URL/user`  
**Authentication:** True  
**Description:** Retrieves the details of the authenticated user.

#### Sample Request
```http
Authorization: Token fbf32dc0321d15f8509eaa99c33afe26abb00e17
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


---

## **GENERAL ENDPOINTS**

### RETRIEVING ALL BOOKS

**Method:** GET  
**URL:** BASE URL + book/  
**Authentication:** False  
**Description:** Allows admin, users, and non-users to retrieve all books.

#### Sample Request
```http
GET http://127.0.0.1:8000/books/
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

### RETRIEVING BOOK DETAILS BY ID

**Method:** GET  
**URL:** BASE URL + book/{id}/  
**Authentication:** False  
**Description:** Allows users and non-users to retrieve details of a particular book by ID.

#### Sample Request
```http
GET http://127.0.0.1:8000/books/1
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

### RETRIEVING A PARTICULAR BOOK’S REVIEWS

**Method:** GET  
**URL:** BASE URL + book/{id}/reviews  
**Authentication:** False  
**Description:** Allows admins, users, and non-users to retrieve all reviews of a particular book

#### Sample Request
```http
GET http://127.0.0.1:8000/books/1/reviews
```

#### Sample Response
```json
{
 "review_text": "Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. Nulla consequat massa quis enim.",
 "rating": "8"
},
{
 "review_text": "Nulla consequat massa quis enim.",
 "rating": "5"
}
```

### **Edit User Details**
**Method:** PUT  
**URL:** `BASE_URL/user`  
**Authentication:** True  
**Description:** Allows authenticated users to update their profile details.

#### Sample Request
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

### RETRIEVING A REVIEW OF A PARTICULAR BOOK

**Method:** GET  
**URL:** BASE URL + book/{id}/review/{id}  
**Authentication:** False  
**Description:** Allows users, admins, and non-users to get a particular review of a book by ID.

#### Sample Request
```http
GET http://127.0.0.1:8000/books/1/reviews/2
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

## USER ENDPOINTS

### RETRIEVE ALL REVIEWS

**Method:** GET  
**URL:** BASE URL + user/review/  
**Authentication:** True  
**Description:** Allows users to get all reviews they’ve ever posted.

#### Sample Request
```http
GET http://127.0.0.1:8000/users/reviews
```

#### Sample Response
```json
{
    "review_id": 1,
    "review_text": "Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. Nulla consequat massa quis enim.",
    "rating": "8",
    "date_posted": "2024-11-01T14:23:00Z"
},
{
    "review_id": 2,
    "review_text": "Nulla consequat massa quis enim.",
    "rating": "5",
    "date_posted": "2024-12-01T14:23:00Z"
}
```

### ADD A REVIEW

**Method:** POST  
**URL:** BASE URL + user/review  
**Authentication:** True  
**Description:** Allows users to add a review to a book.

#### Sample Request
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

### UPDATE REVIEW VISIBILITY

**Method:** PATCH  
**URL:** BASE URL + user/review/{id}/public  
**Authentication:** True  
**Description:** Allows users to edit their visibility detail.

#### Sample Request
```json
{
 "review_text": "Nulla consequat massa quis enim.",
 "rating": "6",
 "visibility": "Private"
}
```

#### Sample Response
```json
{
    "review_id": 3,
    "review_text": "Nulla consequat massa quis enim.",
    "rating": "6",
    "visibility": "Private",
    "date_posted": "2024-14-08T14:23:08Z"
}
```

### UPDATE A REVIEW

**Method:** POST  
**URL:** BASE URL + user/review/{id}  
**Authentication:** True  
**Description:** Allows users to edit the details of a particular review posted.

#### Sample Request
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

### DELETE REVIEW

**Method:** DELETE  
**URL:** BASE URL + user/review/{id}  
**Authentication:** True  
**Description:** Allows users to delete a review posted.

#### Sample Request
```http
DELETE http://127.0.0.1:8000/users/reviews/3
```

#### Sample Response
```json
{
    "message": "Review deleted successfully."
}
```

---

## ADMIN ENDPOINTS

### ADD BOOK

**Method:** POST  
**URL:** BASE URL + book/  
**Authentication:** True  
**Description:** Allows admin to add a book

#### Sample Request
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
  "book_content": "Curabitur ullamcorper ultricies nisi. Nam eget dui. Etiam rhoncus. Maecenas tempus
