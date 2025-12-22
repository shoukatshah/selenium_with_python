import pytest
import time
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.checkout_complete_page import CheckoutCompletePage
from utils.logger import get_logger

log = get_logger()

class TestCheckout:
    @pytest.fixture(autouse=True)
    def setup(self, driver):
        # Login
        login_page = LoginPage(driver)
        login_page.open_login_page()
        login_page.login("standard_user", "secret_sauce")
        self.products_page = ProductsPage(driver)
        assert self.products_page.verify_page_loaded()
        self.cart_page = CartPage(driver)
        # Add product to cart and go to cart page
        self.products_page.add_multiple_product_to_cart([0,2,4])
        self.cart_page.click_cart_icon()
        self.cart_page.verify_page_loaded()
        # Go to checkout
        self.checkout_page = CheckoutPage(driver)
        self.checkout_page.click_checkout()
        self.checkout_page.verify_checkout_step1_loaded()
        yield
        log.info("===== TEARDOWN: Checkout test completed =====")

    @pytest.fixture
    def setup_checkout_step2(self):
        self.checkout_page.complete_checkout_step1(
            first_name="John",
            last_name="Doe",
            postal_code="12345"
        )
        self.checkout_page.verify_checkout_step2_loaded()
    
    def test_checkout_calculations(self, setup_checkout_step2):
        log.info("Test: Checkout price calculations")
        self.checkout_page.verify_calculation()
        item_total = self.checkout_page.get_item_total()
        tax = self.checkout_page.get_tax()
        total = self.checkout_page.get_total()
        
        log.info(f"✅ Calculations: Item Total=${item_total}, Tax=${tax}, Total=${total}")

    def test_complete_checkout_successfully(self, driver, setup_checkout_step2):
        log.info("Test: Complete checkout successfully")
        self.checkout_page.click_finish()
        complete_page = CheckoutCompletePage(driver)
        complete_page.verify_page_loaded()
        success_msg = complete_page.get_success_message()
        assert "Thank you for your order!" in success_msg
        assert "Your order has been dispatched" in success_msg
        
        log.info("✅ Checkout completed successfully")
        
        # Test back home button
        complete_page.click_back_home()
        assert "inventory" in driver.current_url, "Should be back on products page"
        
        log.info("✅ Back Home button works correctly")