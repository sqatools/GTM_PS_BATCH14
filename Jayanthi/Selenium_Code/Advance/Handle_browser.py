from selenium import webdriver
from selenium.webdriver.common.by import By
import time
# Initialize the Chrome driver
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
# Navigate to a sample page
driver.get("https://sqatools.in/automation-practice-page/")

def handle_browser():

    #click on google link 
    driver.find_element(By.ID, "googleLink").click()
    time.sleep(5)
    win_list=driver.window_handles
    print(win_list)
    #switch to new tab
    driver.switch_to.window(win_list[1])
    print("New tab title:",driver.title)
    driver.find_element(By.NAME,"q").send_keys("Holiday")
    time.sleep(5)
    driver.find_element(By.NAME,"btnK").click()
    time.sleep(5)
    driver.close()
    #move to parent tab
    driver.switch_to.window(win_list[0])
    print("Parent tab title:",driver.title)
    time.sleep(5)
    random_file=f"file_{time.strftime('%Y%m%d_%H%M%S')}.txt"
    file_path=f"C:\Automationproject\GTM_PS_BATCH14\Jayanthi\Selenium_Code\Advance\{random_file}"
    #create a sample file to upload 
    with open(file_path,'w') as f:
        f.write("This is a sample file for upload testing.")
    #driver.find_element(By.ID,"fileUpload").send_keys(r"C:\Users\Ajay - PC\Downloads\L2 - Beginner.pdf")
    time.sleep(5)
handle_browser()
# Close the browser
driver.close()

