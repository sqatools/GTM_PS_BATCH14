import time

from selenium import webdriver
from selenium.webdriver.common.by import By



#initialize the Chrome driver
driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("https://sqatools.in/automation-practice-page/")
#locator by XPATH
#absolute XPATH
heading_text=driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/main/article/div/header/h1")
heading_text.click()
print("Heading Text:", heading_text.text)
time.sleep(2)

#relative XPATH with text() method
#step_by_playwriter_text=driver.find_element(By.XPATH,"//ul[@class='wp-block-latest-posts__list wp-block-latest-posts']/li/a[text()='Step-by-Step Guide to Use Playwright Annotations']")
#step_by_playwriter_text.click()
#time.sleep(5)

#relative xpath-contains() method
contains_text=driver.find_element(By.XPATH,"//textarea[contains(text(), 'Enter address')]")
contains_text.clear()
contains_text.send_keys("polo fields ,sandton Johnusbhurg")
time.sleep(5)

#relative xpath-starts-with() method
Click_to_replace_button=driver.find_element(By.XPATH,"//button [starts-with(text(), 'Click ')]")
Click_to_replace_button.click()
time.sleep(5)

#relative xpath and OR operator---Interactive with single elememnt using AND operator
# AND operator
Enable_button=driver.find_element(By.XPATH, "//input[@type='text' and @value='Enabled']")
Enable_button.click()
time.sleep(5)

# OR operator
#OR_operator=driver.find_element(By.XPATH, "//input[@type='text' or @value='Enabled']")
#OR_operator.click()


"""
# What is XPath?
# XPath (XML Path Language) is a query language used to navigate and select nodes from an XML
#
# There are two main types of XPath:
# 1. Absolute XPath: It defines the path from the root element to the desired element.
#    It starts with a single slash (/). For example, /html/body/div[1]/h1.
#    e.g.
#    ->  /html/body/div[1]/div/div[1]/main/article/div/header/h1
#    -> /html/body/div[1]/div/div[1]/main/article/div/div/section[1]/h2
    e.g.(above example header tag)
     -> /html/body/div[1]/div/div[1]/main/article/div/header/h1
    

2. Relative XPath: It defines the path from the current node to the desired element. 
  It starts with a double slash (//). For example, 
    e.g. //taganame[@attribute='value'] or //*[@attribute='value']
    -> //h1[@id='header'].
    -> //h1[@class='entry-title']  or  //*[@class="entry-title"]
    -> //h1[@itemprop="headline"]
    -> //input[@placeholder="Enter username"]
    -> //input[@placeholder="Enter password"]
    -> //button[@type="submit"]

###################################################################
Relative Xpath Methods:
1. text() Method: This method is used to select elements based on their text content.
   e.g. //tagname[text()='textvalue']
   -> //h2[text()='XPath Syntax']
   -> //ul[@class='wp-block-list']/li/a[text()='Python Basic Programs']
   -> //button[text()='Confirm Alert']
   -> //td[text()='Deepesh']
   -> //input[@id="fileUpload"]
   
    -- e.g. above example : //ul[@class='wp-block-latest-posts__list wp-block-latest-posts']
                             /li/a[text()='Step-by-Step Guide to Use Playwright Annotations
   


2. contains() Method: This method is used to select elements that contain a specific substring in their attribute value or text content.
   e.g. //tagname[contains(@attribute,'substring')] or 
        //tagname[contains(text(),'substring')]

    -> //h1[contains(@class, "entry")]
    -> //h1[contains(text(), 'Automation Practice Page')]
    -> (//h1[contains(text(), 'Automation Practice Page')])[1]
    
    -> above expmaple ://textarea[contains(text(), 'Enter address')]


3. starts-with() Method: This method is used to select elements whose attribute value or text content starts with a specific substring.
   e.g. //tagname[starts-with(@attribute,'substring')] or 
        //tagname[starts-with(text(),'substring')]

    -> //input[starts-with(@id, 'user')]
    -> //h2[starts-with(text(), 'XPath')]

    -> //button[starts-with(text(), 'Click to')]
    -> //button[starts-with(@id, 'stale')]


4. and & or Operators: These operators are used to combine multiple conditions in an XPath expression.
   e.g. //tagname[@attribute1='value1' and @attribute2='value2'] or 
        //tagname[@attribute1='value1' or @attribute2='value2']

    -> //input[@type='text' and @id='username']
    -> //input[@type='password' and @id='password']
    -> //input[@type='submit' or @id='loginButton']
    -> //button[@type='button' or @id='alertButton']
    -> //input[@type='text' and @value="Enabled"]
    -> //input[@type='text' or @value="Enabled"]

5. index Method: This method is used to select elements based on their position in a list of similar elements.
   e.g. (//tagname[@attribute='value'])[index]  

    -> (//input[@type='text'])[1]
    -> (//input[@type='text'])[2]
    -> (//button[@type='button'])[1]
    -> (//button[@type='button'])[2]
    -> (//h2[contains(text(), 'XPath')])[1]
    -> (//h2[contains(text(), 'XPath')])[2]
#################################################

Xapth Axes:Advance XPATH concepts that allow you to navigate through the XML document structure in various ways.    
Ancestor: Selects all ancestors (parent, grandparent, etc.) of the current node.
e.g. //tagname[@attribute='value']/ancestor::tagnameparent: Selects the parent of the current node.
e.g. //tagname[@attribute='value']/parent::tagname
//th[text()='ID']//ancestor::section---bottom to top

Ancestor-or-self: Selects all ancestors of the current node and the current node itself.

Child: Selects all direct children of the current node.
e.g. //tagname[@attribute='value']/child::tagname
e,g. //div[@class='container']/child::p

//section//child::table/child::tbody


parent: Selects the parent of the current node.
e.g. //tagname[@attribute='value']/parent::tagname  
e.g. //p[@class='text']/parent::div
//th[text()='ID']//parent::tr

Descendant: Selects all descendants (children, grandchildren, etc.) of the current node.
e.g. //tagname[@attribute='value']/descendant::tagname
e.g. //div[@class='container']/descendant::p

//section//child::table/child::thead----top  to bottom
or
//section//child::table//tr


Following: Selects all nodes that come after the current node in the document.
e.g. //tagname[@attribute='value']/following::tagname
e.g. //h2[@class='title']/following::p

preceding: Selects all nodes that come before the current node in the document.
e.g. //tagname[@attribute='value']/preceding::tagname
--//th[text()='Name']//preceding::h2[text()='Web Table']--upper  side no matter withtagname
--//th[text()='Name']//preceding::label[text()='Male']
--//th[text()='Name']/preceding::label[text()='Male']--we can use with single slash also
---//th[text()='Name']//preceding::h2[text()='Text Fields']

Following-sibling: Selects all siblings that come after the current node.
e.g. //tagname[@attribute='value']/following-sibling::tagname
e.g. //h2[@class='title']/following-sibling::p
    //th[text()='Name']//following-sibling::th--afterside sibling
    --//th[text()='Name']/following::td[text()='Developer']--lowe side no matter with tagname
    --//th[text()='Name']/following::input[@id='searchBox']
    

preceding-sibling: Selects all siblings that come before the current node.
e.g. //tagname[@attribute='value']/preceding-sibling::tagname
//th[text()='Name']//preceding-sibling::th---upperside sibling

 

"""