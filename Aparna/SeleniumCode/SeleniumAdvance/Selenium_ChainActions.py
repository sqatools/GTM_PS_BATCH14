#drag and drop,click and hold -chain actions,import chainaction class fro drag and drop
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.action_chains import ActionChains


driver=webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
action = ActionChains(driver)

driver.get("https://www.globalsqa.com/demo-site/draganddrop/")

def perform_dragAnddrop():
    #inside iframe performing dragand drop action
    iframe_click=driver.find_element(By.XPATH,"//iframe[contains(@src, 'photo-manager')]")
    driver.switch_to.frame(iframe_click)
    
    image_ele=driver.find_element(By.XPATH,"//h5[text()='High Tatras']/parent::li")
    move_to_trash=driver.find_element(By.ID,"trash")
    time.sleep(5)
    
   
    action.drag_and_drop(image_ele, move_to_trash).perform()
    print("Sucessfully drag and drop isdone")
    

#perform_dragAnddrop()
def dragAnddrop2():
    driver.get("https://sqatools.in/automation-practice-page/")
    image1=driver.find_element(By. ID, "drag1")
    drop=driver.find_element(By.XPATH,"//div[@class='drop']")
    time.sleep(10)
    
    action.drag_and_drop(image1,drop).perform()
    time.sleep(5)
    print("Sucessfully drag the option")
#dragAnddrop2()

#mouse hover to element for that we nedd to perform actions 
#I want to locate and scroll the bottom

def perform_mouseHover_to_element():
    driver.get("https://www.globalsqa.com/demo-site/draganddrop/")
    time.sleep(5)
    hover_ele=driver.find_element(By.XPATH,"//div[@id='menu']//a[contains(text(),'Tester')]")
    action.move_to_element(hover_ele).perform()
    
    #click on demo website
    demo_site_testing=driver.find_element(By.XPATH,"//div[@id='menu']//span[contains(text(),'Demo Testing Site')]")
    action.move_to_element(demo_site_testing).perform()
    
    #clcik on alert box in demo website 
    alert_box=driver.find_element(By.XPATH,"//div[@id='menu']//span[contains(text(),'Alert')]")
    action.move_to_element(alert_box).click().perform()
    print(alert_box.text)
    
    time.sleep(10)
#perform_mouseHover_to_element()


#scroll to the particular element
def scrolling_page():
     driver.get("https://sqatools.in/automation-practice-page/")
     time.sleep(5)
     scroll_ele=driver.find_element(By.XPATH,"//input[@placeholder='Press any key']")
     action.scroll_to_element(scroll_ele).click(scroll_ele).send_keys("python").perform()
     time.sleep(5)
     print("Scrol to the keyborad actions")
     time.sleep(5)
     
#scrolling_page()
#context click means right click
def context_click():
    driver.get("https://sqatools.in/automation-practice-page/")
    time.sleep(5)
    right_clickbutton=driver.find_element(By.ID,"drag1")
    action.context_click(right_clickbutton).perform()
    time.sleep(5)
    print("Context click performed sucessfully")
    time.sleep(5)
    
context_click()    


    

