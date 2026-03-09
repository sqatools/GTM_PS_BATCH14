import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# The @pytest.fixture should be outside the class 
# because of how pytest discovers and scopes fixtures.
# Why fixtures are outside classes:

# pytest fixture scope — fixtures are module-level or session-level resources, not instance methods
# Fixture discovery — pytest scans for @pytest.fixture at the module level during test collection
# Reusability — a fixture outside the class can be used by multiple test classes
# Convention — pytest best practice is to define fixtures at module scope, above test classes

# pytest test_val_class.py::TestValidation::test_login_automation_ui -v   

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.maximize_window()
    driver.get("https://sqatools.in/automation-practice-page/")
    yield driver
    driver.quit()


class TestValidation:
    """Test class for automation practice page validation."""
    
    @pytest.mark.parametrize("username, password, address", [
        ("admin", "admin123", "123 Main St"),
        ("user1", "pass1", "456 Elm St"),
        ("testuser", "testpass", "789 Oak St")
    ])
    def test_login_automation_ui(self, driver, username, password, address):
        """Test login with parametrized credentials and address."""
        username_field = driver.find_element(By.ID, "username")
        username_field.send_keys(username)
        
        password_field = driver.find_element(By.ID, "password")
        password_field.send_keys(password)
        
        enter_address = driver.find_element(By.ID, "address")
        enter_address.clear()
        enter_address.send_keys(address)
        
        time.sleep(2)
        assert driver.current_url == "https://sqatools.in/automation-practice-page/"

    
    def test_radio_buttons(self, driver):
        """Test selecting radio buttons for gender field."""
        # Locate radio buttons by ID
        radio_male = driver.find_element(By.ID, "male")
        radio_female = driver.find_element(By.ID, "female")
        radio_other = driver.find_element(By.ID, "other")
        
        # Test selecting Male
        radio_male.click()
        time.sleep(5)
        assert radio_male.is_selected()
        
        # Test selecting Female
        radio_female.click()
        time.sleep(5)
        assert radio_female.is_selected()
        assert not radio_male.is_selected()  # Male should be deselected
        
        # Test selecting Other
        radio_other.click()
        time.sleep(5)
        assert radio_other.is_selected()
        assert not radio_female.is_selected()  # Female should be deselected