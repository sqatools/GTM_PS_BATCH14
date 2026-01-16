
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.implicitly_wait(10)

username_field = driver.find_element(By.XPATH, "//input[@placeholder='Username']")
username_field.send_keys("Admin")
password_field = driver.find_element(By.XPATH, "//input[@placeholder='Password']")
password_field.send_keys("admin123")
login_button = driver.find_element(By.XPATH, "//button[normalize-space()='Login']")
login_button.click()
time.sleep(5)

driver.quit()