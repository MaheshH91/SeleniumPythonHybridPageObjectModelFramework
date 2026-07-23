# SeleniumPythonHybridPageObjectModelFramework
# Selenium Python Hybrid Page Object Model Framework

A Hybrid Test Automation Framework built using **Python, Selenium WebDriver, Pytest, Page Object Model (POM), Data-Driven Framework (DDF), Allure Reports, and Jenkins**.

---

## Project Overview

This framework is designed to automate web applications using industry best practices. It supports:

- Page Object Model (POM)
- Data-Driven Testing using Excel
- Cross Browser Testing
- Pytest Fixtures
- Logging
- HTML & Allure Reports
- Screenshot Capture on Failure
- Jenkins CI/CD Integration
- Headless Execution
- Reusable Utility Classes

---

## Tech Stack

| Technology | Description |
|------------|-------------|
| Python | Programming Language |
| Selenium WebDriver | Browser Automation |
| Pytest | Test Framework |
| OpenPyXL | Excel Data Handling |
| Allure | Test Reporting |
| Git & GitHub | Version Control |
| Jenkins | Continuous Integration |

---

## Project Structure

```
SeleniumPythonHybridPageObjectModelFramework
│
├── configurations
│   ├── config.ini
│
├── ExcelFiles
│   └── TutorialsNinja.xlsx
│
├── pages
│   ├── BasePage.py
│   ├── HomePage.py
│   ├── LoginPage.py
│   ├── RegisterPage.py
│   ├── SearchPage.py
│   ├── AccountPage.py
│   └── AccountSuccessPage.py
│
├── tests
│   ├── BaseTest.py
│   ├── conftest.py
│   ├── test_Login.py
│   ├── test_Register.py
│   └── test_Search.py
│
├── utilities
│   ├── ExcelUtils.py
│   ├── logger.py
│   └── ReadConfigurations.py
│
├── Reports
├── logs
├── screenshots
├── allure-results
├── allure-report
│
├── requirements.txt
├── pytest.ini
├── .gitignore
└── README.md
```

---

# Framework Features

- Hybrid Framework
- Page Object Model (POM)
- Data-Driven Testing (Excel)
- Cross Browser Support
- Chrome
- Edge
- Firefox
- Headless Execution
- Explicit Waits
- Logging
- HTML Report
- Allure Report
- Screenshot on Failure
- Jenkins Ready
- GitHub Ready

---

# Installation

## Clone Repository

```bash
git clone https://github.com/<your-github-username>/SeleniumPythonHybridPageObjectModelFramework.git
```

Move to project directory

```bash
cd SeleniumPythonHybridPageObjectModelFramework
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# Run Tests

Run all tests

```bash
pytest
```

Run Login Tests

```bash
pytest tests/test_Login.py
```

Run Register Tests

```bash
pytest tests/test_Register.py
```

Run Search Tests

```bash
pytest tests/test_Search.py
```

---

# Run by Marker

Smoke

```bash
pytest -m smoke
```

Sanity

```bash
pytest -m sanity
```

Regression

```bash
pytest -m regression
```

---

# Cross Browser Execution

Chrome

```bash
pytest --browser chrome
```

Edge

```bash
pytest --browser edge
```

Firefox

```bash
pytest --browser firefox
```

---

# Headless Execution

```bash
pytest --browser chrome --headless
```

---

# Reports

## HTML Report

Generated automatically inside

```
Reports/
```

## Allure Report

Generate report

```bash
allure serve allure-results
```

or

```bash
allure generate allure-results --clean -o allure-report
```

Open report

```bash
allure open allure-report
```

---

# Screenshots

Whenever a test fails, screenshots are automatically captured and stored in:

```
screenshots/
```

---

# Logging

Execution logs are stored in

```
logs/
```

---

# Test Data

Excel test data is maintained in

```
ExcelFiles/
```

using

```
TutorialsNinja.xlsx
```

---

# Configuration

Application configurations are stored in

```
configurations/config.ini
```

Example

```ini
[commonInfo]
baseURL=https://tutorialsninja.com/demo
email=test@gmail.com
password=Password123
```

---

# Browser Support

- Google Chrome
- Microsoft Edge
- Mozilla Firefox

---

# Jenkins Integration

This framework supports Jenkins Continuous Integration.

Typical Jenkins Build Step

```bash
pip install -r requirements.txt
pytest
```

Reports and screenshots are generated automatically after execution.

---

# Best Practices Followed

- Page Object Model
- Reusable Components
- Explicit Waits
- Centralized Configuration
- Data-Driven Testing
- Exception Handling
- Logging
- Reporting
- Screenshot on Failure
- CI/CD Ready

---

# Future Enhancements

- Parallel Execution using pytest-xdist
- Selenium Grid
- Docker Integration
- GitHub Actions
- Database Validation
- API Automation
- Email Reporting
- Azure DevOps Pipeline

---

# Author

**Mahesh Holkar**

**Senior Automation Test Engineer**

### Skills

- Python
- Selenium WebDriver
- Pytest
- Page Object Model
- Data-Driven Framework
- Jenkins
- Git & GitHub
- SQL
- API Testing
- Manual Testing

---

## Connect with Me

GitHub: https://github.com/MaheshH91


---

## License

This project is for learning, demonstration, and automation practice purposes.