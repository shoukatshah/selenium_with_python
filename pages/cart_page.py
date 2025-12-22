from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.select import Select
from utils.logger import get_logger

class CartPage:
    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.log = get_logger()
    
    PAGE_TITLE = (By.XPATH, "//span[@data-test='title']")
    CART_ITEM = (By.CLASS_NAME, "cart_item")
    CONTINUE_SHOPPING_BTN = (By.ID, "continue-shopping")
    CHECKOUT_BTN = (By.ID, "checkout")
    ITEM_NAME = (By.CLASS_NAME, "inventory_item_name")
    ITEM_DESC = (By.CLASS_NAME, "inventory_item_desc")
    ITEM_PRICE = (By.CLASS_NAME, "inventory_item_price")
    REMOVE_BTN = (By.XPATH, ".//button[contains(text(), 'Remove')]")
    CART_ICON = (By.CLASS_NAME,"shopping_cart_link")

    def click_cart_icon(self):
        cart_icon_btn = self.wait.until(EC.element_to_be_clickable(self.CART_ICON))
        cart_icon_btn.click()
        self.log.info("✅ Cart icon clicked")



    def verify_page_loaded(self):
        self.log.info("Verifying cart page loaded")
        assert "cart" in self.driver.current_url, \
            f"Not on cart page. URL: {self.driver.current_url}"
        title = self.wait.until(EC.visibility_of_element_located(self.PAGE_TITLE))
        assert title.text == "Your Cart", f"Expected 'Your Cart', got '{title.text}'"
        return True
    
    def get_cart_items(self):
        items = self.wait.until(
        EC.presence_of_all_elements_located(self.CART_ITEM)
        )
        self.log.info(f"Found {len(items)} items in cart")
        return items
    
    def get_cart_items_count(self):
        return len(self.get_cart_items())
    
    def get_cart_item_info(self, index=0):
        items = self.get_cart_items()
        assert 0 <= index < len(items), f"Invalid item index: {index}"
        item = items[index]
        return {
            'name':item.find_element(*self.ITEM_NAME).text,
            'description':item.find_element(*self.ITEM_DESC).text,
            'price':item.find_element(*self.ITEM_PRICE).text,
            'remove_button_present':self._is_remove_button_present(item)
        }
    def _is_remove_button_present(self, item_element):
        try:
            item_element.find_element(*self.REMOVE_BTN)
            return True
        except:
            return False
        
    def remove_item_from_cart(self,index=0):
        self.log.info(f"Removing item at index {index} from cart")
        items = self.get_cart_items()
        assert 0 <= index < len(items), f"Invalid item index: {index}"
        item_name = items[index].find_element(*self.ITEM_NAME).text
        remove_btn = items[index].find_element(*self.REMOVE_BTN)
        remove_btn.click()
        self.log.info(f"✅ Removed '{item_name}' from cart")
        return item_name
    
    def click_continue_shopping(self):
        self.log.info("Clicking Continue Shopping")
        self.driver.find_element(*self.CONTINUE_SHOPPING_BTN).click()
        assert "inventory.html" in self.driver.current_url, \
            f"Not inventory.html in url. URL: {self.driver.current_url}"
    
    def click_checkout(self):
        """Click Checkout button"""
        self.log.info("Clicking Checkout button")
        self.driver.find_element(*self.CHECKOUT_BTN).click()
