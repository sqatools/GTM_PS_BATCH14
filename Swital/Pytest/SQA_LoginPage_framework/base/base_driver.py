from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains


class BasePage:

    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    # open url
    def open(self, url):
        self.driver.get(url)

    # find element
    def find(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    # click element
    def click(self, locator):

        element = self.wait.until(EC.element_to_be_clickable(locator))

        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

        try:
            element.click()

        except:
            self.driver.execute_script("arguments[0].click();", element)

    # type text
    def enter_text(self, locator, text):
        element = self.find(locator)
        element.clear()
        element.send_keys(text)

    # get text
    def get_text(self, locator):
        element = self.find(locator)
        return element.text

    # check visibility
    def is_visible(self, locator):
        try:
            self.wait.until(EC.visibility_of_element_located(locator))
            return True
        except TimeoutException:
            return False

    # scroll
    def scroll_to_element(self, locator):
        element = self.find(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    # hover
    def hover(self, locator):
        element = self.find(locator)
        ActionChains(self.driver).move_to_element(element).perform()

    # get page title
    def get_title(self):
        return self.driver.title
    
    def get_current_url(self):
        return self.driver.current_url

    def go_back(self):
        self.driver.back()