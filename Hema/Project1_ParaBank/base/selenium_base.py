from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging
import os
from datetime import datetime 

class SeleniumBase:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 30)
        self.log = logging.getLogger(__name__)

    def create_log_dir(self):
        currentpath =os.getcwd
        logs_path = os.path.join(currentpath, "logs")
        if not os.path.exists(logs_path):
            os.mkdir(logs_path)

    def take_screenshot(self):
        file_name = f"{datetime.now().strftime('%Y_%m_%d_%H_%M_%S')}_image.png"
        file_path = os.path.join(os.getcwd(), f"logs\{file_name}")
        self.log.info(f"screenshot path: {file_path}")
        self.driver.save_screenshot(file_path)


    def get_element(self, locator):
        self.log.info(f"getting element with locator: {locator}")
        return self.wait.until(EC.presence_of_element_located(locator))
    
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
    
  