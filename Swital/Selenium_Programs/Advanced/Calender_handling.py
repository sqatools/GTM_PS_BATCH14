from concurrent.futures import wait

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from datetime import datetime
from selenium.webdriver import ActionChains
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://sqatools.in/automation-practice-page/")

def test_calender_handling1():
    # either enter the date in the text box or select the date from the calendar
    # method 1: enter the date in the text box
    wait = WebDriverWait(driver, 10)
    wait.until(EC.visibility_of_element_located((By.ID, "datePicker"))).send_keys("10/10/2023")
    wait.until(EC.visibility_of_element_located((By.ID, "timePicker"))).send_keys("10:10")
    time.sleep(2)
    
    date_time = wait.until(
    EC.presence_of_element_located((By.ID, "dateTimePicker"))
    )

    # Remove readonly (if present)
    driver.execute_script(
        "arguments[0].removeAttribute('readonly')",
        date_time
    )

    # Clear and send value
    date_time.clear()
    date_time.send_keys("04-12-2002T10:10")
    time.sleep(2)

    #screenshot1 = driver.save_screenshot("Swital/Selenium_Programs/Advanced/calender1.png")

test_calender_handling1()

