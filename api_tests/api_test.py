import pytest
from api_client import SauceDemoAPI
from api_tests.api_client import SauceDemoAPI

def test_login_api_success():
    api = SauceDemoAPI()

    response = api.login(
        email="shoukat@webook.com",
        password="hala1234",
        captcha="AUTOMATION_TEST_CAPTCHA",
        signature="AUTOMATION_SIGNATURE"
    )

    assert response.status_code == 200

    data = response.json()
    assert "token" in data