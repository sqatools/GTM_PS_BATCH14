- selenium_base.py file will present in base folder

- page file, locator file and data file will present in specific page directory.

e.g.  page_objects/dummy_page/dummy_page.py, dummy_page_locators.py, dummy_page_data.py

- All test files will available in "tests" folder and their specific
feature folder.

- conftest.py file will available inside the tests directory.

- from file import class name
or if its in another folder than
from .folder.filename import class name # . dot before from mention on which level/directory


without ... also u can import files
:from foldername.filename import class name to import class

from ...base.selenium_base import SeleniumBase 
from .dummy_page_locator import DummyPageLocator
