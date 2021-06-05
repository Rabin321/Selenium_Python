import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox(executable_path="F:\geckodriver.exe")

driver.get("https://github.com/")
print(driver.title)   #FR


driver.get("https://mail.google.com/mail/u/0/#inbox/")
time.sleep(5)
print(driver.title)   #TT

driver.back()   #FR
time.sleep(5)
print(driver.title)

driver.forward()     #TT
time.sleep(5)
print(driver.title)


