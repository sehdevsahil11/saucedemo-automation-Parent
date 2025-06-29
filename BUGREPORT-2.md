# 🐞 BUG REPORTS – Exercise 2: Petstore API Automation

This document captures all bugs found during the automated testing of the Petstore API (https://petstore.swagger.io/).

---

## Bug #1: API allows pet creation with missing required 'name' field

**Severity:** Medium  
**Priority:** P2  

**Steps to Reproduce:**  
1. Send POST request to `/pet` with JSON payload missing the `name` field  
2. Observe the response status code and content  

**Expected Result:**  
- API should return 400 Bad Request or reject the request due to missing required field  

**Actual Result:**  
- API returns 200 OK and creates a pet without the `name` field  

**Impact:**  
- Allows invalid data to be created in the system, affecting data integrity  


---

## Bug #2: API returns 500 Internal Server Error when creating a pet with invalid ID type

**Severity:** High  
**Priority:** P1  

**Steps to Reproduce:**  
1. Send POST request to `/pet` with `"id"` field set as a string (e.g., `"id": "invalid_id"`)  
2. Observe the response status code  

**Expected Result:**  
- API should return 400 Bad Request indicating invalid input type  

**Actual Result:**  
- API returns 500 Internal Server Error  

**Impact:**  
- Server crashes on invalid input, indicating poor input validation and robustness  

---

## Bug #3: API returns 200 OK when deleting a non-existent pet

**Severity:** Medium  
**Priority:** P2  

**Steps to Reproduce:**  
1. Send DELETE request to `/pet/{petId}` with a pet ID that does not exist (e.g., `99999999`)  
2. Observe the response status code  

**Expected Result:**  
- API should return 404 Not Found or 400 Bad Request indicating the pet does not exist  

**Actual Result:**  
- API returns 200 OK  

**Impact:**  
- Misleading success response for deletion of non-existent resource, which can cause confusion and errors in client applications  

---

## Bug #4: API returns 404 Not Found instead of 400 Bad Request for invalid pet ID format on DELETE

**Severity:** Low  
**Priority:** P3  

**Steps to Reproduce:**  
1. Send DELETE request to `/pet/{petId}` with an invalid ID format (e.g., string `"invalid_id"`)  
2. Observe the response status code  

**Expected Result:**  
- API should return 400 Bad Request indicating invalid ID format  

**Actual Result:**  
- API returns 404 Not Found  

**Impact:**  
- Response code does not accurately reflect the error cause, which may affect error handling logic  

