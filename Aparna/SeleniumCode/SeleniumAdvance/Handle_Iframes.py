import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

from selenium .webdriver.support.select import Select

driver =webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
action = ActionChains(driver)
driver.get("https://www.globalsqa.com/demo-site/frames-and-windows/#iFrame")


def handle_iframe():
    iframe_element=driver.find_element(By.NAME,"globalSqa")
    driver.switch_to.frame(iframe_element)#switch to iframe
    
    #find heading in iframe
    heading=driver.find_element(By.XPATH, "//div[@class='page_heading']/h1")
    print("Heading iframe name:",heading.text)
    
    #perform click in iframe
    # Wait for dropdown to be clickable
    wait = WebDriverWait(driver, 5, poll_frequency=1)
    multi_dropdown = wait.until(EC.element_to_be_clickable((By.ID, "mobile_menu_toggler")))
    multi_dropdown.click()
    #mouse hover element
   # mouse_hover_element=driver.find_element(By.XPATH,"//span[@id='current_filter']")

    #action.move_to_element(mouse_hover_element).perform()
    
   # click_element=driver.find_element(By.XPATH,"//ul[@id='filter_list']//div[contains(text(),'Automation')]")
    #action.move_to_element(click_element).click.perform()
   # time.sleep(10)
    
    #switch to main content
    driver.switch_to.default_content()
    time.sleep(5)
    
    #find heading in main window
    heading=driver.find_element(By.XPATH, "//div[@class='page_heading']/h1")
    print("Heading iframe name:",heading.text)
    
handle_iframe()


    
    
    
    
    
