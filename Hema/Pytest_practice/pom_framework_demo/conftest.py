import pytest
from selenium import webdriver


# fixture to initialize the WebDriver and provide it to test classes
@pytest.fixture(scope="class")
def get_driver(request):# request- to access the requesting test class
    driver = webdriver.Chrome()
    driver.maximize_window
    request.cls.driver = driver # assigning the driver to the test class so that it can be used in test methods
    # request.cls allows access to apis of the test class and assigning the driver to it

    yield
    driver.quit

    