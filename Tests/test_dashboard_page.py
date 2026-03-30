import pytest
from Pages.dashboard_page import DashboardPageActions
from Config.config import Locators, TestData


@pytest.mark.usefixtures("boot")
class TestDashboard:

    def test_in_time(self, boot):
        dashboard_page = DashboardPageActions(boot)
        dashboard_page.punch_in()
        assert TestData.success_message == dashboard_page.success_message
        assert TestData.success_save_message == dashboard_page.success_save_message

    def test_out_time(self, boot):
        dashboard_page = DashboardPageActions(boot)
        dashboard_page.punch_out()
        assert TestData.success_message == dashboard_page.success_message
        assert TestData.success_save_message == dashboard_page.success_save_message

    # def test_in_time_null(self, boot):
    #     dashboard_page = DashboardPageActions(boot)
    #     dashboard_page.null_punch_in()
        # assert TestData.null_date_msg == dashboard_page.null_time_msg
        # assert TestData.null_time_msg == dashboard_page.null_time_msg
        # assert TestData.success_message != dashboard_page.success_message
        # assert TestData.success_save_message != dashboard_page.success_save_message

    def test_assign_leave(self, boot):
        dashboard_page = DashboardPageActions(boot)
        dashboard_page.assign_leave()
        # print(boot.current_url)
        assert TestData.success_message == dashboard_page.success_message
        assert TestData.success_save_message == dashboard_page.success_save_message