from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Selenium_Base :
   def __init__(self, driver):
       self.driver = driver
        # Initialize explicit WebDriverWait with a timeout of 30 seconds
       self.wait = WebDriverWait(self.driver, 30)

   def get_element(self, locator):
       """
        Docstring for get_element
        :param self: Description
        :param locator: locator value will provide in tuple format (By.ID, "id_value")
        :return: WebElement
        """
       return self.wait.until(EC.presence_of_element_located(locator))
   
   def clickon_element(self, locator):
       element = self.get_element(locator)
       element.click()
   
   def enter_text(self, locator, text):
        element = self.get_element(locator)
        element.clear()
        element.send_keys(text)

   def get_text(self, locator):
        element = self.get_element(locator)
        return element.text



       