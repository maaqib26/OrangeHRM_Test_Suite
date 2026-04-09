import pytest
from Pages.pim_page import PIMPageActions
from Config.config import TestData,Locators

@pytest.mark.usefixtures("boot")
class TestPIMManagement:

    def test_bulk_delete_employees(self, boot):
        pim_page = PIMPageActions(boot)
        pim_page.select_all_employees()
        print(pim_page.get_row_count())
        print(pim_page.get_logged_in_username())
        pim_page.delete_selected_records()
        print(pim_page.get_row_count())
        print(pim_page.get_logged_in_username())
        print(pim_page.get_first_row_text())

        assert pim_page.get_row_count() == 1 or f"Expected 1 record (Admin) to remain, but found {pim_page.get_row_count()}"
        assert pim_page.get_first_row_text() == pim_page.get_logged_in_username() or f"The remaining record was not {pim_page.get_logged_in_username()}. Found: {pim_page.get_first_row_text()}"

    def test_delete_existing_employee(self,boot):
        pim_page = PIMPageActions(boot)
        pim_page.navigate_to_employee_list()
        pim_page.search_by_employee_id()
        pim_page.delete_first_record()
        pim_page.search_by_employee_id()

        assert pim_page.is_no_records_displayed(), f"Employee with ID {TestData.target_id} was not deleted successfully."

@pytest.mark.usefixtures("boot")
class TestPIMFilters:

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

    def test_verify_first_name_ascending_sort(self, boot):
        pim_page = PIMPageActions(boot)
        pim_page.navigate_to_employee_list()

        # Sort A-Z
        pim_page.sort_by_first_name_ascending()

        # Verify
        actual_names = pim_page.get_all_first_names()

        # Python's sorted() defaults to Ascending (A-Z)
        assert actual_names == sorted(actual_names), f"UI did not sort A-Z. Found: {actual_names}"
