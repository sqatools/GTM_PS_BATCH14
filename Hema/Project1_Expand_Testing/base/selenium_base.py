from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging
import os
from datetime import datetime
from selenium.webdriver.support.ui import Select

class SeleniumBase:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 20)
        self.log = logging.getLogger(__name__)

    def create_log_dir(self):
        currentpath =os.getcwd()
        logs_path = os.path.join(currentpath, "logs")
        if not os.path.exists(logs_path):
            os.mkdir(logs_path)

    def take_screenshot(self):
        file_name = f"{datetime.now().strftime('%Y_%m_%d_%H_%M_%S')}_image.png"
        file_path = os.path.join(os.getcwd(), "logs", file_name)
        self.log.info(f"screenshot path: {file_path}")
        self.driver.save_screenshot(file_path)


    def get_element(self, locator):
        try:
            self.log.info(f"getting element with locator: {locator}")
            return self.wait.until(EC.element_to_be_clickable(locator))
        except Exception as e:
            self.take_screenshot()
            self.log.info(f"unable to find element :{locator}")
            self.log.error(f"{e}")
            raise
    
    def click_element(self, locator):
        element = self.get_element(locator)
        element.click()

    def enter_text(self, locator, text):
        element = self.get_element(locator)
        element.clear()
        self.log.info(f"entering the text in the element : {locator}")
        element.send_keys(text)

    def get_text(self, locator):
        element = self.get_element(locator)
        return element.text
    
    def click_link(self, link_locator):
        link_click = self.get_element(link_locator)
        link_click.click()


    def element_is_selected(self, locator):
        element = self.get_element(locator)
        return element.is_selected()
  
    def select_dropdown(self, dropdown_locator, option_value):
        dropdown_element  = self.get_element(dropdown_locator)
        select = Select(dropdown_element)
        select.select_by_visible_text(option_value)

    def upload_file(self, locator, file_path):
        file_input_element = self.get_element(locator)
        file_input_element.send_keys(file_path)

    def switch_to_frame(self, frame_locator):
        frame_element = self.get_element(frame_locator)
        self.driver.switch_to.frame(frame_element)

    def switch_to_default_content(self):
        self.driver.switch_to.default_content() 

    def get_attribute(self, locator, attribute_name):
        element = self.get_element(locator)
        return element.get_attribute(attribute_name)