from pages.login_page import LoginPage
from utils.logger import get_logger

log = get_logger()

def test_valid_login(driver):
    log.info("==== START TEST: valid login ====")

    page = LoginPage(driver)
    page.open_login_page()
    page.login("standard_user", "secret_sauce")

    #assert page.get_success_message() == "Logged In Successfully"

    log.info("==== END TEST: valid login ====")


def test_invalid_login(driver):
    log.info("==== START TEST: invalid login ====")

    page = LoginPage(driver)
    page.open_login_page()
    page.login("wrongUser", "wrongPass")

    #assert "invalid" in page.get_error_message().lower()

    #log.info("==== END TEST: invalid login ====")
