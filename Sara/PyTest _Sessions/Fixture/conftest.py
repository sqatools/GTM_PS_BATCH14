from selenium import webdriver
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
    request.cls.driver = driver_instance ## .driver is a variable and can be any name, we are assigning that variable to variable define inside () of the class
    driver_instance.quit()