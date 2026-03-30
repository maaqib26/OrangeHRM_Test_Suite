import pytest
from Pages.dashboard_page import DashboardPageActions
from Config.config import Locators, TestData
from Pages.myinfo_page import MyInfoPageActions


@pytest.mark.usefixtures("boot")
class TestMyinfo:

    def test_change_dp(self, boot):
        myinfo_page = MyInfoPageActions(boot)
        myinfo_page.change_dp()
        assert TestData.success_message == myinfo_page.success_message
        assert TestData.success_update_message == myinfo_page.success_update_message

    def test_add_membership(self, boot):
        myinfo_page = MyInfoPageActions(boot)
        myinfo_page.add_membership()
        assert TestData.success_message == myinfo_page.success_message
        assert TestData.success_save_message == myinfo_page.success_save_message

    def test_add_attachment(self, boot):
        myinfo_page = MyInfoPageActions(boot)
        myinfo_page.add_attachment()
        assert TestData.success_message == myinfo_page.success_message
        assert TestData.success_save_message == myinfo_page.success_save_message