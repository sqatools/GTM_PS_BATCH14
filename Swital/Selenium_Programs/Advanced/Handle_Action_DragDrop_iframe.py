from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)

action = ActionChains(driver)
driver.get("https://www.globalsqa.com/demo-site/draganddrop/")
dragdrop_element = driver.find_element(By.XPATH, "//iframe[contains(@src, 'photo-manager')]")
driver.switch_to.frame(dragdrop_element)

# drag and drop logic
source_element = driver.find_element(By.XPATH, "//h5[text()='High Tatras 4']/parent::li")
target_element = driver.find_element(By.ID, "trash")
action.drag_and_drop(source_element,target_element).perform()
time.sleep(2)
driver.switch_to.default_content()