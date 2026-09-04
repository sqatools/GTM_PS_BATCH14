from page_objects.dynamic_table_page.dynamic_table_page_data import *
from page_objects.dynamic_table_page.dynamic_table_page import DynamicTablePage
import pytest


@pytest.mark.usefixtures("get_driver")
class TestDynamicTablePage:

    @pytest.fixture(scope="function", autouse=True)
    def setup(self):
        self.test_dynamic_table = DynamicTablePage(self.driver)

    def test_chrome_cpu_value_consistency(self):
        self.test_dynamic_table.launch_website(website_url)

        cpu_value = self.test_dynamic_table.get_chrome_cpu()
        cpu_value_bottom = self.test_dynamic_table.get_chrome_cpu_bottom()

        assert cpu_value == cpu_value_bottom
