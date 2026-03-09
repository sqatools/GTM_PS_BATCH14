# pip install selenium
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://sqatools.in/login-page/")
driver.maximize_window()
driver.implicitly_wait(10)
driver.find_element(By.ID, "email").send_keys("swital@gmail.com")
driver.find_element(By.ID, "pass").send_keys("Swital@123")    
driver.find_element(By.ID, "loginbutton").click()
driver.close()


