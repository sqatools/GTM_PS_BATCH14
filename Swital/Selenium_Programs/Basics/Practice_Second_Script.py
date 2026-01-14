from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get("https://sqatools.in/dummy-booking-website/")
driver.maximize_window()
driver.implicitly_wait(10)
driver.find_element(By.NAME, "firstname").send_keys("Swital")
driver.find_element(By.NAME, "firstname").send_keys("Macwan")
driver.implicitly_wait(10)

first_checkbox = driver.find_element(By.XPATH, "(//table[@id='cities']//input[@type='checkbox'])[1]")

first_checkbox.click()