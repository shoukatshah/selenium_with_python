from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.logger import get_logger

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.log = get_logger()

    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")

    def open_login_page(self):
        self.driver.get("https://www.saucedemo.com/")

    def login(self, username, password):
        username_elem = self.driver.find_element(*self.USERNAME_INPUT)
        username_elem.send_keys(username)
        password_elem = self.driver.find_element(*self.PASSWORD_INPUT)
        password_elem.send_keys(password)
        login_elem = self.wait.until(EC.element_to_be_clickable(self.LOGIN_BUTTON))
        login_elem.click()
