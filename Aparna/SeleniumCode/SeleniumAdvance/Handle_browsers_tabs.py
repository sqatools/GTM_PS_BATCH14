
from datetime import datetime

from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver=webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://sqatools.in/automation-practice-page/")
#handle browser tabs
def handle_browser_tabs():
    #open a new tab and switch to it GOOGLE LINK in 
    driver.find_element(By.ID, "googleLink").click()
    time.sleep(10)
    
    #get all window handles
    windows_list=driver.window_handles
    print(windows_list)
    
    #switch to the new tab --google link
    driver.switch_to.window(windows_list[1])
    
    #perfrom actions in the new window --google link
    print("New tab tittle:",driver.title)
    driver.find_element(By.NAME, "q").send_keys("Selenium python")
    time.sleep(5)
    #Click google search
    driver.find_element(By.NAME, "btnK").click()
    time.sleep(5)
    driver.close()
    
    #switch back to the automation tab--original tab
    driver.switch_to.window(windows_list[0])
    time.sleep(5)
    print("Original tab tittle:", driver.title)
    
    #upload file in oroginal tab
    #r is a raw format
    random_file_name = f"file_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    #file_path=f"C:\Automation file uploaded\\{random_file_name}"
    file_path=f"C:\Automation file uploaded\\{random_file_name}"
    #creates sample file to upload
    with open (file_path, 'w') as f:
        f.write("This is a sample  file for upload testing")
    driver.find_element(By.ID , "fileUpload").send_keys(file_path)
    #driver.find_element(By.ID, "fileUpload").send_keys(r"C:\Automation file uploaded")    
    
    time.sleep(5)
handle_browser_tabs()
#practice automation
#automationbysqatools.blogspot.com
#https://automationbysqatools.blogspot.com/p/manual-testing.html
#https://automationexercise.com/