#handle the tabs and windows in selenium
import selenium
from selenium import webdriver  
import time 
from selenium.webdriver.common.by import By     

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("https://sqatools.in/automation-practice-page/")
#print("Main Window Title: ", driver.title)
#click on open new tab button
google_tab_button = driver.find_element(By.LINK_TEXT, "Open Google").click()
time.sleep  (5)
#handle the windows
all_windows = driver.window_handles
print("All window handles: ", all_windows)
#switch to google tab
driver.switch_to.window(all_windows[1])
time.sleep(10)
print("Google Tab Title: ", driver.title)
search_box = driver.find_element(By.NAME, "q").send_keys("https://automationbysqatools.blogspot.com/2020/07/step-by-step-guide-to-install-pycharm.html")
time.sleep(10)
driver.find_element(By.NAME, "btnK").click()
time.sleep(15)
#switch back to main window
driver.switch_to.window(all_windows[0])
time.sleep(15)
print("Main Window Title after switching back: ", driver.title)

driver.close()