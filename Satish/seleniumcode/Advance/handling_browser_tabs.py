"""
When we open any new website then it open in new tab so we want to go to new tab or website and want to perform some action.
For example first we open any website and in that website we click on link element which is say open google website so we go to google website tab and serach some thing in google website

"""

import time
from selenium import webdriver
from selenium.webdriver.common.by import By


driver=webdriver.Edge() # Make driver of Edge webbrowser to interact with website
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("https://sqatools.in/automation-practice-page/") # open this website
# Now in this website search Link element (Open Google) by Right click on link and select inspect to view HTML code
open_google_link_element=driver.find_element(By.ID,"googleLink")
# click on link
open_google_link_element.click() # So new google tab will open
# Now to handle this tab we do following

def browser_handle_tab():
    #get all tabs
    tab_list=driver.window_handles
    print(tab_list)
    # Switch to the new tab (assuming it's the second window handle or tab)
    driver.switch_to.window(tab_list[1])
    # Perform actions in the new tab
    print("New tab title:", driver.title) #Google
    # If we want to search in google then we first search google seach window
    search_window_element=driver.find_element(By.NAME,'q')
    search_window_element.send_keys('Iskraemeco')
    time.sleep(5)
    # Now searchGoogle search button to click on it to seach Iskraemeco word
    google_search_button=driver.find_element(By.NAME,'btnK')
    google_search_button.click()
    time.sleep(5)
    #close google tab
    driver.close()
    #switch back to original tab
    driver.switch_to.window(tab_list[0])
    time.sleep(5)
    print("original tab title",driver.title) # original tab title Automation Practice Page - SQA Tools

browser_handle_tab()