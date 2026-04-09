from selenium.common import NoSuchElementException, ElementNotVisibleException, StaleElementReferenceException, \
    TimeoutException
from selenium.webdriver.common.by import By
from Config.config import TestData,Locators
import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Pages.login_page import LoginPageActions
from selenium.webdriver.common.keys import Keys
import time
from Tests import conftest

class PIMPageActions:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

        login = LoginPageActions(self.driver)
        login.valid_login()

        self.wait.until(EC.element_to_be_clickable((By.XPATH, Locators.pim_menu))).click()

    def navigate_to_employee_list(self):
        # login = LoginPageActions(self.driver)
        # login.valid_login()
        # self.wait.until(EC.element_to_be_clickable((By.XPATH,Locators.pim_menu))).click()
        self.wait.until(EC.element_to_be_clickable((By.XPATH,Locators.employee_list_tab))).click()

    def search_by_employee_id(self):
        # Using clear() before send_keys is a best practice for filter inputs
        id_field = self.wait.until(EC.visibility_of_element_located((By.XPATH, Locators.search_id_input)))
        id_field.clear()
        id_field.send_keys(TestData.target_id)
        self.wait.until(EC.presence_of_element_located((By.XPATH, Locators.search_btn))).click()

    def delete_first_record(self):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, Locators.delete_icon))).click()
        self.wait.until(EC.element_to_be_clickable((By.XPATH, Locators.confirm_delete_btn))).click()

    def is_no_records_displayed(self):
        return self.wait.until(EC.visibility_of_element_located((By.XPATH, Locators.no_records_msg))).is_displayed()

    def select_all_employees(self):
        # Ensure the table has loaded rows first
        self.wait.until(EC.visibility_of_any_elements_located((By.XPATH, Locators.table_rows)))
        # Click the header checkbox to select all
        self.wait.until(EC.element_to_be_clickable((By.XPATH, Locators.select_all_checkbox))).click()

    def delete_selected_records(self):
        # The button only appears after selection
        # time.sleep(10)
        self.wait.until(EC.element_to_be_clickable((By.XPATH, Locators.delete_selected_btn))).click()
        # Confirm in the popup
        # time.sleep(10)
        self.wait.until(EC.element_to_be_clickable((By.XPATH, Locators.confirm_bulk_delete))).click()

    def get_row_count(self):
        # Returns the number of employees currently visible in the table
        rows = self.driver.find_elements(By.XPATH, Locators.table_rows)
        return len(rows)

    def get_logged_in_username(self):
        # This gets the name visible in the top-right corner
        return self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME,Locators.profile_name_header))).text

    def get_first_row_text(self):
        # Returns the text of the first row to verify it's the Admin
        return self.wait.until(EC.visibility_of_element_located((By.XPATH, Locators.table_rows))).text

    def filter_by_status(self, status_text):
        # 1. Open the dropdown using the locator string
        self.wait.until(EC.element_to_be_clickable((By.XPATH, Locators.emp_status_dropdown))).click()

        # 2. Dynamically build the XPATH for the specific status
        # This makes your code work for 'Full-Time', 'Freelance', etc., using one line
        dynamic_option = f"//*[contains(text(), '{status_text}')]"
        self.wait.until(EC.element_to_be_clickable((By.XPATH, dynamic_option))).click()

        # 3. Click Search
        self.driver.find_element(By.XPATH, Locators.search_btn).click()

    def verify_results_accuracy(self, expected_value):
        try:

            # Wait for the table to refresh
            self.wait.until(EC.visibility_of_element_located((By.XPATH, Locators.table_rows)))

            # Combine row locator with the cell index to get the status column
            cells_xpath = f"{Locators.table_rows}{Locators.status_cell_index}"
            cells = self.driver.find_elements(By.XPATH, cells_xpath)

            # Logic check
            for cell in cells:
                if cell.text != expected_value:
                    return False
            return True

        except TimeoutException:
            # We use find_elements (plural) so it doesn't throw another error if not found
            no_rec_element = self.driver.find_element(By.XPATH, Locators.no_records_locator)
            if no_rec_element.is_displayed():
                print(f"There are no {expected_value} records")
                return True

            print("there are no rows AND no 'No Records' message, something is wrong (like a crash)")
            return False

    def sort_by_first_name_ascending(self):
        # 1. Click the sort icon specifically
        sort_icon = self.wait.until(EC.element_to_be_clickable((By.XPATH, Locators.first_name_sort)))
        sort_icon.click()

        # 2. sort A-Z
        ascending_btn = self.wait.until(EC.element_to_be_clickable((By.XPATH, Locators.first_name_ascending)))
        ascending_btn.click()

        # 3. CRITICAL: Wait for the table to refresh/re-sort
        self.wait.until(EC.invisibility_of_element_located((By.XPATH, Locators.oxd_loader)))

    def get_all_first_names(self):
        # 1. Find all cells in the First Name column
        # Using find_elements (plural) to get the whole column
        name_elements = self.driver.find_elements(By.XPATH, Locators.first_name_cells)

        # 2. Extract the text from each element
        # We use .strip() to remove any accidental whitespace
        # We use .lower() to ensure sorting comparison is case-insensitive

        names = []
        for element in name_elements:
            # print(element.text)
            text = element.text.lower()
            if text != "":
                names.append(text)

        # names = [element.text.strip().lower() for element in name_elements if element.text.strip() != ""]
        print(f"Captured Names from UI: {names}")
        return names
