"""Confest file is the base from which we will give basic details and 
 all classes within this will be using this without being called multiple time."""

from selenium import webdriver
import pytest
        

@pytest.fixture(scope="class")
def get_instance():
            driver_instance= webdriver.Chrome()
            driver_instance.get("https://sqatools.in/automation-practice-page/")
            driver_instance.maximize_window()
            driver_instance.implicitly_wait(20)
            yield driver_instance
            driver_instance.quit()



            

