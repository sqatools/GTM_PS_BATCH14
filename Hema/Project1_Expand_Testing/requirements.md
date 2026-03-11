# Project1_Expand_Testing - Requirements Documentation

## Project Overview
This is a Selenium-based web automation testing project for the Expand Testing website. The project uses Page Object Model (POM) design pattern to create maintainable and reusable test automation code.

## Prerequisites
- Python 3.8 or higher
- Chrome browser installed
- Internet connection for downloading webdrivers

## Dependencies

### Core Dependencies
- **selenium==4.15.2**: Web automation framework for browser control
- **pytest==9.0.2**: Testing framework for running test cases
- **pluggy==1.6.0**: Plugin for pytest HTML reporting
- **webdriver-manager==4.0.1**: Automatic webdriver management

## Installation

### 1. Clone or navigate to the project directory
```bash
cd /path/to/Project1_Expand_Testing
```

### 2. Create virtual environment (recommended)
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Verify installation
```bash
python -c "import selenium; print('Selenium version:', selenium.__version__)"
pytest --version
```

## Project Structure
```
Project1_Expand_Testing/
├── base/                          # Base classes and utilities
│   └── selenium_base.py          # Selenium base class with common methods
├── page_objects/                  # Page Object Model classes
│   ├── login_page/               # Login page objects
│   │   ├── login_page.py         # Login page methods
│   │   ├── login_page_data.py    # Test data for login
│   │   └── login_page_locator.py # Element locators for login
│   └── web_inputs_page/          # Web inputs page objects
│       ├── web_inputs_page.py    # Web inputs page methods
│       ├── web_input_data.py     # Test data for web inputs
│       └── web_inputs_locator.py # Element locators for web inputs
├── tests/                        # Test files
│   ├── test_login_page.py        # Login page tests
│   └── test_web_inputs.py        # Web inputs tests
├── logs/                         # Screenshot logs (auto-generated)
├── requirements.txt              # Python dependencies
├── requirements.md               # This documentation file
├── pytest.ini                    # Pytest configuration
└── venv/                         # Virtual environment (created during setup)
```

## Running Tests

### Run all tests
```bash
python -m pytest -v
```

### Run specific test file
```bash
python -m pytest tests/test_login_page.py -v
python -m pytest tests/test_web_inputs.py -v
```

### Run with HTML report
```bash
python -m pytest --html=reports/report.html --self-contained-html
```

### Run tests in parallel (if pytest-xdist is installed)
```bash
pip install pytest-xdist
python -m pytest -n 2
```

## Browser Support
- Chrome (primary)
- Firefox (with webdriver-manager)
- Edge (with webdriver-manager)

## Configuration

### Pytest Configuration (pytest.ini)
```ini
[pytest]
addopts = -v --tb=short
testpaths = tests
python_files = test_*.py
python_classes = Test*
python_functions = test_*
```

### WebDriver Management
The project uses webdriver-manager for automatic webdriver downloads. No manual webdriver setup required.

## Test Data
Test data is stored in separate data files:
- `login_page_data.py`: Contains login credentials and URLs
- `web_input_data.py`: Contains input values for web inputs tests

## Logging and Screenshots
- Screenshots are automatically captured on test failures
- Saved in `logs/` directory with timestamp
- Format: `YYYY_MM_DD_HH_MM_SS_image.png`

## Contributing
1. Follow Page Object Model pattern
2. Add new page objects in `page_objects/` directory
3. Create corresponding test files in `tests/` directory
4. Update locators and data files as needed
5. Run tests before committing

## Troubleshooting

### Common Issues
1. **WebDriver not found**: webdriver-manager should handle this automatically
2. **Chrome not starting**: Ensure Chrome browser is installed
3. **Import errors**: Activate virtual environment and install dependencies
4. **Element not found**: Check locators in locator files

### Debug Mode
```bash
# Run with detailed output
python -m pytest -v -s

# Run single test with debug
python -m pytest tests/test_login_page.py::TestLoginPage::test_login_page -v -s
```

## Version History
- v1.0.0: Initial setup with login and web inputs tests
- Dependencies updated to latest stable versions

## Contact
For questions or issues, please check the test output or review the code structure.