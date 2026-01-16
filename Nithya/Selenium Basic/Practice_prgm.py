"""import time
from webbrowser import Chrome
from selenium import webdriver
from selenium.webdriver.common.by import By     
# Initialize the Chrome driver
driver = webdriver.Chrome()
# Set implicit wait time    
driver.implicitly_wait(10)
# Maximize the browser window
driver.maximize_window()
# Navigate to the URL
driver.get("https://sqatools.in/login-page/")
#driver.find_element(By.ID, "Login Page").click()
driver.find_element(By.ID, "email").send_keys("nithya.test@gmail.com")
driver.find_element(By.ID, "pass").send_keys("Nithya@1234")
driver.find_element(By.ID, "loginbutton").click()    
#driver.find_element(By.ID, "courses").click()
#driver.find_element(By.ID, "Courses").highlight()
driver.find_element(By.ID, "user_login").send_keys("nithya.test@gmail.com")
driver.find_element(By.ID, "user_pass").send_keys("Nithya@1234")
driver.find_element(By.ID, "wp-submit").click()



'''
Practice program 2:
https://sqatools.in/automation-practice-page/
'''

import time
from selenium import webdriver
from selenium.webdriver.common.by import By 
# Initialize the Chrome driver
driver=webdriver.Chrome()
# Set implicit wait time
driver.implicitly_wait(5)
# Maximize the browser window
driver.maximize_window()
# Navigate to the URL
driver.get("https://sqatools.in/automation-practice-page/")
driver.find_element(By.ID, "username").send_keys("Nithya")
driver.find_element(By.ID, "password").send_keys("Test")   
Address= driver.find_element(By.NAME, "address")
Address.clear()
Address.send_keys("Chennai")
time.sleep(2)
Radio_option= driver.find_element(By.NAME , "gender")
Radio_option.click()
Checkbox= driver.find_element(By.ID, "selenium")
Checkbox.click()
Choosecountry= driver.find_element(By.NAME, "country")
Choosecountry.click()
Choosecountry.send_keys("UK")
Mult_Select= driver.find_element(By.ID, "skills")
Mult_Select.click()
Mult_Select.send_keys("Selenium") 
Mult_Select.send_keys("API Testing")

"""
print("#" * 20)
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
# Initialize the Chrome driver
driver = webdriver.Chrome() 
# Set implicit wait time
driver.implicitly_wait(10)
# Maximize the browser window
driver.maximize_window()        
# Navigate to the URL
driver.get("http://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.find_element(By.NAME, "username").send_keys("Admin")
driver.find_element(By.NAME, "password").send_keys("admin123")
driver.find_element(By.XPATH, "//button[@type='submit']").click()
time.sleep(1)
driver.find_element(By.XPATH, "(//span[contains(@class,'oxd-text oxd-text--span oxd-main-menu-item--name')])[6]").click()
time.sleep(5)
element = driver.find_element(By.XPATH, "//label[contains(text(),'Employee Id')]//parent::div/parent::div//input")
#element.click()
time.sleep(2)
element.clear()
element.send_keys("1234")
time.sleep(5)   