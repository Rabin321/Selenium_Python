from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox(executable_path="F:\geckodriver.exe")
driver.get("http://demo.guru99.com/test/newtours/")

# conditional commands return boolean value .i.e true or false

username = driver.find_element_by_name("userName") # yo userName inspect garera name="userName" ko leko ho.
print(username.is_displayed())  # returns true or false based on ele status.

print(username.is_enabled())

passw = driver.find_element_by_name("password") #==> inspect garera name="password"
print(passw.is_displayed())
print(passw.is_enabled())

# now sending/giving username and password
username.send_keys("mercury")
passw.send_keys("mercury")

driver.find_element_by_name("submit").click()# inspect garera name="submit"


