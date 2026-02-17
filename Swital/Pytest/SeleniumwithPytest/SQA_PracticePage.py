import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time


@pytest.mark.usefixtures("get_instance_request")
class TestRadioButton:
    #driver: WebDriver

    def test_radio_button_clickandenable(self, request):
        print("Test Name : ", request.node.name)
        male_btn = self.driver.find_element(By.ID, "male")
        male_btn.click()
        assert male_btn.is_selected(), "Male button is selected"

        female_btn = self.driver.find_element(By.ID, "female")
        female_btn.click()
        assert female_btn.is_selected(), "Female button is selected"

        other_btn = self.driver.find_element(By.ID, "other")
        other_btn.click()
        assert other_btn.is_selected(), "Other button is selected"

        time.sleep(0.5)

    def test_chechbox_Verify_Click(self, request):  
        print("Test Name : ", request.node.name)  
        java_checkbox = self.driver.find_element(By.ID, "java")
        java_checkbox.click()
        assert java_checkbox.is_selected(), "Java checkbox should be selected"

        python_checkbox = self.driver.find_element(By.ID, "python")
        python_checkbox.click()
        assert python_checkbox.is_selected(), "Python checkbox should be selected"

        selenium_checkbox = self.driver.find_element(By.ID, "selenium")
        selenium_checkbox.click()
        assert selenium_checkbox.is_selected(), "Selenium checkbox should be selected"

    def test_single_dropDown_select(self, request):
        dropdown_select = self.driver.find_element(By.ID, "country")
        select_obj = Select(dropdown_select)
        select_obj.select_by_index(2)