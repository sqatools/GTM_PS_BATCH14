import time
from selenium import webdriver
from selenium.webdriver.common.by import By
# initialize the Chrome driver
driver = webdriver.Chrome()
# set implicit wait time
driver.implicitly_wait(10) 
# maximize the browser window
driver.maximize_window()
# navigate to the URL
driver.get("https://sqatools.in/login-page/")
driver.find_element(By.ID, "email").send_keys("user1@gmail.com")
driver.find_element(By.ID, "pass").send_keys("User@1234")
driver.find_element(By.ID, "loginbutton").click()
time.sleep(5)  # wait for 5 seconds to see the result
# close the browser
driver.close()
