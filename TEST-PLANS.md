# Test Plans for Saucedemo Automation Project

## 1. Login Feature

### Objective
Verify that users can log in successfully and invalid login attempts are handled gracefully.

### Test Scenarios
- Valid username and password  
- Invalid username  
- Invalid password  
- Blank username/password fields  
- Locked out user scenario

## 2. Product Listing and Filtering

### Objective
Ensure products display correctly, and filters work as expected.

### Test Scenarios
- Products display on listing page  
- Sorting products by name or price  
- Filtering products by categories or other criteria

## 3. Cart Operations

### Objective
Validate adding and removing products from the cart works correctly.

### Test Scenarios
- Add a product to the cart  
- Remove a product from the cart  
- Verify cart updates product count and price  
- Cart persists after navigation

## 4. Checkout Process

### Objective
Ensure users can complete the checkout process successfully.

### Test Scenarios
- Fill in checkout information (name, postal code)  
- Validate error messages for missing fields  
- Complete order and confirm success message

---

## Test Execution

- Tests will be executed using PyTest automation framework  
- Results will be logged and reported

