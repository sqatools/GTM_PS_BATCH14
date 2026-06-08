from selenium.webdriver.common.by import By
from selenium import webdriver
import time

#initialize the Chrome driver
driver=webdriver.Chrome()   
#maximize the browser window
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://sqatools.in/dummy-booking-website/#google_vignette")
def handle_multiple_checkboxes():
    time.sleep(10)
    checkboxes=driver.find_elements(By.XPATH, "//input[@type='checkbox']")
    for checkbox in checkboxes:
        if not checkbox.is_selected():
            checkbox.click()
            print("Selected checkbox with value:", checkbox.get_attribute("value"))
            time.sleep(10)
        else:
            print("Checkbox with value", checkbox.get_attribute("value"), "is already selected.")


#deselect one option--selenium
    checkbox = driver.find_element(By.XPATH, "(//input[@type='checkbox'])[3]")
    if checkbox.is_selected():
        checkbox.click()
handle_multiple_checkboxes()
#deselected all checkboxes if they are already selected
def deselect_all_checkboxes():
    time.sleep(10)
    checkboxes=driver.find_elements(By.XPATH, "//input[@type='checkbox']")
    for checkbox in checkboxes:
        if checkbox.is_selected():
            checkbox.click()
            print("Deselected checkbox with value:", checkbox.get_attribute("value"))
            time.sleep(10)
        else:
            print("Checkbox with value", checkbox.get_attribute("value"), "is already deselected.")



#deselect_all_checkboxes()

"""
#checkboxes and radio buttons are also handled using click() method. You can use is_selected() method to check if a checkbox or radio button is selected or not before performing click action.

#most_visited_checkbox=driver.find_element(By.XPATH, "//tr//td[text()='Mumbai']/preceding::input[@type='checkbox']")
most_visited_checkbox=driver.find_element(By.XPATH, "input[type='checkbox']")
#print("Is Mumbai Checkbox Selected?:", most_visited_checkbox.is_selected()) # False  
time.sleep(10)
#most_visited_checkbox.click() # select the checkbox
print("Is Mumbai Checkbox Selected After Click?:", most_visited_checkbox.is_selected()) # True
for i in range(7):
    most_visited_checkbox.click() # toggle the checkbox
    print(f"Is Mumbai Checkbox Selected After Click {i+1}?:", most_visited_checkbox.is_selected()) 
    time.sleep(10)


#print("Selected mumbai city name:", most_visited_checkbox.is_selected())//tr//td//input[@type='checkbox']
"""