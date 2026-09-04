from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://sqatools.in/automation-practice-page/")
all_links = driver.find_elements(By.TAG_NAME, "a")
for links in all_links:
    href = links.get_attribute("href")
    print("All the links present in the webpage are: ", href)