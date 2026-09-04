import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver= webdriver.Chrome()
driver.maximize_window()
driver.get("https://sqatools.in/dummy-booking-website/")
driver.implicitly_wait(10)

title= driver.title
print("Page Heading:", title)

page=driver.find_element(By.XPATH,"//h1[contains(text(),'Dummy Tic')]")
print("Heading:", page)

driver.find_element(By.CSS_SELECTOR,"input[value='radio_558']").click()
time.sleep(2)

driver.find_element(By.XPATH,"(//input[@name='firstname'])[1]").send_keys("Sara")
time.sleep(2)

driver.find_element(By.XPATH,"(//input[@name='firstname'])[2]").send_keys("D")
time.sleep(2)

driver.find_element(By.CSS_SELECTOR,"#birthday").send_keys("01/01/2026")
time.sleep(2)

driver.find_element(By.XPATH,"(//input[@id='female'])[1]").click()
time.sleep(2)

dropdown=driver.find_element(By.CSS_SELECTOR,"#admorepass")
select_opt= Select(dropdown)
select_opt.select_by_value("1")
time.sleep(2)

driver.find_element(By.CSS_SELECTOR,"#roundtrip").click()
time.sleep(2)

driver.find_element(By.CSS_SELECTOR,"#fromcity").send_keys("Mumbai")
time.sleep(2)

driver.find_element(By.CSS_SELECTOR,"#destcity").send_keys("Pune")
time.sleep(2)

driver.find_element(By.CSS_SELECTOR,"input[name='departdate']").send_keys("12/03/2026")
time.sleep(2)

driver.find_element(By.CSS_SELECTOR,"input[name='returndate']").send_keys("12/04/2026")
time.sleep(2)

driver.find_element(By.CSS_SELECTOR,"#visadate").send_keys("30/03/2026")
time.sleep(2)

driver.find_element(By.CSS_SELECTOR,"#eamil").click()
time.sleep(2)

driver.find_element(By.CSS_SELECTOR,"#billing_name").send_keys("Sara")
time.sleep(2)

driver.find_element(By.CSS_SELECTOR,"#billing_phone").send_keys("1234567898")
time.sleep(2)

driver.find_element(By.CSS_SELECTOR,"#billing_email").send_keys("abc.d@gmail.com")
time.sleep(2)

driver.find_element(By.CSS_SELECTOR,"#billing_address").send_keys("Mumbai, IN")
time.sleep(2)

country_dd=driver.find_element(By.CSS_SELECTOR,"#billing_country")
select_country= Select(country_dd)
select_country.select_by_visible_text("India")

driver.find_element(By.CSS_SELECTOR,"input[name='postcode']").send_keys("2234")
time.sleep(2)

driver.find_element(By.CSS_SELECTOR,"input[name='prefecture']").send_keys("001")
time.sleep(2)

driver.find_element(By.CSS_SELECTOR,"#street_address1").send_keys("Room No. 33")
time.sleep(2)

driver.find_element(By.CSS_SELECTOR,"#street_address2").send_keys("Main street")
time.sleep(2)

driver.find_element(By.XPATH,"(//input[@type='checkbox'])[1]").click()
time.sleep(2)

driver.find_element(By.XPATH,"(//input[@type='checkbox'])[5]").click()
time.sleep(2)

driver.find_element(By.XPATH,"(//input[@type='checkbox'])[7]").click()
time.sleep(3)
