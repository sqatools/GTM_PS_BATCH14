
import time
import pytest
from selenium import webdriver

from selenium.webdriver.common.by import By
@pytest.mark.usefixtures("get_instance_request")

class TestLoginFeature:
    #def test_login(self, get_instance):
     #   self.driver = get_instance
    def test_login(self, request):
        print("Test Name : ", request.node.name)
        self.driver.find_element("id", "username").send_keys("SQATools")
        self.driver.find_element("id", "password").send_keys("SQATools@123")
        address = self.driver.find_element("id", "address")
        address.clear()
        address.send_keys("Hyderabad")
        time.sleep(5)

    #def test_verify_radiobutton(self, get_instance):
    def test_verify_radio_button(self, request):
        #self.driver = get_instance
        radio_button = self.driver.find_element("id", "male")
        assert radio_button.is_displayed(), "Radio button not displayed"
        assert radio_button.is_enabled(), "Radio button is not enabled"
        assert not radio_button.is_selected(), "Radio button is already selected"
        radio_button.click()
        assert radio_button.is_selected()

        female_button=self.driver.find_element("id", "female")
        assert  not female_button.is_selected(), "Radio button is selected"
        female_button.click()
        assert female_button.is_selected(), "Radio button is selected"
        
        checkbox_check=self.driver.find_element(By.XPATH, "//input[@value='Java']")
        checkbox_check.click()
        assert checkbox_check.is_selected()
        time.sleep(4)

        