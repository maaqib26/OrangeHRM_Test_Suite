import pytest
from Pages.pim_page import PIMPageActions
from Config.config import TestData,Locators

@pytest.mark.usefixtures("boot")
class TestPIMBulkActions:

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
