from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium import webdriver
import time

path = "C:\\python310\\libs\\chromedriver.exe"

driver = webdriver.Chrome(path)
driver.get("https://test1234.planday.com/")
# driver.maximize_window()
time.sleep(2)
driver.find_element(By.XPATH, "//button[@id='cookie-consent-button']").click()
form_ele = driver.find_elements(By.XPATH, "//form[@id='login']")
is_form = driver.find_element(By.XPATH, "//form[@id='login']")
print(f"is_username displayed: {is_form.is_displayed()} and enabled: {is_form.is_selected()} ")

is_username = driver.find_element(By.XPATH, "//input[@id='Username']")
print(f"is_username displayed: {is_username.is_displayed()} and enabled: {is_username.is_enabled()} ")

is_password = driver.find_element(By.XPATH, "//input[@id='Password']")
print(f"is_password displayed: {is_password.is_displayed()} and enabled: {is_password.is_enabled()} ")

is_login_btn = driver.find_element(By.XPATH, "//button[@id='MainLoginButton']")
print(f"is_login_btn displayed: {is_login_btn.is_displayed()} and enabled: {is_login_btn.is_enabled()} ")
is_login_btn.click()
time.sleep(2)





driver.close()