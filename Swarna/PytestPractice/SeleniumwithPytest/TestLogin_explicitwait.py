import pytest 
import time
from Deepesh.PytestPractice.SeleniumwithPytest.Selenium_Base import SeleniumAction




@pytest.mark.usefixtures("get_instance_module")
class TestLoginFature:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self):
      self.action_obj = SeleniumAction(self.driver)


    def test_login_and_verify():
       




   





    