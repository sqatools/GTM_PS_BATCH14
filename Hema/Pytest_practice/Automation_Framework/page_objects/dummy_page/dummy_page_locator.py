from selenium.webdriver.common.by import By

class DummyPageLocator:
   # personal info
   FIRST_NAME = (By.XPATH, "//span[contains(text(), 'First Name')]/following-sibling::input")
   LAST_NAME = (By.XPATH, "//span[contains(text(), 'Last Name')]/following-sibling::input")
   BILLING_ADDRESS = (By.ID, "billing_address")
   EMAIL_ADDRESS = (By.ID, "billing_email")
   # date and gender
   BIRTHDAY = (By.ID, "birthday")
   GENDER_MALE = (By.ID, "male")
   GENDER_FEMALE = (By.ID, "female")
   # journey type
   ONEWAY = (By.ID, "oneway")
   ROUNDTRIP = (By.ID, "roundtrip")
   # travel details
   FROM_CITY = (By.ID, "fromcity")
   DEST_CITY = (By.ID, "destcity")
   PREFECTURE = (By.NAME, "prefecture")
   POSTCODE = (By.NAME, "postcode")
   # ticket options (list of radio buttons under ticket section)
   # ticket options are inside a left-aligned div containing a ul
   TICKET_OPTIONS = (By.XPATH, "//div[@align='left']//ul//input[@type='radio']")
