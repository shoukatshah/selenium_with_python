from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.select import Select
from utils.logger import get_logger

class CheckoutPage:
    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.log = get_logger()

    PAGE_TITLE = (By.CLASS_NAME,"title")
    CHECKOUT_BTN = (By.XPATH,"//button[contains(text(),'Checkout')]")
    FIRST_NAME_INPUT = (By.ID, "first-name")
    LAST_NAME_INPUT = (By.ID, "last-name")
    POSTAL_CODE_INPUT = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")
    CANCEL_BUTTON = (By.ID, "cancel")
    ERROR_MESSAGE = (By.XPATH,"//h3[@data-test='error']")
    PAYMENT_INFO_LABEL  = (By.CSS_SELECTOR, "[data-test='payment-info-label']")
    SHIPPING_INFO_LABEL = (By.CSS_SELECTOR, "[data-test='shipping-info-label']")
    PRICE_TOTAL_LABEL   = (By.CSS_SELECTOR, "[data-test='total-info-label']")
    OVERVIEW_ITEMS = (By.CLASS_NAME, "cart_item")
    ITEM_TOTAL = (By.CLASS_NAME, "summary_subtotal_label")
    TAX = (By.CLASS_NAME, "summary_tax_label")
    TOTAL = (By.CLASS_NAME, "summary_total_label")
    FINISH_BUTTON = (By.ID, "finish")
    CANCEL_BUTTON_STEP2 = (By.ID, "cancel")

    def click_checkout(self):
        self.log.info("Clicking Checkout button")
        self.driver.find_element(*self.CHECKOUT_BTN).click()

    def verify_checkout_step1_loaded(self):
        self.log.info("Verifying checkout information page")
        assert "checkout-step-one" in self.driver.current_url, \
            f"Not on checkout step 1. URL: {self.driver.current_url}"
        assert self.driver.find_element(*self.FIRST_NAME_INPUT).is_displayed()
        assert self.driver.find_element(*self.LAST_NAME_INPUT).is_displayed()
        assert self.driver.find_element(*self.POSTAL_CODE_INPUT).is_displayed()
        self.log.info("✅ Checkout step 1 loaded successfully")
        return True
    
    def enter_checkout_information(self,first_name="", last_name="", postal_code=""):
        if first_name:
            first_name_field = self.driver.find_element(*self.FIRST_NAME_INPUT)
            first_name_field.clear()
            first_name_field.send_keys(first_name)
        if last_name:
            last_name_field = self.driver.find_element(*self.LAST_NAME_INPUT)
            last_name_field.clear()
            last_name_field.send_keys(last_name)
        if postal_code:
            postal_code_field = self.driver.find_element(*self.POSTAL_CODE_INPUT)
            postal_code_field.clear()
            postal_code_field.send_keys(postal_code)

    def click_continue(self):
        self.log.info("Clicking Continue button")
        self.driver.find_element(*self.CONTINUE_BUTTON).click()
    
    def click_cancel(self):
        self.log.info("Clicking Cancel button")
        self.driver.find_element(*self.CANCEL_BUTTON).click()

    def verify_checkout_step2_loaded(self):
        assert "checkout-step-two" in self.driver.current_url, \
            f"Not on checkout step 2. URL: {self.driver.current_url}"
        title = self.wait.until(EC.visibility_of_element_located(self.PAGE_TITLE))
        assert title.text == "Checkout: Overview",\
            f"Expected: Checkout: Overview, got '{title.text}'"
        assert self.driver.find_element(*self.SHIPPING_INFO_LABEL).is_displayed()
        assert self.driver.find_element(*self.PAYMENT_INFO_LABEL).is_displayed()
        assert self.driver.find_element(*self.PRICE_TOTAL_LABEL).is_displayed()
        return True
    def complete_checkout_step1(self,first_name,last_name,postal_code):
        self.enter_checkout_information(first_name, last_name, postal_code)
        self.click_continue()

    def get_item_total(self):
        item_total_text = self.driver.find_element(*self.ITEM_TOTAL).text
        return float(item_total_text.split('$')[1])
    def get_tax(self):
        tax_text = self.driver.find_element(*self.TAX).text
        return float(tax_text.split('$')[1])
    def get_total(self):
        total_text = self.driver.find_element(*self.TOTAL).text
        return float(total_text.split('$')[1])
    def verify_calculation(self):
        item_total = self.get_item_total()
        tax = self.get_tax()
        total = self.get_total()
        calculated_total = round(item_total + tax,2)
        assert total == calculated_total, \
            f"Total mismatch. Expected {calculated_total}, got {total}"
        return True
    
    def get_overview_items(self):
        return self.driver.find_elements(*self.OVERVIEW_ITEMS)
    
    def get_overview_item_info(self, index=0):
        items = self.get_overview_items()
        assert 0 <= index <= len(items), f"Invalid index"
        item = items[index]
        return {
            'name': item.find_element(By.CLASS_NAME, "inventory_item_name").text,
            'description': item.find_element(By.CLASS_NAME, "inventory_item_desc").text,
            'price': float(item.find_element(By.CLASS_NAME, "inventory_item_price").text.replace('$', ''))
        }
    
    def click_finish(self):
        self.log.info("Clicking Finish button")
        self.driver.find_element(*self.FINISH_BUTTON).click()
    
    def click_cancel_step2(self):
        self.log.info("Clicking Cancel button in overview")
        self.driver.find_element(*self.CANCEL_BUTTON_STEP2).click()

        
        
        

    