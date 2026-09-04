from base.selenium_base import SeleniumBase
from page_objects.drag_and_drop_page.drag_and_drop_page_locator import DragAndDropPageLocator

class DragAndDropPage(SeleniumBase):
    def __init__(self, driver):
        super().__init__(driver)

    def launch_website(self, url):
        self.driver.get(url)

    def perform_drag_and_drop(self):
        source = self.get_element(DragAndDropPageLocator.source_element_locator)
        target = self.get_element(DragAndDropPageLocator.target_element_locator)
        self.drag_and_drop(source, target)
        
    