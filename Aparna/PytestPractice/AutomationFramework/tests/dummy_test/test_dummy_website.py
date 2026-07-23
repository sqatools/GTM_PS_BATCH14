import time

import pytest
from selenium import webdriver
from ...page_objects.dummy_page.dummy_page import DummyPage
from ...page_objects.dummy_page.dummy_page_data import website_url, firstname_value, lastname_value

@pytest.fixture(scope="class")
def get_driver(request):
    driver = webdriver.Chrome()
    driver.maximize_window()
    #request is a special object that is used to access the fixture
    # context and request information about the test being executed. 
    # It is passed as an argument to the fixture function and can be used to 
    # ssaccess the test class, test method, and other information about the test being executed.
    request.cls.driver = driver
    yield driver
    driver.quit()

@pytest.mark.usefixtures("get_driver")
class TestDummyWebsite:
    #get_driver fixture is used to initialize the driver and
    # pass it to the test class
    #initialize the DummyPage class in setup method to use it in test method
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, get_driver):
        self.dp = DummyPage(get_driver)
    #def setup(self): other way  to use fixture to initialize the DummyPage class
    #    self.dp = DummyPage(self.driver)

        
    def test_provide_user_details(self):
        #coming from data file dummy_page_data.py

        self.dp.launch_website(url=website_url)
        self.dp.enter_first_name(firstname_value)
        self.dp.enter_last_name(lastname_value)
        time.sleep(5)
        
        
        #self.dp.launch_website(url=website_url)
        #self.dp.enter_first_name(first_name_value)
        #self.dp.enter_last_name(last_name_value)
        #time.sleep(5)

        