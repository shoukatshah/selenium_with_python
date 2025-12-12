from pages.login_page import LoginPage
from utils.logger import get_logger
import pytest

log = get_logger()
def test_valid_login(driver):
    log.info("==== START TEST: valid login ====")
    page = LoginPage(driver)
    page.open_login_page()
    if not page.verify_url():
        raise Exception(f"❌ URL mismatch — stopping test execution")
    if not page.verify_page_title():
        page.log.error("❌ Page title mismatch — stopping test execution")
    page.verify_input_fields() # verify input fields
    page.login("standard_user", "secret_sauce") #Login with correct credentails
    log.info("==== END TEST: valid login ====")
@pytest.mark.only
def test_invalid_login(driver):
    log.info("==== START TEST: invalid login ====")
    page = LoginPage(driver)
    page.open_login_page()
    if not page.verify_url():
        raise Exception(f"❌ URL mismatch — stopping test execution")
    page.verify_input_fields()
    page.login("wrongUser", "wrongPass")
    page.verify_error_message_displayed()
    log.info("==== END TEST: invalid login ====")
