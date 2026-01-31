from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://sqatools.in/automation-practice-page/")
time.sleep(3)

source = driver.find_element(By.ID, "drag1")
target = driver.find_element(By.CLASS_NAME, "drop")

# Scroll to source element
driver.execute_script("arguments[0].scrollIntoView();", source)
time.sleep(1)

# JavaScript Drag & Drop
script = """
var source = arguments[0];
var target = arguments[1];

var dataTransfer = new DataTransfer();

source.dispatchEvent(new DragEvent('dragstart', {dataTransfer:dataTransfer}));
target.dispatchEvent(new DragEvent('drop', {dataTransfer:dataTransfer}));
source.dispatchEvent(new DragEvent('dragend', {dataTransfer:dataTransfer}));"""


driver.execute_script(script, source, target)

time.sleep(3)
driver.quit()
