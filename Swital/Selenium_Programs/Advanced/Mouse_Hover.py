from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)

action = ActionChains(driver)
driver.get("https://www.globalsqa.com/demo-site/draganddrop/")
time.sleep(4)
tester_hub_menu = driver.find_element(By.XPATH, "//li[@id='menu-item-2822']//a[text() = 'Tester’s Hub']")
action.move_to_element(tester_hub_menu).perform()
time.sleep(4)
submenu_demosite = driver.find_element(By.XPATH, "//div[@id='menu']//span[text()='Demo Testing Site']")
action.move_to_element(submenu_demosite).perform()
time.sleep(4)
dialog_box = driver.find_element(By.XPATH, "//div[@class='subsub_menu']//span[text()='Dialog Boxes']")
action.move_to_element(dialog_box).click().perform()


#$x("//input[@name ='username']").[0].value='abc'
#$x("//input[@value='male']")[0].click()