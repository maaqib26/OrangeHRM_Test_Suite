import pytest
from Pages.pim_page import PIMPageActions
from Config.config import TestData,Locators

@pytest.mark.usefixtures("boot")
class TestPIMDelete:

    def test_delete_existing_employee(self,boot):
        pim_page = PIMPageActions(boot)
        pim_page.navigate_to_employee_list()
        pim_page.search_by_employee_id()
        pim_page.delete_first_record()
        pim_page.search_by_employee_id()

        assert pim_page.is_no_records_displayed(), f"Employee with ID {TestData.target_id} was not deleted successfully."
