import pytest
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from utils.logger import get_logger
from selenium.webdriver.support.select import Select

log = get_logger()

class TestProductsPage:
    @pytest.fixture(autouse=True)
    def setup(self, driver):
        """Login and navigate to products page before each test"""
        login_page = LoginPage(driver)
        login_page.open_login_page()
        login_page.login("standard_user", "secret_sauce")
        self.products_page = ProductsPage(driver)
        assert self.products_page.verify_page_loaded()

    @pytest.mark.skip
    def test_products_displayed(self):
        """Test that products are displayed"""
        count = self.products_page.get_products_count()
        assert count > 0
        log.info(f"✅ Found {count} products")

    @pytest.mark.skip
    def test_page_title(self):
        """Test page title is correct"""
        assert "inventory" in self.products_page.driver.current_url

    @pytest.mark.skip
    def test_sort_dropdown_displayed(self):
        log.info("Test: Sorting options availability")
        options = self.products_page.get_sorting_options()
        expected_options = [
            "Name (A to Z)",
            "Name (Z to A)", 
            "Price (low to high)",
            "Price (high to low)"
        ]
        assert options == expected_options, \
            f"Sorting options mismatch. Expected {expected_options}, got {options}"
        log.info("✅ All sorting options available")

    @pytest.mark.skip
    def test_sort_by_name_a_to_z(self):
        log.info("Test: Sort by Name A-Z")
        self.products_page.verify_sorting_by_name_az()

    @pytest.mark.skip
    def test_sort_by_name_z_to_a(self):
        log.info("Test: Sort by Name Z-A")
        self.products_page.verify_sorting_by_name_za()

    @pytest.mark.skip
    def test_sort_by_price_low_to_high(self):
        log.info("Test: Sort by Price low to high")
        self.products_page.verify_sorting_by_price_low_to_high()

    @pytest.mark.skip
    def test_sort_by_price_high_to_low(self):
        log.info("Test: Sort by Price high to low")
        self.products_page.verify_sorting_by_price_high_to_low()

    def test_add_product_to_cart(self):
        log.info("Test: Add product to cart")
        self.products_page.add_product_to_cart(4)

    def test_add_multiple_products_to_cart(self):
        log.info("Test: Add multiple products to cart")
        added_products = self.products_page.add_multiple_product_to_cart([0,2,4])
        self.products_page.verify_cart_count(3)
        log.info(f"✅ Added {len(added_products)} products: {added_products}")
    
    def test_add_all_products_to_cart(self):
        log.info("Test: Add all products to cart")
        self.products_page.add_all_products_to_cart()

    def test_navigation_to_cart_page(self):
        log.info("Test: Cart icon navigation")
        self.products_page.add_product_to_cart(0)
        self.products_page.go_to_cart()

    def test_click_product_to_view_details(self):
        log.info("Test: Click product to view details")
        self.products_page.view_product_details_page('Sauce Labs Bike Light')

