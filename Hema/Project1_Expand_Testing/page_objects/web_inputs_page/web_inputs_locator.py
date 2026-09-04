from selenium.webdriver.common.by import By

class WebInputsLocator:
    link_web_inputs = (By.LINK_TEXT, "Web Inputs")
    input_number_locator = (By.ID, "input-number")
    input_text_locator = (By.ID, "input-text")
    input_password_locator = (By.ID, "input-password")
    input_date_locator = (By.ID, "input-date")    
