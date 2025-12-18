import pytest
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from utils.logger import get_logger
from selenium.webdriver.support.select import Select

log = get_logger()

class TestCartPage:
    @pytest.fixture(autouse=True)
    def setup(self, driver):
        """Login and navigate to products page before each test"""
        login_page = LoginPage(driver)
        login_page.open_login_page()
        login_page.login("standard_user", "secret_sauce")
        self.products_page = ProductsPage(driver)
        assert self.products_page.verify_page_loaded()
        self.cart_page = CartPage(driver)
    
    def test_cart_page(self):
         self.products_page.add_multiple_product_to_cart([0,2,4])
         self.cart_page.click_cart_icon()
         self.cart_page.verify_page_loaded()
         self.cart_page.get_cart_item_info(0)
         