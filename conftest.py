from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pytest
import time

@pytest.fixture(scope="class")
def driver():
    options = Options()

    prefs = {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False
    }

    options.add_experimental_option("prefs", prefs)
    options.add_argument("--disable-infobars")
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-save-password-bubble")

    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    yield driver
    time.sleep(10)
    #input("Press enter key to quit.....")
    driver.quit()
