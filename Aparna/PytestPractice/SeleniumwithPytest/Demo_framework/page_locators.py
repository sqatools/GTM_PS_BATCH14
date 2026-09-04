from selenium.webdriver.common.by import By 


class LoginPageLocators:
    username=(By.ID,"email")
    password=(By.ID,"pass")
    login_button=(By.ID,"loginbutton")