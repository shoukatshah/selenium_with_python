import pytest
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.checkout_complete_page import CheckoutCompletePage
from utils.logger import get_logger
from pages.menu_page import MenuPage

log = get_logger()

class TestMenuBar:
    @pytest.fixture(autouse=True)
    def setup(self,driver):
        login_page = LoginPage(driver)
        self.menu_page = MenuPage(driver)
        login_page.open_login_page()
        login_page.login("standard_user", "secret_sauce")
        
    def test_menu_bar(self):
        self.menu_page.open_menu()
        log.info("✅ Menu bar opened successfully")
        self.menu_page.close_menu()
        log.info("✅ Menu bar closed successfully")

    def test_logout(self):
        self.menu_page.logout()
