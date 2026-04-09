from base.selenium_base import SeleniumBase
from page_objects.dynamic_table_page.dynamic_table_page_locator import DynamicTablePageLocator


class DynamicTablePage(SeleniumBase):
    def __init__(self, driver):
        super().__init__(driver)

    def launch_website(self, url):
        self.driver.get(url)

    def get_column_index(self):
        column_headers = self.get_elements(
            DynamicTablePageLocator.column_headers_locator)
        for index, header in enumerate(column_headers):
            if header.text.strip() == "CPU":
                return index + 1
        raise Exception("CPU column not found")

    def get_chrome_cpu(self):
        column_index = self.get_column_index()
        chrome_cpu_locator = (DynamicTablePageLocator.chrome_row_locator[0],
                              DynamicTablePageLocator.chrome_row_locator[1] + f"/td[{column_index}]")
        return self.get_element(chrome_cpu_locator).text.strip()

    def get_chrome_cpu_bottom(self):
        text = self.get_text(
            DynamicTablePageLocator.chrome_cpu_atbottom_locator)
        return text.split(":")[1].strip()
