import time
from selenium.webdriver.common.by import By
from Locators.locators import Locators
from datetime import date

class EmployeeDashboard:

    def __init__(self, driver):
        self.driver = driver
        self.schedule_link = Locators.schedule_link
        self.count_employee_rows = Locators.count_employee_rows
        self.shift_grid = Locators.shift_grid
        self.emp_count = []
        self.current_date = date.today()
        #schedule shift locators
        # ----------------------------------------------------------------
        self.shift_start = Locators.shift_start
        self.shift_end = Locators.shift_end
        self.create_shift_btn = Locators.create_shift_btn
        self.delete_shift_btn = Locators.delete_shift_btn
        # ------------------------------------------------------------------
        self.click_schdedule_link = self.driver.find_element(By.XPATH, self.schedule_link)


    # ----------------------VERIFY SCHEDULE URL START-------------------------------------------------------------
    def verify_schedule_url(self):
        """
        Verifying URL has '/page/schedule'
        """
        print(f"<b> 5-Verify the URL contains /page/schedule </b><br>")
        self.click_schdedule_link.click()
        currentURL = self.driver.current_url
        print(f"current url:{currentURL} <br>")
        try:
            assert '/page/schedule' in currentURL
        except:
            print(f"<b>{currentURL} is not containing '/page/schedule'</b><br>")
        time.sleep(1)
    # ----------------------VERIFY SCHEDULE URL END---------------------------------------------------------------

    # ----------------------COUNT EMPLOYEE START------------------------------------------------------------------
    def count_employees(self):
        """
        Counting the total employees in the left gird and
        Display the employees names and used assertion
        """
        print(f"<b>6- Counting & assert Number of employees </b><br>")
        self.driver.switch_to.frame(0)
        print("swithced to iframe <br>")
        self.emp_count = self.driver.find_elements(By.CSS_SELECTOR, self.count_employee_rows)
        # self.emp_count = self.driver.find_elements(By.CSS_SELECTOR, ".virtualized-board__row .row-header3__text__title")
        print(f"<br> <b>Employee counts:{len(self.emp_count)-1}</b> <br>")
        for i in range(1, len(self.emp_count)):
            print(f"<b>{i}:{self.emp_count[i].text}</b> <br>")
            assert len(self.emp_count)-1 is 3
            # return self.emp_count
    # ----------------------COUNT EMPLOYEE END------------------------------------------------------------------

    # ----------------------SHEDULE SHIFT START------------------------------------------------------------------
    def shedule_shift(self):
        """
        Employee can schedule shift
        if shself.ift is already scheduled --> it delete it and then again create it
        """
        print(f"<br><b>7 & 8- Creating Shift for Employee One and checking it has been displayed </b><br>")
        # getting schedule gird 28 attributes
        time_gird = self.driver.find_elements(By.XPATH, self.shift_grid)
        print(f"length of time gird:{len(time_gird)} <br>")

        formate_date = self.current_date.strftime('%B %d, %Y') + " Employee One"
        # print(f"formate date:{formate_date} <br>")
        for i in range(len(time_gird)):
            if formate_date in time_gird[i].get_attribute('aria-label'):
                print("<b>Found</b>")
                time_gird[i].click()
                try:
                    self.delete_shift_time()
                    time.sleep(2)
                    time_gird[i].click()
                    self.add_shift_time()
                    print(f"<b>Verifying Shift has been created: {time_gird[i].get_attribute('aria-label')}</b><br>")
                except:
                    self.add_shift_time()
                    print(f"<b>Verifying Shift has been created: {time_gird[i].get_attribute('aria-label')}</b><br>")
            else:
                print("Not found")
            print(f"{time_gird[i].get_attribute('aria-label')}<br>")


    # ----------------------SHEDULE SHIFT END------------------------------------------------------------------




    #-----------------------------FUNCTIONS-----------------------------------------------------------------

    #delete shift time --> deleting shift time
    def delete_shift_time(self):
        delete_shift = self.driver.find_element(By.XPATH, self.delete_shift_btn)
        delete_shift.click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.delete_shift_btn).click()

    #add shift time -->  adding shift time
    def add_shift_time(self):
        self.driver.find_element(By.XPATH, self.shift_start).send_keys("09:00")
        self.driver.find_element(By.XPATH, self.shift_end).send_keys("17:00")
        self.driver.find_element(By.XPATH, self.create_shift_btn).click()
        # self.count_employees()

   #-----------------------------END FUNCTIONS-----------------------------------------------------------------