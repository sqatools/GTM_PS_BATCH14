from seleniumbase import SeleniumBase
from locators import Locators



class Page(SeleniumBase):
    def __init__(self,driver):
        super(). __init__(driver)
        self.driver=driver
        
    def get_url(self,url):
        self.driver.get(url)
        
    def get_title(self):
        return self.driver.title()
    
    def  enter_username(self,value):
        self.enter_text(Locators.text_field_username,value)
        
    def enter_password(self,value):
        self.enter_text(Locators.password_field,value)
        
    def enter_address(self,value):
        self.enter_text(Locators.enter_address,value)
        
    def click_radio_button(self):
        self.select_radio_button(Locators.click_radio_button)
        
    def click_checkbox(self):
        self.select_checkbox(Locators.click_checkbox)
        
    def click_dropdown(self):
        self.select_dropdown(Locators.select_dropdown)

    
    
        