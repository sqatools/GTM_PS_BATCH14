from selenium import webdriver
import pytest

# fixture to initialize the WebDriver and provide it to test classes
@pytest.fixture(scope="class")
def get_driver(request):
    driver = webdriver.Chrome()
    driver.maximize_window()
    # class variable as driver, that we can 
    # access inside as self.driver
    request.cls.driver = driver
    yield
    driver.quit()