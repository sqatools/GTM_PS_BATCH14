import time

from selenium import webdriver
from selenium.webdriver.common.by import By



#initialize the Chrome driver
driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("https://sqatools.in/login-page/")

#Locator by CSS Selectors
#By Attribute Selector
css_selector_attribute=driver.find_element(By.CSS_SELECTOR, "form[action='/login']>input[id='email'][name='email']")
css_selector_attribute.send_keys("user1@gmail.com")
time.sleep(5)

#By ID
css_selector_id=driver.find_element(By.CSS_SELECTOR, "#pass")
css_selector_id.send_keys("password123")
time.sleep(5)

#By Class Name
#css_selector_class=driver.find_element(By.CSS_SELECTOR, "button.btn-login") 
#css_selector_class=driver.find_element(By.CSS_SELECTOR, "header>h1.entry-title")
#css_selector_class.click()
#time.sleep(5)

#By Contains or substring match
css_selector_contains=driver.find_element(By.CSS_SELECTOR, "button[type*='submit']")
css_selector_contains.click()
time.sleep(5)

"""
CSS Selectors Methods in Selenium:

1. ID Selector: This method is used to select elements based on their ID attribute.
   e.g. #idvalue
   -> #header
   -> #username
   -> #password
   -> #loginButton
   -> #submitButton
   -> #pass

2. Class Selector: This method is used to select elements based on their class attribute.
   e.g. .classname
    -> .entry-title
    -> .wp-block-list
    -> .button
    -> .input-field
    -> button.btn-login
    -> header>h1.entry-title


3. Attribute Selector: This method is used to select elements based on their attribute values.
   e.g. tagname[attribute='value']
    -> h1[id='header']
    -> h1[class='entry-title']
    -> input[placeholder='Enter username']
    -> input[placeholder='Enter password']
    -> button[type='submit']
    -> input[type='text'][id='username']    
    -> form[action='/login']>input[id=email][name='email']

4. contains or substring Selector: This method is used to select elements that contain 
                                 a specific substring in their attribute value.
   e.g. tagname[attribute*='substring']
    -> h1[class*='entry']
    -> input[id*='user']
    -> button[id*='submit']
    -> div[class*='container']
    -> a[href*='login']
    -> img[src*='logo']
    -> textarea[name*='dd']


    """