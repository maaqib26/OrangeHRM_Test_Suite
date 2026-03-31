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

    def navigate_to_employee_list(self):
        login = LoginPageActions(self.driver)
        login.valid_login()
        self.wait.until(EC.element_to_be_clickable((By.XPATH, Locators.time_button))).click()
        self.wait.until(EC.element_to_be_clickable((By.XPATH,Locators.pim_menu))).click()
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
