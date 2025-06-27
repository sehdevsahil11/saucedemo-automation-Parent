# Decisions and Reasons

## Choice of Programming Language and Framework

- **Python** was chosen due to its simplicity and its use in Droneshield.  
- **PyTest** framework was selected for its easy syntax, powerful features, and integration capabilities.  
- **Selenium WebDriver** was used for browser automation because it supports all major browsers and is widely adopted.

## Test Design Approach

- Tests are designed to be modular and reusable to reduce maintenance.  
- Page Object Model (POM) pattern is recommended to separate test logic and UI locators.  
- Data-driven testing approach will be used where multiple inputs need to be tested.

## Tools and Technologies

- Using **GitHub** for version control to manage code and documentation.  
- Planning for CI/CD integration via **GitHub Actions** in future for automation execution.

## Risk Management

- Chose stable selectors to minimize test breakage due to UI changes.  
- Manual verification will be done periodically to ensure automated tests remain relevant.

