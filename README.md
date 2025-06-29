# 🧪 QA Automation Project – Saucedemo + Petstore API

This repository contains automated tests for both a web-based e-commerce application and a REST API service. The goal of this project is to demonstrate strong QA fundamentals through manual and automated test design, implementation, and execution using Python and PyTest.

---

## 📂 Project Structure

saucedemo-automation-Parent/
│
├── automation/
│   ├── pages/                         # Page Object Model classes
│   │   ├── logout_page.py             # Logout functionality
│   │   ├── login_page.py              # Login functionality
│   │   ├── inventory_page.py          # Product listing page
│   │   ├── product_details_page.py    # Single product detail view
│   │   ├── cart_page.py               # Cart interactions
│   │   └── checkout_page.py           # Checkout workflow
│   │
│   └── tests/                         # UI test cases (Exercise 1)
│       ├── test_login.py              # Login/logout scenarios
│       ├── test_cart.py               # Add/remove items from cart
│       ├── test_checkout.py           # Checkout flow tests
│       ├── test_product_details.py    # Product detail validations
│       ├── test_logout.py             # Logout scenarios
│       └── test_filtering.py          # Product filtering tests
│
├── tests_petstore_api/               # API test cases (Exercise 2)
│   └── test_petstore_api.py          # CRUD operations on /pet endpoint
│
├── EXERCISE-1.md
├── EXERCISE-2.md
├── BUGREPORT-1.md
├── BUGREPORT-2.md
├── TEST-PLAN.md
├── TEST-STRATEGY.md
├── README.md
└── requirements.txt


---

## ✅ Tech Stack

- Language: Python 3.8+
- Test Framework: PyTest
- UI Automation: Selenium WebDriver
- API Testing: requests

---

## 📦 Installation Instructions

1. Clone the repository:

   git clone https://github.com/your-username/qa-automation-project.git  
   cd qa-automation-project

2. Create and activate virtual environment:

   python -m venv venv  
   source venv/bin/activate     # macOS/Linux  
   venv\Scripts\activate        # Windows

3. Install dependencies:

   pip install -r requirements.txt

---

## 🚀 How to Run Tests

### ✅ Run all UI tests for SauceDemo – Exercise 1

   pytest automation/tests/ -v


### ✅ Run all Petstore API tests – Exercise 2

   pytest tests_petstore_api/ -v


---

## 🧪 Exercise 1 – UI Automation for Saucedemo

URL: https://www.saucedemo.com

Covers login, product listings, filters, cart, checkout, logout.

Reference files:
- EXERCISE-1.md – Test cases
- BUGREPORT-1.md – Bug report

---

## 🔗 Exercise 2 – API Testing for Swagger Petstore

API URL: https://petstore.swagger.io/v2

Covers CRUD for `/pet` endpoint, with positive and negative test cases.

Reference files:
- EXERCISE-2.md – API test cases
- BUGREPORT-2.md – Bug report

---

## 📄 Documentation

- 📌 [TEST-STRATEGY.md](./TEST-STRATEGY.md): QA scope, types of testing, tools, CI readiness
- 📌 [TEST-PLAN.md](./TEST-PLAN.md): Features under test, test approach, timeline
- 📌 [EXERCISE-1.md](./EXERCISE-1.md): UI test cases for Saucedemo
- 📌 [EXERCISE-2.md](./EXERCISE-2.md): API test cases for Petstore
- 📌 [BUGREPORT-1.md](./BUGREPORT-1.md): UI bugs with severity/priority
- 📌 [BUGREPORT-2.md](./BUGREPORT-2.md): API bugs with severity/priority

---

## 🤝 Contributions

This repo is part of a QA automation project for learning and assessment.

---

## 👤 Author

**Sahil Sehdev**  
QA Engineer | Python | Selenium | Test Automation


