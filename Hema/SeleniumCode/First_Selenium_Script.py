"""
install selenium using pip:
pip install selenium
"""
# Initialize the crome driver
import selenium
from selenium import webdriver  
import time 
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()

driver.get("https://sqatools.in/login-page/")

email_field = driver.find_element(By.ID, "email").send_keys("hema@gmail.com")

password_field = driver.find_element(By.ID, "pass").send_keys("Hema")
driver.find_element(By.ID, "loginbutton").click()
time.sleep(5)
driver.close()
# practice links
# https://sqatools.in/dummy-booking-website/
# https://sqatools.in/automation-practice-page/
