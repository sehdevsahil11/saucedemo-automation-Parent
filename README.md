
🧪 E-Commerce Test Automation Project – SauceDemo

This project automates core end-to-end test scenarios for [SauceDemo](https://www.saucedemo.com/), a sample e-commerce web app, using Python, Selenium, and Pytest.

---

📌 Project Goals

- Demonstrate ability to build a clean automation framework
- Cover both positive and negative test scenarios
- Use PyTest + Selenium for UI test coverage
- Structure code using Page Object Model (POM)

---

✅ Features Covered

| Feature                | Test Type     | Status |
|------------------------|---------------|--------|
| Login (valid/invalid)  | Manual + Auto | ✅     |
| Product Listing Page   | Manual + Auto | ✅     |
| Product Details Page   | Manual + Auto | ✅     |
| Cart Add/Remove        | Manual + Auto | ✅     |
| Checkout Flow          | Manual + Auto | ✅     |
| Logout Functionality   | Manual + Auto | ✅     |

---

🧰 Tech Stack

- Python 3.9
- Selenium
- PyTest
- Page Object Model
- Git + GitHub

---


📦 Installation Instructions

1. Clone the repository:

   git clone https://github.com/your-username/saucedemo-automation.git  
   cd saucedemo-automation

2. Set up virtual environment:

   python -m venv venv  
   source venv/bin/activate     # macOS/Linux  
   venv\Scripts\activate        # Windows

3. Install dependencies:

   pip install -r requirements.txt

---

🚀 How to Run UI Tests

   pytest tests/ui_tests/test_saucedemo.py -v

---

📁 Project Structure

automation/
│
├── pages/
│ ├── login_page.py
│ ├── inventory_page.py
│ ├── cart_page.py
│ ├── checkout_page.py
│ └── product_details_page.py
│
├── tests/
│ ├── test_login.py
│ ├── test_cart.py
│ ├── test_checkout.py
│ ├── test_product_details.py
│ └── test_logout.py
│
├── README.md
└── requirements.txt

---

📄 Documentation

- 📌 [TEST-STRATEGY.md](./TEST-STRATEGY.md): Testing scope and goals
- 📌 [TEST-PLAN.md](./TEST-PLAN.md): Feature coverage and approach
- 📌 [EXERCISE-1.md](./EXERCISE-1.md): Detailed test cases
- 📌 [BUGREPORT-1.md](./BUGREPORT-1.md): UI bugs with severity and priority

---


👤 Author

Sahil Sehdev
QA Engineer | Python | Selenium | Test Automation

