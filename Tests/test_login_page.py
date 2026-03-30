import pytest
from Pages.login_page import LoginPageActions
from Config.config import Locators


@pytest.mark.usefixtures("boot")
class TestLogin:

    def test_valid_login(self, boot):
        login_page = LoginPageActions(boot)
        login_page.valid_login()
        assert Locators.dashboard_url == boot.current_url

    def test_invalid_login(self, boot):
        login_page = LoginPageActions(boot)
        login_page.invalid_login()
        assert Locators.dashboard_url != boot.current_url

    def test_forgot_password(self, boot):
        reset_password = LoginPageActions(boot)
        reset_password.forgot_password()
        assert Locators().reset_confirm_print == reset_password.reset_confirmation.text
