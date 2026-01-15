from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("https://www.saucedemo.com/")
login_un= driver.find_element(By.XPATH, "//input[@type='text']")
login_un.send_keys("standard_user")
password = driver.find_element(By.XPATH, "//input[@type='password']")
password.send_keys("secret_sauce")
login_btn = driver.find_element(By.ID, "login-button")
login_btn.click()