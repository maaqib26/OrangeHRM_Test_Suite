from datetime import datetime
class Locators:
    """
    Login Page Locators
    """
    username = "username"
    password = "password"
    submit_button = "//button[@type='submit']"
    url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
    dashboard_url = "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"
    forgot_password = "//div[@class='orangehrm-login-forgot']//p"
    forgot_password_username = "username"
    reset_password_button = "//div[@class='orangehrm-forgot-password-button-container']//button[2]"
    reset_password_success = "//div[@class='orangehrm-card-container']//h6"
    reset_confirm_print = "Reset Password link sent successfully"

    """
    Dashboard Punch In/Out Locators 
    """

    time_button = "//button//i[@class='oxd-icon bi-stopwatch']"
    date_box = "//input[@placeholder='yyyy-dd-mm']"
    # out_date_box = "//input[@placeholder='yyyy-dd-mm']"
    time_box = "//input[@placeholder='hh:mm']"
    # out_time_box = "//input[@placeholder='hh:mm']"
    in_button = "//button[text()=' In ']"
    out_button = "//button[text()=' Out ']"
    time_success = "//div//p[text()='Success']"
    time_success_saved = "//div//p[text()='Successfully Saved']"
    spinning_wheel = "//div[@class='oxd-loading-spinner']"
    null_date_msg = "(//div//span[text()='Required'])[1]"
    null_time_msg = "(//div//span[text()='Required'])[2]"

    """
    Dashboard Assign Locators 
    """
    assign_leave_button =  "//button[@title='Assign Leave']"
    emp_name_box = "//input[@placeholder='Type for hints...']"
    emp_name_dropdown = "//div[@role='option']/span[text()='Orange  Test']"
    # emp_name_dropdown = "//div[@role='option']/span[text()='Emily Rose Brown']"
    leave_type_box = "//div[@class='oxd-select-text oxd-select-text--active']"
    personal_leave = "//div[@role='listbox']//div[@role='option']/span[text()='CAN - Personal']"
    from_date_box = "//label[text()='From Date']/../following-sibling::div//input"
    to_date_box = "//label[text()='To Date']/../following-sibling::div//input"
    body = "//div[@class='orangehrm-card-container']"
    partial_days_box = "//div[text()='-- Select --']"
    partial_days_dropdown = "//div[@role='option']/span[text()='All Days']"
    duration_box = "//div[text()='-- Select --']"
    duration_box_dropdown = "//div[@role='option']/span[text()='Specify Time']"

    comments = "//textarea[@class='oxd-textarea oxd-textarea--active oxd-textarea--resize-vertical']"
    assign_button = "//button[@type='submit']"
    confirm_Button = "//button[text()=' Ok ']"
    success_mesg = "//div//p[text()='Success']"
    success_save_mesg = "//div//p[text()='Successfully Saved']"

    """
    myinfo page Locators 
    """
    my_info = "//a/span[text()='My Info']"
    emp_image = "//img[@class='employee-image']"
    change_pic_button = "//button[@class='oxd-icon-button oxd-icon-button--solid-main employee-image-action']"
    input_button = "//input[@type='file']"
    save_button = "//button[@type='submit']"
    success_mesg = "//div//p[text()='Success']"
    success_save_mesg = "//div//p[text()='Successfully Saved']"
    success_update_mesg = "//div//p[text()='Successfully Updated']"

    membership_link = "Memberships"
    add_membership_btn = "(//button[text()=' Add '])[1]"
    membership_type = "//label[text()='Membership']//parent::div/following-sibling::div"
    membership_selection = "//div[@role='option']//span[text()='CIMA']"
    membership_save = "//button[text()=' Save ']"
    add_attachment_btn = "(//button[text()=' Add '])[2]"
    browse_btn = "//div[text()='Browse']"
    input_button = "//input[@type='file']"


class TestData:
    """
    Login Page Test Data
    """
    valid_Username = "Admin"
    valid_Password = "admin123"
    invalid_Username = "abc"
    invalid_Password = "xyz"

    """
    Dashboard PunchIn/Out Test Data
    """
    date = datetime.now().date()
    # today_date = date.strftime("%Y-%d-%m")
    today_date = "2025-13-09"
    in_time = "08:00 AM"
    out_time = "06:00 PM"
    success_message = "Success"
    success_save_message = "Successfully Saved"
    punch_out_url = "https://opensource-demo.orangehrmlive.com/web/index.php/attendance/punchOut"
    null_date_msg = "Required"
    null_time_msg = "Required"

    """
    Dashboard Assign Leave Test Data
    """
    employee_name = "Orange Test"
    # employee_name = "Emily Rose Brown"
    from_date = "2025-11-10"
    to_date = "2025-13-10"
    comments = "Leave Granted"
    success_message = "Success"
    success_save_message = "Successfully Saved"

    """
    myinfo page Test Data
    """
    upload_photo = r"C:\Users\moham\Downloads\codekata.png"
    success_message = "Success"
    success_update_message = "Successfully Updated"
    upload_attachement = r"C:\Users\moham\Downloads\test.txt"