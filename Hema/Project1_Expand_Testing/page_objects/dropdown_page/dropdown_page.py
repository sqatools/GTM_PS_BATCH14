from base.selenium_base import SeleniumBase
from page_objects.dropdown_page.dropdown_page_locator import DropdownPageLocator

class DropdownPage(SeleniumBase):
    def __init__(self, driver):
        super().__init__(driver)

    def launch_website(self, url):
        self.driver.get(url)

    def select_dropdown_option(self, option_locator):
        self.select_dropdown(DropdownPageLocator.dropdown_locator, option_locator)
       
    def select_elements_per_page(self, elements_per_page_locator):
        self.select_dropdown(DropdownPageLocator.elements_per_page_locator, elements_per_page_locator)
       
    def select_country(self, country_locator):
        self.select_dropdown(DropdownPageLocator.country_locator, country_locator)
      