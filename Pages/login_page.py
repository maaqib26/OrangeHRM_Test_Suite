from selenium.common import NoSuchElementException, ElementNotVisibleException
from selenium.webdriver.common.by import By
from Config.config import TestData,Locators
from Tests.conftest import ChromeDriverManager
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPageActions:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 100)

    def valid_login(self):
        try:
            # Enter the username and password
            valid_username = self.wait.until(EC.presence_of_element_located((By.NAME,Locators().username)))
            valid_username.send_keys(TestData.valid_Username)
            valid_password = self.wait.until(EC.presence_of_element_located((By.NAME, Locators().password)))
            valid_password.send_keys(TestData.valid_Password)

            # Click the login button
            login_button = self.wait.until(EC.element_to_be_clickable((By.XPATH,Locators().submit_button)))
            login_button.click()
            self.wait.until(EC.url_to_be(Locators.dashboard_url))


        # Handle any exceptions that may occur
        except (NoSuchElementException, ElementNotVisibleException) as e:
            print("ERROR : ", e)

    def invalid_login(self):
        try:
            # Enter the username and password
            invalid_username = self.wait.until(EC.presence_of_element_located((By.NAME, Locators().username)))
            invalid_username.send_keys(TestData.invalid_Username)
            invalid_password = self.wait.until(EC.presence_of_element_located((By.NAME, Locators().password)))
            invalid_password.send_keys(TestData.invalid_Password)

            # Click the login button
            login_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, Locators().submit_button)))
            login_button.click()

        # Handle any exceptions that may occur
        except (NoSuchElementException, ElementNotVisibleException) as e:
            print("ERROR : ", e)

    def forgot_password(self):
        """
        TC ID - TC_PIM_01
        Test Objective - Forgot Password link validation on login page
        """
        try:
            # Click on the Forgot Password Link
            forgot_password = self.wait.until(EC.element_to_be_clickable((By.XPATH, Locators().forgot_password)))
            forgot_password.click()

            # Verify is the username is visible and then enter the username from the excel
            username = self.wait.until(EC.presence_of_element_located((By.NAME, Locators().forgot_password_username)))
            if username.is_displayed():
                username.send_keys(TestData.valid_Username)
            else:
                print("Username is not visible")

            # Click on the reset button
            reset_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, Locators().reset_password_button)))
            reset_button.click()

            # Wait for the reset confirmation message to appear
            self.reset_confirmation = self.wait.until(
                EC.presence_of_element_located((By.XPATH, Locators().reset_password_success)))

            # Handle any exceptions that may occur
        except (NoSuchElementException, ElementNotVisibleException) as e:
            print("ERROR : ", e)




