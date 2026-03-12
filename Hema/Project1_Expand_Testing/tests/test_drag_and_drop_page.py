from page_objects.drag_and_drop_page.drag_and_drop_page import DragAndDropPage
from page_objects.drag_and_drop_page.drag_and_drop_page_data import *

import pytest
import time


@pytest.mark.usefixtures("get_driver")
class TestDragAndDropPage:

    @pytest.fixture(scope="function", autouse=True)
    def setup(self):
        self.test_drag_and_drop = DragAndDropPage(self.driver)

    def test_drag_and_drop_page(self):
        time.sleep(5)
        self.test_drag_and_drop.launch_website(website_url)
        self.test_drag_and_drop.perform_drag_and_drop()
        time.sleep(5)