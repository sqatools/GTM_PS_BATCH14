import pytest 
import time


@pytest.mark.usefixtures("get_instance_request")
class TestLoginFature:

    def test_login_and_verify(self, request):
        print("Test Name : ", request.node.name) # request.node.name will give the name of the test case which is currently executing i.e. test_login_and_verify
        self.driver.find_element("id", "username").send_keys("SQATools")
        self.driver.find_element("id", "password").send_keys("SQATools@123")
        address = self.driver.find_element("id", "address")
        address.clear()
        address.send_keys("Bangalore")
        time.sleep(5)

    def test_verify_radio_button(self, request):
        print("Test Name : ", request.node.name)
        radio_button = self.driver.find_element("id", "male")
        assert radio_button.is_displayed(), "Radio button is not displayed"
        assert radio_button.is_enabled(), "Radio button is not enabled"
        assert not radio_button.is_selected(), "Radio button is already selected"
        radio_button.click()
        assert radio_button.is_selected(), "Radio button is not selected after clicking"

        female = self.driver.find_element("id", "female")
        assert female.is_displayed(), "Female radio button is not displayed"
        time.sleep(5)

"""
When you define request in () then u dont have to define any variable to call the instance from config file
and you can directly call the instance by using self.driver because 
we have assigned the driver instance to the class variable in config file
and that variable is self.driver in this class.
"""        