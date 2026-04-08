import pytest
from Pages.pim_page import PIMPageActions
from Config.config import TestData,Locators

@pytest.mark.usefixtures("boot")

class TestPIMFilter:

    # Parameterize concept
    @pytest.mark.parametrize("status_to_test", [
        TestData.status_freelance,
        TestData.status_full_time
     # You can add as many as you want here
    ])

    def test_verify_full_time_filter(self, boot, status_to_test):
        pim_page = PIMPageActions(boot)
        pim_page.filter_by_status(status_to_test)

        # 3. Assert
        is_valid = pim_page.verify_results_accuracy(status_to_test)
        assert is_valid, f"Table contains records that are not {status_to_test}"
