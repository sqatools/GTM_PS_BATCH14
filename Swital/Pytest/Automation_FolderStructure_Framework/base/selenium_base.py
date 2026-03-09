import logging
import os
from datetime import datetime
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

log = logging.getLogger(__name__)

class SeleniumBase:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    def _take_screenshot(self, name):
        folder = "screenshots"
        os.makedirs(folder, exist_ok=True)

        file = f"{name}_{datetime.now().strftime('%H%M%S')}.png"
        path = os.path.join(folder, file)

        self.driver.save_screenshot(path)
        log.error(f"Screenshot saved: {path}")

    def _get_element(self, locator):
        log.info(f"Waiting for element: {locator}")
        return self.wait.until(EC.visibility_of_element_located(locator))

    def click(self, locator):
        try:
            self._get_element(locator).click()
            log.info(f"Clicked on: {locator}")
        except Exception:
            log.exception(f"Click failed for: {locator}")
            self._take_screenshot("click_failed")
            raise

    def enter_text(self, locator, text):
        try:
            element = self._get_element(locator)
            element.clear()
            element.send_keys(text)
            log.info(f"Entered text in: {locator}")
        except Exception:
            log.exception(f"Typing failed for: {locator}")
            self._take_screenshot("type_failed")
            raise

    def get_text(self, locator):
        try:
            text = self._get_element(locator).text
            log.info(f"Text captured from: {locator}")
            return text
        except Exception:
            log.exception(f"Get text failed for: {locator}")
            self._take_screenshot("gettext_failed")
            raise