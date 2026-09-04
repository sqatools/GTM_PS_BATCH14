import logging
import os
from datetime import datetime
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.select import Select

#selenium actions

class SeleniumBase:
    #constructor required a parameter
    #when we create aobject the parameter of constructor is provide
    def __init__(self, driver):
        self.driver = driver
        self.create_log_dir()
        # Initialize explicit WebDriverWait with a timeout of 20 seconds
        self.wait = WebDriverWait(self.driver, 20)
        self.logger = logging.getLogger(__name__)
        
        #iflog folderis not presentit willcreate
    def create_log_dir(self):
        curr_path = os.getcwd()
        logs_path = os.path.join(curr_path, "logs")
        if not os.path.exists(logs_path):
            os.mkdir(logs_path)
        
    def take_screenshot(self):
        new_name = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
        file_name = f"{new_name}_image.png"
        #getcwd means current working directory
        logs_dir = os.path.join(os.getcwd(), "logs")
        os.makedirs(logs_dir, exist_ok=True)
        file_path = os.path.join(logs_dir, file_name)
        self.logger.info(f"screenshot path : {file_path}")
        self.driver.save_screenshot(file_path)
        return file_path

        
    def get_element(self, locator):
        """
        Docstring for get_element
        :param self: Description
        :param locator: locator value will provide in tuple format (By.ID, "id_value")
        :return: WebElement
        """
        try:
            self.logger.info(f"getting element with locator : {locator}")
            elem = self.wait.until(ec.presence_of_element_located(locator))
            return elem
        except Exception as e:
            self.take_screenshot()
            self.logger.info(f"unable to find element :{locator}")
            self.logger.error(f"{e}")
            #raise
    """
    def get_element(self, locator):
        
        try:
            self.logger.info(f"Getting Element found: {locator}")
        except Exception as e:
            #created randomfile name with date and time
            file_name=f"{datetime.now().strftime('%Y_%m_%d_%H_%M_%S')}_image.png"
            file_path=os.path.join(os.getcwd(),f"logs/{file_name}")
            self.logger.info(f"Screenshot path: {file_path}")
            self.driver.save_screenshot(file_path)
            self.logger.info(f"Screenshot saved at: {file_path}")
            self.logger.info(f"Error occurred while getting element: {locator}. Exception: {e}")
            
        elem = self.wait.until(ec.presence_of_element_located(locator))
        
        return elem
    """
    
    def click_element(self, locator):
        """
        Docstring for click_element
        :param self: Description
        :param locator: locator value will provide in tuple format (By.ID, "id_value")
        :return: None
        """
        
        elem = self.get_element(locator)
        self.logger.info(f"Clicking Element: {locator}")
        elem.click()

    def enter_text(self, locator, value):
        """
        Docstring for enter_text
        :param self: Description
        :param locator: locator value will provide in tuple format (By.ID, "id_value")
        :param text: text to be entered in the input field
        :return: None
        """
        self.logger.info(f"Entering text '{value}' into Element: {locator}")
        elem = self.get_element(locator)
        elem.clear()
        elem.send_keys(value)
        
    def get_text(self, locator):
        """
        Docstring for get_text
        :param self: Description
        :param locator: locator value will provide in tuple format (By.ID, "id_value")
        :return: text of the element
        """
        element = self.get_element(locator)
        return element.text

    def get_elements(self, locator):
        elems = self.wait.until(ec.presence_of_all_elements_located(locator))
        return elems
    
    def get_element_text(self, locator):
        elem = self.get_element(locator)
        return elem.text
    

    def select_dropdown(self, locator, value): 
        elem = self.get_element(locator)
        select = Select(elem)
        select.select_by_visible_text(value)

    def is_element_selected(self, locator):
        """
        Docstring for is_element_selected
        :param self: Description
        :param locator: locator value will provide in tuple format (By.ID, "id_value")
        :return: True if element is selected, False otherwise
        """
        elem = self.get_element(locator)
        self.logger.info(f"Checking if Element is selected: {locator}:{elem.is_selected()}")
        return elem.is_selected()
    
    def upload_file(self, locator, file_path):
        """
        Docstring for upload_file
        :param self: Description
        :param locator: locator value will provide in tuple format (By.ID, "id_value")
        :param file_path: path of the file to be uploaded
        :return: None
        """
        elem = self.get_element(locator)
        self.logger.info(f"Uploading file '{file_path}' to Element: {locator}")
        #elem.clear()
        elem.send_keys(file_path)
    
    


    
