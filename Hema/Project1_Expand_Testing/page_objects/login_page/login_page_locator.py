from selenium.webdriver.common.by import By

class LoginPageLocator:
    link_login_locator = (By.XPATH, "//a[text()='Login']")
    input_username_locator = (By.NAME, "username")  
    input_password_locator = (By.NAME, "password")
    click_login_locator = (By.ID, "submit-login")