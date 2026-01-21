from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://sqatools.in/automation-practice-page/")

# Selenium Methods:
# 1. Title page
title = driver.title
print("The title of the page is:", title)

# 2. Current URL of the page
current_url = driver.current_url
print("The current url is:", current_url)

# 3. Get page source code
page_scode = driver.page_source
print("Source code : ", page_scode)

