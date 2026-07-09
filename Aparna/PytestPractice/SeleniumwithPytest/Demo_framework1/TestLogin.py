
import time
import pytest
#from selenium import webdriver

@pytest.mark.usefixtures("get_instance_request")
class TestLoginFeature:
    #self  is by default an instance of a class
    #self is object of the class
    def test_login(self,get_instance):
        driver = get_instance
        driver.find_element("id", "username").send_keys("SQATools")
        driver.find_element("id", "password").send_keys("SQATools@123")
        address = driver.find_element("id", "address")
        address.clear()
        address.send_keys("Hyderabad")
        time.sleep(5)
        
    
        
        