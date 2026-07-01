import pytest
#from selenium import webdriver

from selenium.webdriver.common.by import By
from Operation_class import SeleniumAction
#imported the class

@pytest.mark.usefixtures("get_instance_module")
class TestLoginFeature:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self):
        self.action_obj=SeleniumAction(self.driver)
        #self. class parameter,this get_instance_request fixture is providing
        # action is a instance variable
        #for accessing class we need  to create object
	


