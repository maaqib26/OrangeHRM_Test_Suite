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



class DashboardPageActions:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 100)

    def punch_in(self):
        login = LoginPageActions(self.driver)
        login.valid_login()
        try:
            self.wait.until(EC.element_to_be_clickable((By.XPATH,Locators.time_button))).click()
            in_date = self.wait.until(EC.presence_of_element_located((By.XPATH,Locators().date_box)))
            # time.sleep(3)
            in_date.send_keys(Keys.CONTROL + 'a')
            # time.sleep(3)
            in_date.send_keys(Keys.DELETE)
            # time.sleep(3)
            in_date.send_keys(TestData.today_date)
            # time.sleep(3)
            in_time = self.wait.until(EC.presence_of_element_located((By.XPATH, Locators().time_box)))
            in_time.send_keys(Keys.CONTROL + 'a')
            in_time.send_keys(Keys.DELETE)
            # time.sleep(3)
            in_time.send_keys(TestData.in_time)
            self.wait.until(EC.element_to_be_clickable((By.XPATH,Locators().in_button))).click()
            print("Punched In on {a} at {b}".format(a=TestData.today_date,b=TestData.in_time))
            self.success_message = self.wait.until(EC.presence_of_element_located((By.XPATH,Locators.time_success))).text
            self.success_save_message = self.wait.until(EC.presence_of_element_located((By.XPATH, Locators.time_success_saved))).text

        # # Handle any exceptions that may occur
        except (NoSuchElementException, ElementNotVisibleException) as e:
            print("ERROR : ", e)

    def punch_out(self):
        login = LoginPageActions(self.driver)
        login.valid_login()

        try:
            self.wait.until(EC.element_to_be_clickable((By.XPATH, Locators().time_button))).click()
            # time.sleep(3)
            out_date = self.wait.until(EC.presence_of_element_located((By.XPATH, Locators.date_box)))
            # time.sleep(3)
            out_date.send_keys(Keys.CONTROL + 'a')
            # time.sleep(3)
            out_date.send_keys(Keys.DELETE)
            # time.sleep(3)
            out_date.send_keys(TestData.today_date)
            # time.sleep(3)
            out_time = self.wait.until(EC.presence_of_element_located((By.XPATH, Locators.time_box)))
            out_time.send_keys(Keys.CONTROL + 'a')
            out_time.send_keys(Keys.DELETE)
            # time.sleep(3)
            out_time.send_keys(TestData.out_time)
            self.wait.until(EC.invisibility_of_element((By.XPATH,Locators.spinning_wheel)))
            self.wait.until(EC.element_to_be_clickable((By.XPATH, Locators.out_button))).click()
            print("Punched Out on {a} at {b}".format(a=TestData.today_date, b=TestData.out_time))
            self.success_message = self.wait.until(EC.presence_of_element_located((By.XPATH, Locators.time_success))).text
            self.success_save_message = self.wait.until(EC.presence_of_element_located((By.XPATH, Locators.time_success_saved))).text

    #Handle any exceptions that may occur
        except (NoSuchElementException, ElementNotVisibleException) as e:
            print("ERROR : ", e)

    # def null_punch_in(self):
    #     login = LoginPageActions(self.driver)
    #     login.valid_login()
    #     try:
    #         self.wait.until(EC.element_to_be_clickable((By.XPATH,Locators.time_button))).click()
    #         self.wait.until(EC.invisibility_of_element((By.XPATH, Locators.spinning_wheel)))
    #         time.sleep(3)
    #         in_date = self.wait.until(EC.presence_of_element_located((By.XPATH,Locators.date_box)))
    #         time.sleep(3)
    #         in_date.send_keys(Keys.CONTROL + 'a')
    #         time.sleep(3)
    #         in_date.send_keys(Keys.DELETE)
    #         time.sleep(3)
            # # in_date.send_keys(TestData.today_date)
            # time.sleep(3)
            # in_time = self.wait.until(EC.presence_of_element_located((By.XPATH, Locators.time_box)))
            # in_time.send_keys(Keys.CONTROL + 'a')
            # in_time.send_keys(Keys.DELETE)
            # time.sleep(3)
            # # in_time.send_keys(TestData.in_time)
            # self.wait.until(EC.element_to_be_clickable((By.XPATH,Locators.in_button))).click()
            # self.null_date_msg = self.wait.until(EC.presence_of_element_located((By.XPATH, Locators.null_date_msg))).text
            # self.null_time_msg = self.wait.until(EC.presence_of_element_located((By.XPATH, Locators.null_time_msg))).text
            # self.success_message = self.wait.until(EC.presence_of_element_located((By.XPATH,Locators.time_success)))
            # self.success_save_message = self.wait.until(EC.presence_of_element_located((By.XPATH, Locators.time_success_saved)))
            # if not self.success_message.is_displayed() and self.success_save_message.is_displayed():
            #     print("Not able to punch In due to null input")
            # else:
            #     print("ERROR: Able to punch In with null input")
        # # Handle any exceptions that may occur
        # except (NoSuchElementException, ElementNotVisibleException) as e:
        #     print("ERROR : ", e)

    def assign_leave(self):
        login = LoginPageActions(self.driver)
        login.valid_login()

        try:
            self.wait.until(EC.element_to_be_clickable((By.XPATH, Locators().assign_leave_button))).click()
            emp_name = self.wait.until(EC.presence_of_element_located((By.XPATH, Locators.emp_name_box)))
            emp_name.send_keys(TestData.employee_name)
            self.wait.until(EC.element_to_be_clickable((By.XPATH, Locators.emp_name_dropdown))).click()
            self.wait.until(EC.element_to_be_clickable((By.XPATH, Locators.leave_type_box))).click()
            self.wait.until(EC.element_to_be_clickable((By.XPATH, Locators.personal_leave))).click()
            from_date = self.wait.until(EC.presence_of_element_located((By.XPATH, Locators.from_date_box)))
            from_date.send_keys(Keys.CONTROL + 'a')
            from_date.send_keys(Keys.DELETE)
            from_date.send_keys(TestData.from_date)
            to_date = self.wait.until(EC.presence_of_element_located((By.XPATH, Locators.to_date_box)))
            to_date.send_keys(Keys.CONTROL + 'a')
            to_date.send_keys(Keys.DELETE)
            to_date.send_keys(TestData.to_date)
            self.wait.until(EC.element_to_be_clickable((By.XPATH, Locators.body))).click()
            self.wait.until(EC.element_to_be_clickable((By.XPATH, Locators.partial_days_box))).click()
            self.wait.until(EC.element_to_be_clickable((By.XPATH, Locators.partial_days_dropdown))).click()
            self.wait.until(EC.element_to_be_clickable((By.XPATH, Locators.duration_box))).click()
            self.wait.until(EC.element_to_be_clickable((By.XPATH, Locators.duration_box_dropdown))).click()
            comments = self.wait.until(EC.presence_of_element_located((By.XPATH, Locators.comments)))
            comments.send_keys(TestData.comments)
            self.wait.until(EC.element_to_be_clickable((By.XPATH, Locators.assign_button))).click()
            self.wait.until(EC.element_to_be_clickable((By.XPATH, Locators.confirm_Button))).click()
            print("Leave granted for {a} on {b} to {c}".format(a=TestData.employee_name, b=TestData.from_date, c=TestData.to_date))
            self.success_message = self.wait.until(EC.presence_of_element_located((By.XPATH, Locators.success_mesg))).text
            self.success_save_message = self.wait.until(EC.presence_of_element_located((By.XPATH, Locators.success_save_mesg))).text

    #Handle any exceptions that may occur
        except (NoSuchElementException, ElementNotVisibleException) as e:
            print("ERROR : ", e)
