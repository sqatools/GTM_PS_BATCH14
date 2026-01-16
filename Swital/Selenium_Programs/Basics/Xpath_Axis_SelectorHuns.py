from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("https://selectorshub.com/xpath-practice-page/")

# Example of Xpath Axis Selectors
#1. child axis
driver.find_element(By.XPATH, "//div[@id='tableWrapper']/child::table")
driver.find_element(By.XPATH, "//table[@id='resultTable']/child::thead")
driver.find_element(By.XPATH, "//tr/child::th[@class='header'][1]")

#2. parent axis
driver.find_element(By.XPATH, "//table/parent::div[@id=tableWrapper']")
driver.find_element(By.XPATH, "//thead/parent::table[@id= 'resultTable']")
driver.find_element(By.XPATH, "//th[@class='header']/parent::tr") 

#3. ancestor axis
driver.find_element(By.XPATH, "//th[@class='header']/ancestor::table")
driver.find_element(By.XPATH, "//th[@class='header']/ancestor::div[1]")
driver.find_element(By.XPATH, "(//tr/ancestor::table)[1]")

#4. descendant axis
driver.find_element(By.XPATH, "//table/descendant::th[@class='header'][2]")
driver.find_element(By.XPATH, "//div[@id='tableWrapper']/descendant::th[@class='header'][1]")

#5. following sibling axis
driver.find_element(By.XPATH, "(//th[@class='header']/following-sibling::th)[1]")
driver.find_element(By.XPATH, "//td[text() ='Garry White']/following-sibling::td")

#6. preceding sibling axis
driver.find_element(By.XPATH, "(//th[@class='header']/preceding-sibling::th)[1]")//ask
driver.find_element(By.XPATH, "(//td[text() ='Enabled']/preceding-sibling::td[text() ='ESS'])[1]") //ask

#7. following axis
driver.find_element(By.XPATH, "//a[text() ='Username']/following::th[1]")
driver.find_element(By.XPATH, "(//th[@class='header']/following::tr)[2]")
driver.find_element(By.XPATH, "//th[@class='header']/following::h3[text()='Useful Links for learning']")

#8. preceding axis
driver.find_element(By.XPATH, "//tr[@class='usr_acn']/preceding::th[@class='header'][3]")
driver.find_element(By.XPATH, "//td[text()= 'Garry White']/preceding::th[@class='header'][4]")