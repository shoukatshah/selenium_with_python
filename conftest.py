import pytest
from utils.browser import get_driver
import time

@pytest.fixture(scope="class")
def driver():
    driver = get_driver()
    yield driver
    time.sleep(10)
    #input("Press enter key to quit.....")
    driver.quit()
