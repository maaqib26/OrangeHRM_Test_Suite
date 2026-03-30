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



class MyInfoPageActions:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 100)

    def change_dp(self):
        login = LoginPageActions(self.driver)
        login.valid_login()
        try:
            self.wait.until(EC.element_to_be_clickable((By.XPATH,Locators.my_info))).click()
            self.wait.until(EC.element_to_be_clickable((By.XPATH,Locators.emp_image))).click()
            self.wait.until(EC.presence_of_element_located((By.XPATH, Locators.change_pic_button))).click()
            input_path = self.wait.until(EC.presence_of_element_located((By.XPATH, Locators.input_button)))
            input_path.send_keys(TestData.upload_photo)
            self.wait.until(EC.presence_of_element_located((By.XPATH, Locators.save_button))).click()
            self.success_message = self.wait.until(EC.presence_of_element_located((By.XPATH,Locators.success_mesg))).text
            self.success_update_message = self.wait.until(EC.presence_of_element_located((By.XPATH, Locators.success_update_mesg))).text

        # # Handle any exceptions that may occur
        except (NoSuchElementException, ElementNotVisibleException) as e:
            print("ERROR : ", e)

    def add_membership(self):
        login = LoginPageActions(self.driver)
        login.valid_login()
        try:
            self.wait.until(EC.element_to_be_clickable((By.XPATH,Locators.my_info))).click()
            self.wait.until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT,Locators.membership_link))).click()
            self.wait.until(EC.element_to_be_clickable((By.XPATH,Locators.add_membership_btn))).click()
            self.wait.until(EC.element_to_be_clickable((By.XPATH,Locators.membership_type))).click()
            self.wait.until(EC.element_to_be_clickable((By.XPATH,Locators.membership_selection))).click()
            self.wait.until(EC.element_to_be_clickable((By.XPATH,Locators.membership_save))).click()
            self.success_message = self.wait.until(EC.presence_of_element_located((By.XPATH,Locators.success_mesg))).text
            self.success_save_message = self.wait.until(EC.presence_of_element_located((By.XPATH, Locators.success_save_mesg))).text

        # # Handle any exceptions that may occur
        except (NoSuchElementException, ElementNotVisibleException) as e:
            print("ERROR : ", e)

    def add_attachment(self):
        login = LoginPageActions(self.driver)
        login.valid_login()
        try:
            self.wait.until(EC.element_to_be_clickable((By.XPATH,Locators.my_info))).click()
            self.wait.until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT,Locators.membership_link))).click()
            self.wait.until(EC.element_to_be_clickable((By.XPATH,Locators.add_attachment_btn))).click()
            self.wait.until(EC.element_to_be_clickable((By.XPATH,Locators.browse_btn))).click()
            input_path = self.wait.until(EC.presence_of_element_located((By.XPATH, Locators.input_button)))
            input_path.send_keys(TestData.upload_attachement)
            self.wait.until(EC.element_to_be_clickable((By.XPATH,Locators.membership_save))).click()
            self.success_message = self.wait.until(EC.presence_of_element_located((By.XPATH,Locators.success_mesg))).text
            self.success_save_message = self.wait.until(EC.presence_of_element_located((By.XPATH, Locators.success_save_mesg))).text

        # # Handle any exceptions that may occur
        except (NoSuchElementException, ElementNotVisibleException) as e:
            print("ERROR : ", e)