import pytest
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from utils.logger import get_logger

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