import time 
from selenium import webdriver
from selenium.webdriver.common.by import By 

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://sqatools.in/dummy-booking-website/")
driver.implicitly_wait(10)

"""
checkboxes = driver.find_elements(By.XPATH, "//table[@id='cities']//input[@type='checkbox']")
for checkbox in checkboxes:
    checkbox.click()
    time.sleep(2)
"""

city_list = ["Indore", "Mumbai", "Pune", "Kolkata"]
for city in city_list:
    checkbox = driver.find_element(By.XPATH, f"//td[text()='{city}']/parent::tr//input[@type='checkbox']")
    checkbox.click()
    time.sleep(2)