from selenium.webdriver.common.by import By

class LoginPageLocators:
    USERNAME = (By.ID, "email")
    PASSWORD = (By.ID, "pass")
    LOGIN_BUTTON = (By.ID, "loginbutton")
    MOBILE_NUMBER = (By.ID, "mobile_number")
    COUNTRY_DROPDOWN = (By.ID, "country")