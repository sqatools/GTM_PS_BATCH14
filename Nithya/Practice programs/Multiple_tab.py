import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://sqatools.in/automation-practice-page/")
def handle_multiple_tabs():
    driver.find_element(By.XPATH, "//section//a[contains(text(), 'Open Google')]").click()
    window_handles = driver.window_handles
    print(window_handles)
    driver.switch_to.window(window_handles[1])
    print("New tab title:", driver.title)
    driver.find_element(By.XPATH, "//style//div[contains(text(), title='Search')]").send_keys("Selenium Python")
driver.implicitly_wait(5)