from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.logger import get_logger
from pages.login_page import LoginPage

class MenuPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.log = get_logger()
    
    #Locators
    MENU_BUTTON = (By.ID, "react-burger-menu-btn")
    MENU_LIST = (By.CLASS_NAME, "bm-menu")
    CLOSE_MENU_BUTTON = (By.ID, "react-burger-cross-btn")
    MENU_CONTAINER = (By.CLASS_NAME, "bm-menu-wrap")
    # Menu items
    ALL_ITEMS_LINK = (By.ID, "inventory_sidebar_link")
    ABOUT_LINK = (By.ID, "about_sidebar_link")
    LOGOUT_LINK = (By.ID, "logout_sidebar_link")
    RESET_APP_LINK = (By.ID, "reset_sidebar_link")

    def open_menu(self): #opening the menu
        self.log.info("Opening side menu")
        menu_btn = self.wait.until(
            EC.element_to_be_clickable(self.MENU_BUTTON)
            )
        menu_btn.click()
        self.wait.until(
            EC.visibility_of_element_located(self.MENU_CONTAINER)
            )
        self.log.info("✅ Menu opened")

    def close_menu(self): #closing the menu
        self.log.info("Closing side menu")
        self.wait.until(EC.visibility_of_element_located(self.MENU_CONTAINER))
        close_btn = self.wait.until(EC.visibility_of_element_located(self.CLOSE_MENU_BUTTON))
        close_btn.click()
        self.wait.until(EC.invisibility_of_element_located(self.MENU_LIST))
        self.log.info("✅ Menu closed successfully")
    
    def logout(self): #logout from the application
        self.log.info("Logging out")
        self.open_menu()
        self.wait.until(EC.visibility_of_element_located(self.MENU_CONTAINER))
        logout_btn = self.wait.until(EC.presence_of_element_located(self.LOGOUT_LINK))
        self.wait.until(EC.element_to_be_clickable(self.LOGOUT_LINK))
        logout_btn.click()
        self.wait.until(EC.url_contains("saucedemo.com"))
        self.log.info("✅ Logout clicked successfully")

    def go_to_all_items(self):
        """Navigate to all items"""
        self.log.info("Navigating to all items")
        self.open_menu()
        self.driver.find_element(*self.ALL_ITEMS_LINK).click()
    
    def reset_app_state(self):
        """Reset application state"""
        self.log.info("Resetting app state")
        self.open_menu()
        self.driver.find_element(*self.RESET_APP_LINK).click()
        self.close_menu()