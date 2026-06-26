
import pytest
from selenium import webdriver





@pytest.fixture(scope='class')
def get_instance():
    driver_instance=webdriver.Chrome()
    driver_instance.maximize_window()
    driver_instance.implicitly_wait(10)
    driver_instance.get("https://sqatools.in/automation-practice-page/")
    
    yield driver_instance
    
    driver_instance.quit()
    
    
#request--It will get the test case name which testcase is going to execute we will know 
# and cls
@pytest.fixture(scope='class')
def get_instance_request(request):
    driver_instance=webdriver.Chrome()
    driver_instance.maximize_window()
    driver_instance.implicitly_wait(10)
    driver_instance.get("https://sqatools.in/automation-practice-page/")
    #Assigng the driver instance to the class variable
    request.cls.driver=driver_instance
    #driver can write as anything 
    yield 
    
    driver_instance.quit()

 