from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

# initialize the Chrome driver
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://sqatools.in/automation-practice-page/")

def execute_javascript():
    # get title of the page
    title = driver.execute_script("return document.title;")
    print("Title of the page is:", title)

    # get current URL of the page
    current_url = driver.execute_script("return document.URL;")
    print("Current URL of the page is:", current_url)


    drag_elem1 = driver.execute_script("return document.getElementById('drag1');")
    drop_elem1 = driver.execute_script("return document.getElementsByClassName('drop')[0];")
    print("Hovering over Alerts link")
    # perform drag and drop using JavaScript
    action = ActionChains(driver)
    action.drag_and_drop(drag_elem1, drop_elem1).perform()
    # Alternatively, you can use:
    action.move_to_element(drag_elem1).click_and_hold().move_to_element(drop_elem1).release().perform()
    #driver.execute_script("""""")
    script = """
    var source = arguments[0];
    var target = arguments[1];
    var dataTransfer = new DataTransfer();
    source.dispatchEvent(new DragEvent('dragstart', {dataTransfer:dataTransfer}));
    target.dispatchEvent(new DragEvent('drop', {dataTransfer:dataTransfer}));
    source.dispatchEvent(new DragEvent('dragend', {dataTransfer:dataTransfer}));"""
    driver.execute_script(script, drag_elem1, drop_elem1)
    time.sleep(5)

    driver.execute_script("window.open('https://sqatools.in/login-page/','_blank');")
    time.sleep(5)

    windows_list = driver.window_handles
    driver.switch_to.window(windows_list[1])
    time.sleep(5)

    username = driver.execute_script("return document.getElementById('email');")
    paswword = driver.execute_script("return document.getElementById('pass');")
    login_btn = driver.execute_script("return document.getElementById('loginbutton');")
    username.send_keys("user1@gmail.com")
    paswword.send_keys("password123")
    login_btn.click()
    time.sleep(5)

#execute_javascript()

def scroll_to_element():
    time.sleep(5)
    element =  driver.find_element(By.ID, "drag1")
    driver.execute_script("arguments[0].scrollIntoView(true);", element)
    print("Scrolled to element with ID 'drag1'.")
    time.sleep(5)
    element2 = driver.execute_script("return document.getElementsByClassName('drop')[0].innerText;")
    print("Text of the first drop element is:", element2)

#scroll_to_element()