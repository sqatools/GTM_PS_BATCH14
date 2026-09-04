import logging
import os
from datetime import datetime
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select


class SeleniumBase:
    def __init__(self, driver):
        self.driver = driver
        self.create_log_dir()
        # Initialize explicit WebDriverWait with a timeout of 20 seconds
        self.wait = WebDriverWait(self.driver, 20)
        self.log  = logging.getLogger(__name__)

    def create_log_dir(self):
        curr_path = os.getcwd()
        logs_path = os.path.join(curr_path, "logs")
        if not os.path.exists(logs_path):
            os.mkdir(logs_path)

    def take_screenshot(self):
        file_name = f"{datetime.now().strftime("%Y_%m_%d_%H_%M_%S")}_image.png"
        file_path = os.path.join(os.getcwd(), f"logs\{file_name}")
        self.log.info(f"screenshot path : {file_path}")
        self.driver.save_screenshot(file_path)


    def get_element(self, locator):
        """
        Docstring for get_element
        :param self: Description
        :param locator: locator value will provide in tuple format (By.ID, "id_value")
        :return: WebElement
        """
        try:
            self.log.info(f"getting element with locator : {locator}")
            return self.wait.until(EC.presence_of_element_located(locator))
        except Exception as e:
            self.take_screenshot()
            self.log.info(f"unable to find element :{locator}")
            self.log.error(f"{e}")
            
    
    def click_element(self, locator):
        """
        Docstring for click_element
        :param self: Description
        :param locator: locator value will provide in tuple format (By.ID, "id_value")
        :return: None
        """
        element = self.get_element(locator)
        self.log.info(f"clicking on element : {locator}")
        element.click()

    def enter_text(self, locator, text):
        """
        Docstring for enter_text
        :param self: Description
        :param locator: locator value will provide in tuple format (By.ID, "id_value")
        :param text: text to be entered in the input field
        :return: None
        """
        element = self.get_element(locator)
        element.clear()
        self.log.info(f"entering text on element  {text}: {locator}")
        element.send_keys(text)

    def get_text(self, locator):
        """
        Docstring for get_text
        :param self: Description
        :param locator: locator value will provide in tuple format (By.ID, "id_value")
        :return: text of the element
        """
        element = self.get_element(locator)
        return element.text

    def is_element_selected(self, locator):
        """
        Docstring for is_element_selected
        :param self: Description
        :param locator: locator value will provide in tuple format (By.ID, "id_value")
        :return: True if element is selected, False otherwise
        """
        element = self.get_element(locator)
        self.log.info(f"element status is {locator}: {element.is_selected}")
        return element.is_selected()
    

    def select_dropdown_option(self, dropdown_locator, option_text):
        """
        Docstring for select_dropdown_option
        :param self: Description
        :param dropdown_locator: locator value for the dropdown element in tuple format (By.ID, "id_value")
        :param option_text: visible text of the option to be selected
        :return: None
        """
        dropdown_element = self.get_element(dropdown_locator)
        select = Select(dropdown_element)
        select.select_by_visible_text(option_text)


    def upload_file(self, locator, file_path):
        """
        Docstring for upload_file
        :param self: Description
        :param locator: locator value for the file input element in tuple format (By.ID, "id_value")
        :param file_path: absolute path of the file to be uploaded
        :return: None
        """
        file_input_element = self.get_element(locator)
        file_input_element.send_keys(file_path)