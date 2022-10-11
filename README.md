# Planday_demo
This solution is implemented by using 
--> Python
--> selenium + unittest framework
--> for reporting --> used html reports 

# How to execute 
    1- **install python** 
    2- **install selenium, html reports, unittest framework** 
        --> pip install selenium
        --> pip install html-testRunner
        --> pip install unittest
    
    3- **Download the chrome webdriver and put it in your PYTHON's libs folder**
        fx "C:\\python310\\libs\\chromedriver.exe"
        download from here according to your chrome version
        https://chromedriver.chromium.org/downloads

# Description
    Try to implement the POM (Page Object Model) but its basic structure
    of POM, locators, pages, test and reports are in different folder
    There is possiblity to optimize and refactor the code but due to busy schedule I am just providing 
    simple solution 

# Covered Areas 
    1- Open the website
    2- Accepting Cookies
    3- Verify login Page elements
    4- Verify with invalid credentials --> Partially implemented 
    5- Verify with valid credentials  
    6- Verify the URL contains /page/schedule
    7- Counting & assert Number of employees
    8- Creating Shift for Employee One and checking it has been displayed

# What is not covered
    Invalid credentials -- Partially implemented--captcha implementation is not handled



