from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.logger import get_logger

class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.log = get_logger()

    def open(self, url):
        self.log.info(f"Opening URL: {url}")
        self.driver.get(url)

    def find(self, locator):
        self.log.info(f"Finding element: {locator}")
        return self.wait.until(EC.visibility_of_element_located(locator))

    def click(self, locator):
        self.log.info(f"Clicking element: {locator}")
        self.find(locator).click()

    def type(self, locator, text):
        self.log.info(f"Typing in element {locator}: {text}")
        self.find(locator).send_keys(text)
