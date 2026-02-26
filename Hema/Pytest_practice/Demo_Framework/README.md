# Selenium Pytest Automation Framework

## Project Description  

Generate a professional README for Selenium Pytest POM framework


## Project Structure

```
Demo_Framework/
├── tests/
│   ├── conftest.py              # Pytest fixtures and configuration
│   ├── test_login.py            # Test cases
│   └── test_dashboard.py
├── pages/
│   ├── base_page.py             # Base Page Object class
│   ├── login_page.py            # Page Object Models
│   └── dashboard_page.py
├── utilities/
│   ├── driver_factory.py         # WebDriver initialization
│   └── config.py                 # Configuration and constants
├── requirements.txt
├── pytest.ini
└── README.md
```

## Features

- **Page Object Model (POM)**: Maintainable and scalable test architecture
- **Pytest Framework**: Powerful testing with fixtures and parameterization
- **Cross-browser Support**: Chrome, Firefox, Safari configuration
- **Reporting**: HTML test reports with screenshots
- **Logging**: Comprehensive test execution logs
- **CI/CD Ready**: Easy integration with GitHub Actions, Jenkins

## Key Dependencies

- `selenium>=4.0.0` - Browser automation
- `pytest>=7.0.0` - Test framework
- `pytest-html` - HTML reporting
- `python-dotenv` - Environment variable management

## Running Tests

```bash
# Run all tests with verbose output
pytest tests/ -v

# Run with HTML report
pytest tests/ -v --html=report.html --self-contained-html

# Run tests in parallel (requires pytest-xdist)
pytest tests/ -v -n auto

# Run specific test class or method
pytest tests/test_login.py::TestLogin::test_valid_login -v
```

## Best Practices

- Keep page objects focused on UI elements and interactions
- Use explicit waits (`WebDriverWait`) instead of sleeps
- Store test data in configuration files or fixtures
- Generate reports after each test run
- Use descriptive test names and docstrings

---

**Framework Version:** 1.0  
**Last Updated:** January 2026