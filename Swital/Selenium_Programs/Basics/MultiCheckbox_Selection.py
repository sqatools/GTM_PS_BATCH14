from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://selectorshub.com/xpath-practice-page/")
driver.implicitly_wait(30)
#time.sleep(10)

checkboxes = driver.find_elements(By.XPATH, "//a[contains(text(),'Employee')]//ancestor::thead/following-sibling::tbody//input[@type='checkbox']")
#checkboxes = driver.find_elements(By.XPATH, "//table[@id='resultTable']//input")
time.sleep(2)
for checkbox in checkboxes:
    checkbox.click()
    time.sleep(2)