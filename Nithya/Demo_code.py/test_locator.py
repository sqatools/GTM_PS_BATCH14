from selenium.webdriver.common.by import By

class Loginscreen:
    username= By.id="username"
    password= By.id="password"
    text= By.id="address"
    text.clear()
    text.send_keys("Demo on Fixture")   
    loginbutton= By.id="loginbutton"
