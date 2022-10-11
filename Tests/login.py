
from selenium import webdriver
import unittest
import time
import HtmlTestRunner

from Pages.login_page import LoginPage
from Pages.employee_dashboard import EmployeeDashboard

class LoginTest(unittest.TestCase):
    driver = None

#setupclass method run once, thats why website open once and
    @classmethod
    def setUpClass(cls):
        path = "C:\\python310\\libs\\chromedriver.exe"
        cls.driver = webdriver.Chrome(path)
        cls.driver.get("https://test1234.planday.com/")
        # cls.driver.maximize_window()
        cls.driver.implicitly_wait(5)

    # Login page
    """
    1- Open the website
    2- Accepting Cookies
    3- Verify login Page elements
    4- Verify with invalid credentials --> 
    5- Verify with valid credentials  
    """
    def test_a_login_page(self):
        self.login = LoginPage(self.driver)
        self.login.enter_coke_btn()
        self.login.verify_login_page_elements()
        self.login.invalid_login()
        self.login.valid_login()


    # Employee Dashboard
    """
    1- Verify the URL contains /page/schedule
    2- Counting & assert Number of employees
    3- Creating Shift for Employee One and checking it has been displayed
    """
    def test_b_verify_employee_dashboard(self):
        self.emp_dash = EmployeeDashboard(self.driver)
        self.emp_dash.verify_schedule_url()
        time.sleep(2)
        self.emp_dash.count_employees()
        self.emp_dash.shedule_shift()

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='Reports'))


