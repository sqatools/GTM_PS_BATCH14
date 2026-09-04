from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Initialize the Chrome driver
driver = webdriver.Chrome()
# maximize the browser window
driver.maximize_window()
driver.implicitly_wait(10)
# navigate to the URL
driver.get("https://sqatools.in/automation-practice-page/")

#handling tabs
def handle_tabs():
    driver.find_element(By.ID, "googleLink").click()

    windows_list = driver.window_handles
    driver.switch_to.window(windows_list[1])

    driver.find_element(By.NAME, "q").send_keys("Selenium Python")
    time.sleep(5)

    driver.find_element(By.NAME, "btnK").click()
    time.sleep(5)

    driver.close()  # Close the new tab

    # switch back to the original tab
    driver.switch_to.window(windows_list[0])

handle_tabs()