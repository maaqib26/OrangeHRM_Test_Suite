from selenium.common import NoSuchElementException, ElementNotVisibleException, StaleElementReferenceException
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
