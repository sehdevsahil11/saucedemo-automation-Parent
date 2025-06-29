# 🧪 EXERCISE 2 – API Automation for Petstore

This document outlines the automated test cases implemented for the [Petstore Swagger API](https://petstore.swagger.io/).  
The goal is to validate core CRUD functionality for the `/pet` endpoint, covering positive, negative, and edge case scenarios.

## 🔧 Base URL

https://petstore.swagger.io/v2

---

## ✅ Test Scenarios

### 1. Create a New Pet
- Valid pet creation with all fields  
- Creation with missing required fields (e.g., name)  
- Creation with empty string values  
- Invalid data types (e.g., string instead of number for `id`)  

### 2. Get Pet by ID
- Get existing pet by valid ID  
- Get with invalid ID (e.g., string instead of integer)  
- Get non-existent pet (e.g., ID not in DB)  

### 3. Update Pet
- Update existing pet with valid data  
- Update with invalid data (missing name, wrong ID)  
- Update non-existent pet  

### 4. Delete Pet
- Delete existing pet  
- Delete non-existent pet  
- Delete with invalid ID (e.g., text)  

### 5. Edge Cases
- Use special characters in fields  
- Use extremely large ID  
- Duplicate ID on creation  
- Sending wrong `Content-Type` header  

---

## 📊 Status Code Coverage

- 200 OK – success  
- 400 Bad Request – invalid input  
- 404 Not Found – pet not found  
- 405 Method Not Allowed – wrong method  

---

## 🔁 Sequence of Testing

1. Create pet  
2. Retrieve same pet  
3. Update pet  
4. Delete pet  
5. Validate deletion  

---

## 🧰 Tools Used

- Python 3.x  
- PyTest  
- Requests library  
- Swagger Petstore API  

---

