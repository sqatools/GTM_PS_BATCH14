
from ...page_objects.pages.page import Page
from ...page_objects.pages.pagedata import website_url, ENTER_EMAIL, ENTER_PASSWORD, ENTER_ADDRESS
from selenium import webdriver
import pytest
import time

@pytest.fixture(scope="class")
def get_driver(request):
    driver = webdriver.Chrome()
    driver.maximize_window()
    request.cls.driver = driver
    yield driver
    driver.quit()

@pytest.mark.usefixtures("get_driver")
class TestSqatools:
    #class name always starts with capital letter and test class name 
    # should start with Test
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, get_driver):
        self.p = Page(get_driver)
        #self.p=Page(self.driver) #self.driver is the driver instance created in the fixture and passed to the test class

    def test_launch_page(self):
        self.p.get_url(website_url) #get_url is a method in Page class that takes the url as an argument and opens the url in the browser
        self.p.enter_username(ENTER_EMAIL)#enter_username is a method in Page class that takes the username as an argument and enters the username in the username field
        self.p.enter_password(ENTER_PASSWORD)#enetr_password is a method in Page class that takes the password as an argument and enters the password in the password field
        self.p.enter_address(ENTER_ADDRESS)
        self.p.click_radio_button()#click_radio_button is a method in Page class that clicks the radio button
        self.p.click_checkbox()
        self.p.click_dropdown()#click_dropdown is a method in Page class that clicks the dropdown
        time.sleep(5) #time.sleep is used to wait for the page to load completely before closing the browser
        