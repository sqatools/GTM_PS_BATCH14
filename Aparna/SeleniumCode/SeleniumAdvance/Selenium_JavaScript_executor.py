#javascipt is an to get element ,scroll to the elementdrag and drop ,hidden element,set the element
#In order to check the javascript executo in website inspect--goto console-- type document.tittle 
#If we dont have solution in when action chain is not working in selenium to find element instead of that use javascript
#https://www.w3schools.com/jsref/met_document_queryselector.asp


from gc import disable
from sqlite3 import Time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
driver=webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://sqatools.in/automation-practice-page/")

def javascript_executor():
    #get title of the page
    tittle=driver.execute_script("return document.title;")
    print("Title of the pageis:",tittle)
    
    #get current url of the page
    current_url=driver.execute_script("return document.URL;")
    time.sleep(5)
    print("Get current url of the page is:", current_url)
    
    #draga and drop perform
    drag_elem1 = driver.execute_script("return document.getElementById('drag1');")
    drop_elem1 = driver.execute_script("return document.getElementsByClassName('drop')[0];")
    
    action = ActionChains(driver)
    action.drag_and_drop(drag_elem1, drop_elem1).perform()
    # Alternatively, you can use:
    action.move_to_element(drag_elem1).click_and_hold().move_to_element(drop_elem1).release().perform()
    
    script = """
    var source = arguments[0];
    var target = arguments[1];
    var dataTransfer = new DataTransfer();
    source.dispatchEvent(new DragEvent('dragstart', {dataTransfer:dataTransfer}));
    target.dispatchEvent(new DragEvent('drop', {dataTransfer:dataTransfer}));
    source.dispatchEvent(new DragEvent('dragend', {dataTransfer:dataTransfer}));"""
    driver.execute_script(script, drag_elem1, drop_elem1)
    time.sleep(5)
    
    
    #To open new tab  from the current url '-blank'is a  special window target
    #To tells the browser open the url in a new window
    
    driver.execute_script("window.open('https://sqatools.in/login-page/', '-blank');")
    time.sleep(5)
    
    window_list=driver.window_handles
    driver.switch_to.window(window_list[1])
    time.sleep(5)
    
    username=driver.execute_script("return document.getElementById('email');")
    password=driver.execute_script("return document.getElementById('pass');")
    loginbutton=driver.execute_script("return document.getElementById('loginbutton');")
    username.send_keys("user1@gmail.com")
    password.send_keys("password123")
    loginbutton.click()
    time.sleep(5)

#javascript_executor()
#arguments[0] = first argument after the script string (element)
#arguments[1] = second argument
#true → align the element to the top of the viewport.
#false → align the element to the bottom of the viewport.
def scroll_to_the_element():
    element_scroll=driver.find_element(By.ID,"submit")
    
    driver.execute_script("arguments[0].scrollIntoView(true);",element_scroll)
    print("Scroll to the  element post comment")
    time.sleep(5)
    
"""For drag and drop field
    element =  driver.find_element(By.ID, "drag1")
    driver.execute_script("arguments[0].scrollIntoView(true);", element)
    print("Scrolled to element with ID 'drag1'.")
    time.sleep(5)
    element2 = driver.execute_script("return document.getElementsByClassName('drop')[0].innerText;")
    print("Text of the first drop element is:", element2)
"""
    
#scroll_to_the_element()
    
 #Only in javascript we can disable
def disable_element():
    disable_input=driver.find_element(By.ID,"disabledInput")
    driver.execute_script("arguments[0].removeAttribute('disabled');",disable_input)
    disable_input.send_keys("Text entered in the field")
    time.sleep(5)
    print("Text entered in disable field successfully")
    
#disable_element()

def hidden_element():
    hidden_ele=driver.find_element(By.ID,"hiddenField")
    driver.execute_script("arguments[0].style.display='block';",hidden_ele)
    hidden_ele.send_keys("Text entered in field")
    time.sleep(6)
    
    print("Text entered in hidden field successfully")
hidden_element()


