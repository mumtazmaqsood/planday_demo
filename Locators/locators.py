

class Locators:


    #login pages locators
    cookies_btn = "//button[@id='cookie-consent-button']"

    form_ele = "//form[@id='login']"
    username_textbox = "#Username"
    password_textbox = "#Password"
    login_btn = "//button[@id='MainLoginButton']"


    #invalid login and password locators
    wrong_username_txt = "#Username-validation-error"
    wrong_password_txt = "#Password-validation-error"



    # Employee Dashboards' locators
    schedule_link = "//a[text()='Schedule']"  # getting 2 elements

    count_employees_xpath = "//div[@class='row-header3__text']" #getting 4 elements,
    count_employee_rows = "div.virtualized-board__row"  #getting 4 rows
    # count_employee_rows1 = "div.virtualized-board__row + div" #getting 3 rows


    #shift gird
    shift_grid = "//div[@class='board-slot board-slot--clickable']"
    shift_start = "//input[@id='shiftStartEnd_start']"
    shift_end = "//input[@id='shiftStartEnd_end']"
    create_shift_btn = "//button[text()='Create']"
    delete_shift_btn = "//button[text()='Delete']"

