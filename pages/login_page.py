from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from utils.logger import get_logger

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.log = get_logger()
    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    LOGIN_URL = "https://www.saucedemo.com/"
    LOGIN_CONTAINER = (By.CLASS_NAME, "login_container")
    ERROR_MESSAGE = (By.XPATH, "//h3[@data-test='error']")
    CART_ICON = (By.CSS_SELECTOR, "[data-test='shopping-cart-link']")

    def open_login_page(self):
        self.driver.get(self.LOGIN_URL)

    def verify_url(self):
        self.log.info("Verifying login page loaded properly")
        current_url = self.driver.current_url
        if current_url == self.LOGIN_URL:
            self.log.info(f"✅ URL verified: {current_url}")
            return True
        else:
            self.log.error(f"❌ URL mismatch. Expected: {self.LOGIN_URL}, Got: {current_url}")
            return False
        
    def verify_page_title(self):
        page_title = self.driver.title
        excepted_title = "Swag Labs"
        if page_title == excepted_title:
            self.log.info(f"✅ Page title verified: {page_title}")
            return True
        else:
            self.log.error(f"❌ Page title mismatch. Expected: {excepted_title}, Got: {page_title}")

    def verify_input_fields(self):
        #Username field
        username_field = self.wait.until(EC.visibility_of_element_located(self.USERNAME_INPUT))
        assert username_field.is_displayed(), "Username field is not displayed"
        assert username_field.is_enabled(), "Username field is not enabled"
        assert username_field.get_attribute("placeholder") == "Username", "Username placeholder text is incorrect"
        self.log.info("✅ Username field verified")
        #Password field
        password_field = self.wait.until(EC.visibility_of_element_located(self.PASSWORD_INPUT))
        assert password_field.is_displayed(), "Password field is not displayed"
        assert password_field.is_enabled(), "Password field is not enabled"
        assert password_field.get_attribute("placeholder") == "Password", "Password placeholder text is incorrect"
        self.log.info("✅ Password field verified")
        #Login button
        login_button = self.wait.until(EC.visibility_of_element_located(self.LOGIN_BUTTON))
        assert login_button.is_displayed(), "Login button is not displayed"
        assert login_button.is_enabled(), "Login button is not enabled"
        assert login_button.get_attribute("value") == "Login", f"Login button text incorrect."
        self.log.info("✅ Login button verified")

    def verify_error_message_displayed(self, expected_error=None):
            try:
                error_element = self.wait.until(EC.visibility_of_element_located(self.ERROR_MESSAGE))
                assert error_element.is_displayed(), "Error message is not displayed"
                actual_error = error_element.text
                if expected_error:
                    if expected_error in actual_error:
                        self.log.info(f"✅ Error message displayed and matched: {actual_error}")
                    else:
                        self.log.error(f"❌ Error message mismatch. Expected '{expected_error}' in '{actual_error}'")
                else:
                    self.log.warning(f"⚠ Error message displayed: {actual_error}")
                return actual_error

            except TimeoutException:
                self.log.info("✅ No error message displayed")
                return None
            

    def login(self, username, password):
        self.wait.until(EC.visibility_of_element_located(self.LOGIN_CONTAINER))
        self.log.info("✅ Login container is visible")
        username_elem = self.driver.find_element(*self.USERNAME_INPUT)
        username_elem.send_keys(username)
        password_elem = self.driver.find_element(*self.PASSWORD_INPUT)
        password_elem.send_keys(password)
        login_elem = self.wait.until(EC.element_to_be_clickable(self.LOGIN_BUTTON))
        login_elem.click()
        cart_icon = self.wait.until(EC.visibility_of_element_located(self.CART_ICON))
        assert cart_icon.is_displayed(), "Cart Icon is not being displayed"

