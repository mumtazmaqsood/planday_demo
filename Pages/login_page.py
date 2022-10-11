from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from Locators.locators import Locators
import time

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.cookies_btn = Locators.cookies_btn

        #login
        self.form_ele = Locators.form_ele
        self.username_textbox = Locators.username_textbox
        self.password_textbox = Locators.password_textbox
        self.login_btn = Locators.login_btn
        #wrong msg
        self.wrong_username_txt = Locators.wrong_username_txt
        self.wrong_password_txt = Locators.wrong_password_txt


        self.get_form = driver.find_element(By.XPATH, self.form_ele)
        self.get_username = driver.find_element(By.CSS_SELECTOR, self.username_textbox)
        self.get_password = driver.find_element(By.CSS_SELECTOR, self.password_textbox)
        self.get_login_btn = driver.find_element(By.XPATH, self.login_btn)
        # self.get_invalid_login_msg = driver.find_elements(By.XPATH, self.invalid_login_msg)

    def enter_coke_btn(self):
        try:
            self.driver.find_element(By.XPATH, self.cookies_btn).click()
            print(f"<b> 1 & 2- Website opened & Cookies accepted </b><br>")
        except:
            print("Not Clickable")

    def verify_login_page_elements(self):
        print(f"<b> 3- Verification of Login page elements </b><br>")
        # print(f" \t is_form displayed: {self.get_form.is_displayed()} and checked: {self.get_form.is_selected()} <br>")
        print(f"3.1 is_username displayed: {self.get_username.is_displayed()} and enabled: {self.get_username.is_enabled()} <br>")
        print(f"3.2 is_password displayed: {self.get_password.is_displayed()} and enabled: {self.get_password.is_enabled()} <br>")
        print(f"3.3 is_login_btn displayed: {self.get_login_btn.is_displayed()} and enabled: {self.get_login_btn.is_enabled()} <br>")
        # self.get_login_btn.click()

    def invalid_login(self):
        print(f"<b> 4- Invalid credentials -- Partially implemented--captcha implementation is not handled </b><br>")
        self.get_username.send_keys("mumtaz")
        self.get_password.send_keys("APItestig21")
        # self.get_login_btn.click()
        #login btn is not clicked bcz captcha is active, remian disable until captcha handle
        time.sleep(1)
        try:
            msg1, msg2 = self.check_invalid_login_text()
            print(f"<b>validation error: {msg1} <br> {msg2}</b>")
            self.assertEqual(msg1, 'The username or password is incorrect.')
        except:
            print("cannot access elements<br>")

    def valid_login(self):
        print(f"<b> 5- Verifying with valid credentials </b><br>")
        self.get_username.send_keys(Keys.CONTROL, 'a')
        self.get_username.send_keys(Keys.BACKSPACE)
        self.get_username.send_keys("plandayqa@outlook.com")

        self.get_password.send_keys(Keys.CONTROL, 'a')
        self.get_password.send_keys(Keys.BACKSPACE)
        self.get_password.send_keys("APItesting21")
        self.get_login_btn.click()
        time.sleep(2)

    def check_invalid_login_text(self):
        wrong_username_msg = self.driver.find_element(By.CSS_SELECTOR, self.wrong_username_txt).text
        wrong_password_msg = self.driver.find_element(By.CSS_SELECTOR, self.wrong_password_txt).text
        return wrong_username_msg, wrong_password_msg