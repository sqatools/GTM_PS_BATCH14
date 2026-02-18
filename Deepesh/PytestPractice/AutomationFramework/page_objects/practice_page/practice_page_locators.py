from selenium.webdriver.common.by import By

class PracticePageLocators:
    USERNAME_FIELD = (By.ID, "username")
    PASSWORD_FIELD = (By.ID, "password")
    ADDRESS_FIELD = (By.ID, "address")
    MALE_RADIO_BUTTON = (By.ID, "male")
    FEMALE_RADIO_BUTTON = (By.ID, "female")

    ################ Checkbox Locators ################
    JAVA_CHECKBOX = (By.ID, "java")
    PYTHON_CHECKBOX = (By.ID, "python")
    SELENIUM_CHECKBOX = (By.ID, "selenium")


    ################ Dropdown Locators ################
    COUNTRY_DROPDOWN = (By.ID, "country")
    SKILLS_DROPDOWN = (By.ID, "skills")


    ################### Upload FILE LOCATORS ###################
    UPLOAD_FILE_INPUT = (By.ID, "fileUpload")
    DATEPICKER_INPUT = (By.ID, "datePicker")



