

from pydoc import text

from selenium.webdriver.common.by import By


class DynamicTablePageLocator:
    table_locator = (By.XPATH, "//table[@class='table table-striped']")
    column_headers_locator = (By.XPATH, "column_headers = (By.XPATH, "//div[@role = 'columnheader']")")

    chrome_row_locator = (
        By.XPATH, "//table[@class='table table-striped']//tbody/tr[td[text()='Chrome']]")

    chrome_cpu_atbottom_locator = (By.XPATH, "//p[@class='bg-warning p-1']")
