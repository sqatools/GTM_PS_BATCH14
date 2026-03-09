from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("https://selectorshub.com/xpath-practice-page/")
download_link = driver.find_element(By.LINK_TEXT, "//a[text() = 'Download Link']")
download_link.click()