
from selenium.webdriver.common.by import By

class Locators:
    
    #SQA Tools page locators
    text_field_username=(By.ID, "username")
    password_field=(By.ID, "password")
    enter_address=(By.ID, "address")
    click_radio_button=(By.ID, "male")
    click_checkbox=(By.ID, "java")
    select_dropdown=(By.XPATH, "//select[@id='country']/descendant::option[@value='india']")