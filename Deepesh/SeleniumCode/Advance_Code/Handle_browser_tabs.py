from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By 
import time

# Initialize the Chrome driver
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
# Navigate to a sample page
driver.get("https://sqatools.in/automation-practice-page/")

def handle_browser_tabs():
    # click on google link which opens in a new tab
    driver.find_element(By.ID, "googleLink").click()

    # Get all window handles
    windows_list = driver.window_handles
    print(windows_list)

    # Switch to the new tab (assuming it's the second window handle)
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
    print("Original tab title:", driver.title)

    # Upload a file in the original tab
    random_file_name = f"file_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    file_path = f"E:\\Filesdata\\Batch14\\{random_file_name}"
    # create a sample file to upload
    with open(file_path, 'w') as f:
        f.write("This is a sample file for upload testing.")   


    #driver.find_element(By.ID, "fileUpload").send_keys(r"E:\Filesdata\count_name.txt")
    driver.find_element(By.ID, "fileUpload").send_keys(file_path)
    time.sleep(5)

handle_browser_tabs()