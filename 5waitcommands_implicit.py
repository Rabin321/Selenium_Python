from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox(executable_path="F:\geckodriver.exe")
driver.get("http://demo.guru99.com/test/newtours/")  # Let opening website takes some time

driver.implicitly_wait(5) # implict wait is applicable for all the elements on the page
# we can only specify implicity wait only one time at the begenning of the code
assert "Welcome: Mercury Tours" in driver.title #verify the title. if correct return true else false

driver.find_element_by_name("userName").send_keys("mercury")
driver.find_element_by_name("password").send_keys("mercury")

driver.find_element_by_name("submit").click()

