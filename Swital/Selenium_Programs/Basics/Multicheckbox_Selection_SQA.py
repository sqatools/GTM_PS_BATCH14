from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://sqatools.in/dummy-booking-website/")
driver.implicitly_wait(10)

#//table[@id='cities']//input[@type='checkbox']
"""checkboxes = driver.find_elements(By.XPATH, "//th[text()='City Name']/parent::tr/following-sibling::tr//input")
time.sleep(2)
for checkbox in checkboxes:
    checkbox.click()
    time.sleep(2)"""

# Select specific checkboxes based on city names
city_list = ["Indore", "Mumbai", "Pune", "Kolkata"]
for city in city_list:
    specific_checkboxes = driver.find_element(By.XPATH, f"//td[text()='{city}']/parent::tr//input[@type='checkbox']")
    specific_checkboxes.click()
    time.sleep(2)