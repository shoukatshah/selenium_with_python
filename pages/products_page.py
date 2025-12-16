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
    
    def get_sort_dropdown(self):
        return Select(self.driver.find_element(*self.SORT_DROPDOWN))
    
    def get_sorting_options(self):
        sort_dropdown = self.get_sort_dropdown()
        return [option.text for option in sort_dropdown.options]
    
    def select_sort_option(self, option_text):
        self.log.info(f"Selecting sort option: {option_text}")
        sort_dropdown = self.get_sort_dropdown()
        sort_dropdown.select_by_visible_text(option_text)
        self.wait.until(EC.presence_of_all_elements_located(self.PRODUCT_CARDS))

    def get_all_product_names(self):
        names = []
        for product in self.get_all_products():
            name = product.find_element(*self.PRODUCT_NAMES).text
            names.append(name)
        return names
    
    def get_all_product_prices(self):
        prices = []
        for product in self.get_all_products():
            price_text = product.find_element(*self.PRODUCT_PRICES).text
            price = float(price_text.replace('$', ''))
            prices.append(price)
        return prices

    def verify_sorting_by_name_az(self):
        self.select_sort_option("Name (A to Z)")
        product_names = self.get_all_product_names()
        sorted_names = sorted(product_names)
        assert product_names == sorted_names, \
             f"Products not sorted A-Z. Got: {product_names}"
        self.log.info("✅ Products sorted by Name A-Z")

    def verify_sorting_by_name_za(self):
        self.select_sort_option("Name (Z to A)")
        product_names = self.get_all_product_names()
        sorted_names = sorted(product_names, reverse= True)
        assert product_names == sorted_names, \
            f"Products not sorted Z-A. Got: {product_names}"
        self.log.info("✅ Products sorted by Name Z-A")

    def verify_sorting_by_price_low_to_high(self):
        self.select_sort_option("Price (low to high)")
        product_prices = self.get_all_product_prices()
        sorted_prices = sorted(product_prices)
        assert product_prices == sorted_prices, \
            f"Products not sorted low to high. Got: {product_prices}"
        self.log.info("✅ Products sorted by Price low to high")

    def verify_sorting_by_price_high_to_low(self):
        self.select_sort_option("Price (high to low)")
        product_prices = self.get_all_product_prices()
        sorted_prices = sorted(product_prices, reverse= True)
        assert product_prices == sorted_prices, \
            f"Products not sorted high to low. Got: {product_prices}"
        self.log.info("✅ Products sorted by Price high to low")

        
    
    



