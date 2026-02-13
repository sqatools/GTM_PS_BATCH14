from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SeleniumBase:
    def __init__(self, driver):
        self.driver = driver
        # Initialize explicit WebDriverWait with a timeout of 20 seconds
        self.wait = WebDriverWait(self.driver, 20)


    def get_element(self, locator):
        """
        Docstring for get_element
        :param self: Description
        :param locator: locator value will provide in tuple format (By.ID, "id_value")
        :return: WebElement
        """
        return self.wait.until(EC.presence_of_element_located(locator))
    
    def click_element(self, locator):
        """
        Docstring for click_element
        :param self: Description
        :param locator: locator value will provide in tuple format (By.ID, "id_value")
        :return: None
        """
        element = self.get_element(locator)
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