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
    
    def test_products_displayed(self):
        """Test that products are displayed"""
        count = self.products_page.get_products_count()
        assert count > 0
        log.info(f"✅ Found {count} products")
    
    def test_page_title(self):
        """Test page title is correct"""
        assert "inventory" in self.products_page.driver.current_url
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

    def test_sort_by_name_a_to_z(self):
        log.info("Test: Sort by Name A-Z")
        self.products_page.verify_sorting_by_name_az()

    def test_sort_by_name_z_to_a(self):
        log.info("Test: Sort by Name Z-A")
        self.products_page.verify_sorting_by_name_za()

    def test_sort_by_price_low_to_high(self):
        log.info("Test: Sort by Price low to high")
        self.products_page.verify_sorting_by_price_low_to_high()

    def test_sort_by_price_high_to_low(self):
        log.info("Test: Sort by Price high to low")
        self.products_page.verify_sorting_by_price_high_to_low()
