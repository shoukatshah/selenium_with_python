import pytest
import time
from pages.login_page import LoginPage
from utils.user_manager import UserManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from utils.logger import get_logger

log = get_logger()

@pytest.mark.parametrize("user_role", ["standard","problem", "performance"])
def test_user_roles(driver, user_role):
    """Test different user roles"""
    user = UserManager.get_user(user_role)
    
    login_page = LoginPage(driver)
    login_page.open_login_page()
    login_page.login(user.username, user.password)
