from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome
driver.maximize_window
driver.implicitly_wait(10)
driver.get("https://sqatools.in/automation-practice-page/")

#Is Enabled and disabled
