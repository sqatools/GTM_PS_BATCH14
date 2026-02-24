from ...Base.SeleniumBase import SeleniumBase
from .dummy_page_locator import DummyPageLocator

class DummyPage(SeleniumBase):

    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver

    def launch_website(self,url):
        self.driver.get(url)

    def enter_first_name(self,value):
        self.enter_text(DummyPageLocator.FIRST_NAME,value)
    
    def enter_last_name(self,value):
        self.enter_text(DummyPageLocator.LAST_NAME,value)
