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

## **Authentication Management**

### **Signup**
- **Method**: POST
- **URL**: `BASE_URL/signup/`
- **Payload**:
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
- **Response**:
```json
{
    "message": "User registration successful."
}
```

### **Signin**
- **Method**: POST
- **URL**: `BASE_URL/signin/`
- **Payload**:
```json
{
    "username": "maame",
    "password": "123password"
}
```
- **Response**:
```json
{
    "message": "User login successful.",
    "token": "fbf32dc0321d15f8509eaa99c33afe26abb00e17"
}
```

### **Test Token**
- **Method**: GET
- **URL**: `BASE_URL/test-token/`
- **Headers**:
```json
{
    "Authorization": "Token fbf32dc0321d15f8509eaa99c33afe26abb00e17"
}
```
- **Response**:
```json
{
    "message": "Passed for maame@example.com"
}
```

---

## **User Details**

### **Retrieve User Details**
- **Method**: GET
- **URL**: `BASE_URL/users/token`
- **Authentication**: Required
- **Headers**:
```json
{
    "Authorization": "Token fbf32dc0321d15f8509eaa99c33afe26abb00e17"
}
```
- **Response**:
```json
{
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
- **Method**: POST
- **URL**: `BASE_URL/users/token/`
- **Authentication**: Required
- **Headers**:
```json
{
    "first_name": "Maame",
    "last_name": "Naa",
    "username": "maame",
    "email": "maame.naa@example.com",
    "phone_number": "27783674",
}
```
- **Response**:
```json
{
    "first_name": "Maame",
    "last_name": "Naa",
    "username": "maame",
    "email": "maame@example.com",
    "password": "123password",
    "phone_number": "27783674",
    "date_joined": "2024-12-01T14:23:00Z"
}
```

