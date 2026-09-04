import pytest 
import time


@pytest.mark.usefixtures("get_instance")
class TestLoginFature:
    def test_login_and_verify(self, get_instance):
        driver = get_instance
        driver.find_element("id", "username").send_keys("SQATools")
        driver.find_element("id", "password").send_keys("SQATools@123")
        address = driver.find_element("id", "address")
        address.clear()
        address.send_keys("Bangalore")
        time.sleep(5)