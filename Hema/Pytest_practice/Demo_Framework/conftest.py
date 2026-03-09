#fixture file is a conftest file which is used to store all the fixtures which are used in the test cases
import pytest
from selenium import webdriver

@pytest.fixture(scope="class")
def get_driver(request):   
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://sqatools.in/automation-practice-page/")
    request.cls.driver = driver
    yield
    driver.quit()