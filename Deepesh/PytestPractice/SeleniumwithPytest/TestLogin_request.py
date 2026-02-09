import pytest 
import time


@pytest.mark.usefixtures("get_instance_request")
class TestLoginFature:

    def test_login_and_verify(self, request):
        print("Test Name : ", request.node.name)
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





    