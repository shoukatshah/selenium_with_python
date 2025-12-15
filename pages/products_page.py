from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.select import Select
from utils.logger import get_logger

class ProductsPage:
    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.log = get_logger()

    PAGE_TITLE = (By.CLASS_NAME, "title")
    SORT_DROPDOWN = (By.CLASS_NAME, "product_sort_container")
    PRODUCT_CARDS = (By.CLASS_NAME, "inventory_item")
    PRODUCT_NAMES = (By.CLASS_NAME, "inventory_item_name")
    PRODUCT_PRICES = (By.CLASS_NAME, "inventory_item_price")
    PRODUCT_DESCRIPTIONS = (By.CLASS_NAME, "inventory_item_desc")
    ADD_TO_CART_BUTTONS = (By.XPATH, "//button[contains (text(), 'Add to cart')]")
    REMOVE_BUTTONS = (By.XPATH, "//button[contains (text(), 'Remove')]")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    CART_ICON = (By.CLASS_NAME, "shopping_cart_link")
    MENU_BUTTON = (By.ID, "react-burger-menu-btn")
    LOGOUT_LINK = (By.ID, "logout_sidebar_link")

    def verify_page_loaded(self):
        assert "inventory" in self.driver.current_url, \
        f"Not on products page. URL: {self.driver.current_url}"

        # Verify at least one product is displayed
        products = self.get_all_products()
        assert len(products) > 0, "No products found on products page"
        self.log.info(f"✅ Products page loaded with {len(products)} products")
        return True
    
    def get_all_products(self):
        return self.driver.find_elements(*self.PRODUCT_CARDS)
    
    def get_products_count(self):
        return len(self.get_all_products())
    
    def get_sorting_options(self):
        sort_dropdown = Select(self.driver.find_element(*self.SORT_DROPDOWN))
        return [option.text for option in sort_dropdown.options]
    
    def select_sort_option(self, option_text):
        self.log.info(f"Selecting sort option: {option_text}")
        sort_dropdown = Select(self.driver.find_element(*self.SORT_DROPDOWN))
        sort_dropdown.select_by_visible_text(option_text)
        self.wait.until(EC.presence_of_all_elements_located(self.PRODUCT_CARDS))
    
    



