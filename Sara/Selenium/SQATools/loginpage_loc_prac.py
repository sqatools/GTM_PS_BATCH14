import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver= webdriver.Chrome()
driver.maximize_window()

driver.get("https://sqatools.in/login-page/")
driver.implicitly_wait(10)

#ID Locator Prac

driver.find_element(By.ID,"email").send_keys("user1@gmail.com")
driver.find_element(By.ID,"pass").send_keys("User@1234")
driver.find_element(By.ID,"loginbutton").click()

