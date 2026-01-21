# Locators/Selectors in Selenium

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("https://sqatools.in/automation-practice-page/")

# ID Locator
driver.find_element(By.ID, "username").send_keys("Swital")
driver.find_element(By.ID, "password").send_keys("Test@1234")

# NAME Locator
driver.find_element(By.NAME, "address").send_keys("12.4, Abc street, india")
#Tag_NAME Locator
heading = driver.find_element(By.TAG_NAME, "h2")
print("Heading Text is :", heading.text)

# link_TEXT Locator
link_google = driver.find_element(By.LINK_TEXT, "Open Google")
link_google.click()

# partial_LINK_TEXT Locator
Plink_google = driver.find_element(By.PARTIAL_LINK_TEXT, "Open")
Plink_google.click()
