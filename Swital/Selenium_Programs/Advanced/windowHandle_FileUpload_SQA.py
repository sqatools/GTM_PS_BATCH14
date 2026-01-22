from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://sqatools.in/automation-practice-page/")

weblink = driver.find_element(By.ID, "googleLink")
weblink.click()

# Handle window tabs
all_window = driver.window_handles
print("All windows: ", all_window)
# switch to the newly opened window (index 1)
driver.switch_to.window(all_window[1])

print("Title of the page:", driver.title)

# switch back to original window
driver.switch_to.window(all_window[0])
time.sleep(4)

# File Upload: locate the file input and send the absolute path
file_input = driver.find_element(By.XPATH, "//input[@type='file']")
file_path = r"E:\Growtechmind\java.txt"
file_input.send_keys(file_path)
time.sleep(2)