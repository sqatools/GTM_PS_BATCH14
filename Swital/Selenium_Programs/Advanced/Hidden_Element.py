from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://sqatools.in/automation-practice-page/")

driver.execute_script(
    "document.getElementById('hiddenField').style.display='block';"
)

element = driver.find_element(By.ID, "hiddenField")
driver.execute_script("arguments[0].scrollIntoView();", element)

# Set value using JS
driver.execute_script(
    "document.getElementById('hiddenField').value='Swital';"
)
time.sleep(4)
print("Value updated using JS")

driver.quit()