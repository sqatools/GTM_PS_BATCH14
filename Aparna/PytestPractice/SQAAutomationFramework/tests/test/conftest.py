#drivers
from selenium import webdriver
import pytest

#fixture to get the driver instance and provide it to the test class
@pytest.fixture(scope="class")
def get_driver(request):
    driver = webdriver.Chrome()
    driver.maximize_window()
    request.cls.driver = driver
    yield driver
    driver.quit()