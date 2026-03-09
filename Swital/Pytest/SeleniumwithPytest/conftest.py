from selenium import webdriver
from selenium.webdriver.common.by import By

import pytest   

@pytest.fixture(scope="class")
def get_instance():
    driver_instance = webdriver.Chrome()
    driver_instance.get("https://sqatools.in/automation-practice-page/")
    driver_instance.maximize_window()
    driver_instance.implicitly_wait(15)
    yield driver_instance
    driver_instance.quit()

@pytest.fixture(scope="class")
def get_instance_request(request):
    driver_instance = webdriver.Chrome()
    driver_instance.get("https://sqatools.in/automation-practice-page/")
    driver_instance.maximize_window()
    driver_instance.implicitly_wait(15)
    # Assigning the driver instance to the class variable
    request.cls.driver = driver_instance
    yield 
    driver_instance.quit()