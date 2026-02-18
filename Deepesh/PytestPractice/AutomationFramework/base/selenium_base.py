from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

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

    def is_element_selected(self, locator):
        """
        Docstring for is_element_selected
        :param self: Description
        :param locator: locator value will provide in tuple format (By.ID, "id_value")
        :return: True if element is selected, False otherwise
        """
        element = self.get_element(locator)
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