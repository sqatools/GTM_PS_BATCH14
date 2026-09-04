
import pytest
from selenium import webdriver

@pytest.fixture(scope="class")
def  get_driver(request):
    driver=webdriver.Chrome()
    driver.maximize_window()
    request.cls.driver=driver
    yield driver
    driver.quit()
    #request is a special object that is used to access the fixture
    # context and request information about the test being executed.
    #cls is a special attribute of the request
    # object that refers to the test class that is currently being executed.
    #driver is assigned to the cls.driver attribute of the request object, 
    # which allows the test class to access the driver instance created in the fixture.
   
    
    