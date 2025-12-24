import pytest
import time
from pages.login_page import LoginPage
from utils.user_manager import UserManager
from selenium.webdriver.common.by import By

@pytest.mark.parametrize("user_role", ["standard", "locked", "problem", "performance"])
def test_user_roles(driver, user_role):
    """Test different user roles"""
    user = UserManager.get_user(user_role)
    
    login_page = LoginPage(driver)
    login_page.open_login_page()
    login_page.login(user.username, user.password)
    
    if user_role == "locked":
        # Verify error message
        error = login_page.get_error_message()
        assert "locked out" in error.lower()
    elif user_role == "performance":
        # Add longer waits
        print("Long wait")
        #login_page.wait = WebDriverWait(driver, 30)
    elif user_role == "problem":
        # Test specific issues
        # Example: Check if images load correctly
        images = driver.find_elements(By.TAG_NAME, "img")
        broken_images = []
        for img in images:
            if not img.get_attribute("naturalWidth") or img.get_attribute("naturalWidth") == "0":
                broken_images.append(img.get_attribute("src"))
        if broken_images:
            pytest.xfail(f"Problem user has broken images: {broken_images}")