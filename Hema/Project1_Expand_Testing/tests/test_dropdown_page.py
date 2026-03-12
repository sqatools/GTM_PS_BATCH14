from page_objects.dropdown_page.dropdown_page_locator import DropdownPageLocator
from page_objects.dropdown_page.dropdown_page import DropdownPage
from page_objects.dropdown_page.dropdown_page_data import *
import pytest
import time


@pytest.mark.usefixtures("get_driver")
#Indicates that this test class will use a fixture named get_driver.
#Usually, get_driver is defined elsewhere to initialize a Selenium WebDriver (like Chrome or Firefox).
#This allows self.driver to be available in the tests.
class TestDropdownPage:

    @pytest.fixture(scope="function", autouse=True)
#In pytest, a fixture is a way to set up preconditions before running a test and optionally clean up after the test.
#scope="function" means the fixture will run once for each test function.
# autouse=-true will automatically run this fixture for every test function in the class without needing to explicitly call it.
    def setup(self):
        self.test_dropdown = DropdownPage(self.driver)

    def test_dropdown_page(self):
        self.test_dropdown.launch_website(website_url)
        self.test_dropdown.select_dropdown_option(option1)
        time.sleep(5)
        self.test_dropdown.select_elements_per_page(elements_per_page)
        time.sleep(5)
        self.test_dropdown.select_country(country_name)
        time.sleep(5)
        
        
        #by index value
        # self.test_dropdown.select_dropdown_option(option11)
        #self.test_dropdown.select_elements_per_page(elements_per_page_1)
        #self.test_dropdown.select_country(country_name_1)
        #time.sleep(5)
    