# 🧪 QA Automation Project – Saucedemo + Petstore API

This repository contains automated tests for both a web-based e-commerce application and a REST API service. The goal of this project is to demonstrate strong QA fundamentals through manual and automated test design, implementation, and execution using Python and PyTest.

---

## 📂 Project Structure

automation/
│
├── tests/
│   ├── ui_tests/
│   └── api_tests/
│
├── requirements.txt
├── README.md
├── TEST-STRATEGY.md
├── TEST-PLAN.md
├── EXERCISE-1.md
├── EXERCISE-2.md
├── BUGREPORT-1.md
└── BUGREPORT-2.md

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

### ✅ UI Tests – Exercise 1

   pytest tests/ui_tests/test_saucedemo.py -v

### ✅ API Tests – Exercise 2

   pytest tests/api_tests/test_petstore_api.py -v

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


