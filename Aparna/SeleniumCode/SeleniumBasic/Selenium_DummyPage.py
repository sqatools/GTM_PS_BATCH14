
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.support import expected_conditions as EC
driver=webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("https://sqatools.in/dummy-booking-website/")
driver.find_element(By.CSS_SELECTOR, "input[value='radio_123']").click()
#driver.find_element(By.CSS_SELECTOR, "input[value='radio_123']").click()

# Find and click radio button
#radio_btn = driver.find_element(By.CSS_SELECTOR, "input[value='radio_123']")
#radio_btn.click()

# Wait until value appears in textbox
#WebDriverWait(driver, 10).until(
  #  lambda d: d.find_element(By.ID, "firstname").get_attribute("value") == "Aparna"
#)
driver.find_element(By.ID, "firstname").send_keys("Aparna")
driver.find_element(By.NAME, "firstname").send_keys("S")
driver.implicitly_wait(100)
driver.find_element(By.ID, "female").click()
#driver.get.title()
#print(driver.title)
expected_title = "Example Domain"

actual_title = driver.title

if actual_title == expected_title:
    print("Title matched")
else:
    print("Title not matched")
    
