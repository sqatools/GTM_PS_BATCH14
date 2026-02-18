from selenium import webdriver
import pytest

# fixture to initialize the WebDriver and provide it to test classes
@pytest.fixture(scope="class")
def get_driver(request):  # request is an internal API of pytest to access test context
    driver = webdriver.Chrome()
    driver.maximize_window()
    request.cls.driver = driver #cls is used to access the class level attributes
    yield
    driver.quit()