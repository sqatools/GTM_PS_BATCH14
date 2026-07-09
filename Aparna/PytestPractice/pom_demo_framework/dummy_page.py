from selenium_base import SeleniumBase
from dummy_page_locators import DummyPageLocators

#page class will have all the methods related to that page
#page class have locators and methods related to that page
#methods means actions we perform on that page
#exmaple of methods are click, enter text, get text, get title, get url etc
#super() is used to call the constructor of parent class
#driver is passed to the constructor of parent class to initialize the driver
# in parent class
class DummyPage(SeleniumBase):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def launch_website(self, url):
        self.driver.get(url)

    def get_title(self):
        return self.driver.title

    def enter_first_name(self, value):
        self.enter_text(DummyPageLocators.FIRST_NAME, value)

    def enter_last_name(self, value):
        self.enter_text(DummyPageLocators.LAST_NAME, value)
