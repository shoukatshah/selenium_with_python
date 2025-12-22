from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.logger import get_logger

class CheckoutCompletePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.log = get_logger()
    
    PAGE_TITLE = (By.CLASS_NAME, "title")
    COMPLETE_HEADER = (By.CLASS_NAME, "complete-header")
    COMPLETE_TEXT = (By.CLASS_NAME, "complete-text")
    PONY_EXPRESS_IMAGE = (By.CLASS_NAME, "pony_express")
    BACK_HOME_BUTTON = (By.ID, "back-to-products")
    
    def verify_page_loaded(self):
        self.log.info("Verifying checkout complete page")
        assert "checkout-complete" in self.driver.current_url, \
            f"Not on checkout complete page. URL: {self.driver.current_url}"
        title = self.wait.until(EC.visibility_of_element_located(self.PAGE_TITLE))
        assert title.text == "Checkout: Complete!", \
            f"Expected 'Checkout: Complete!', got '{title.text}'"
        header = self.driver.find_element(*self.COMPLETE_HEADER)
        assert header.text == "Thank you for your order!", \
            f"Expected success message, got '{header.text}'"
        assert self.driver.find_element(*self.PONY_EXPRESS_IMAGE).is_displayed()
        self.log.info("✅ Checkout complete page loaded successfully")
        return True
    
    def get_success_message(self):
        header = self.driver.find_element(*self.COMPLETE_HEADER).text
        text = self.driver.find_element(*self.COMPLETE_TEXT).text
        return f"{header}\n{text}"
    
    def click_back_home(self):
        self.log.info("Clicking Back Home button")
        self.driver.find_element(*self.BACK_HOME_BUTTON).click()