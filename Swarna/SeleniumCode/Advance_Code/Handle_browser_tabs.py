from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By 
import time
import os

# Initialize the Chrome driver
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
# Navigate to a sample page
driver.get("https://sqatools.in/automation-practice-page/")

def handle_browser_tabs():
    # Click on google link which opens in a new tab
    driver.find_element(By.ID, "googleLink").click()
    time.sleep(5)

    # Get all window handles
    windows_list =  driver.window_handles
    print(windows_list)

    # Switch to the new tab(assuming it's the second window handle)
    driver.switch_to.window(windows_list[1])

    # Perform actions in the new tab
    print("New tab title:", driver.title)

    driver.find_element(By.NAME, "q").send_keys("Selenium Python")
    time.sleep(5)
    driver.find_element(By.NAME, "btnK").click()
    time.sleep(5)

    driver.close()  # Close the new tab

    # switch back to the original tab
    driver.switch_to.window(windows_list[0])
    time.sleep(5)

    file_path = os.path.join(os.getcwd(), 'upload_' + datetime.now().strftime('%Y%m%d_%H%M%S') + '.txt')
    with open(file_path, 'w') as f:
        f.write("This is a sample file for screenshot naming.")

    driver.find_element(By.ID, "fileUpload").send_keys(file_path)

    time.sleep(10)
    print("Original tab title:", driver.title)


handle_browser_tabs()