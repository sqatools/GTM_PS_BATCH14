"""
install selenium using pip:
pip install selenium
"""
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# initialize the Chrome driver
#driver = webdriver.Chrome()
# driver = webdriver.Firefox()
driver = webdriver.Edge()
# set implicit wait time
driver.implicitly_wait(10)
# maximize the browser window
driver.maximize_window()
# navigate to the URL
driver.get("https://sqatools.in/login-page/")
#driver.find_element(By.ID, "email").send_keys("user1@gmail.com")
email_field = driver.find_element(By.ID, "email")
email_field.send_keys("user1@gmail.com")

driver.find_element(By.ID, "pass").send_keys("User@1234")
driver.find_element(By.ID, "loginbutton").click()

time.sleep(5)  # wait for 5 seconds to see the result
# close the browser
driver.close()

# practice links
# https://sqatools.in/dummy-booking-website/
# https://sqatools.in/automation-practice-page/
# https://opensource-demo.orangehrmlive.com/web/index.php/auth/login

