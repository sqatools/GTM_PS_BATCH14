from selenium.webdriver.common.by import By

class RegisterPageLocator:
    input_username_locator = (By.NAME, "username")
    input_password_locator = (By.NAME, "password")
    confirm_password_locator = (By.NAME, "confirmPassword")
    click_register_locator = (By.XPATH, "//button[text()='Register']")