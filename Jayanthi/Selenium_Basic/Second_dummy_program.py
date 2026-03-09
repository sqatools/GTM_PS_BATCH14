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
driver.get("https://sqatools.in/dummy-booking-website/")
driver.find_element(By.ID, "firstname").send_keys("testuser")
driver.find_element(By.ID, "birthday").send_keys("01/01/1990")
driver.find_element(By.ID, "male").click()

time.sleep(5)  # wait for 5 seconds to see the result
# close the browser
driver.close()