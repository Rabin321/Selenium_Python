import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox(executable_path="F:\geckodriver.exe")
driver.get("http://automationpractice.com/")

driver.find_element_by_id("search_query_top").send_keys("Shirts")
driver.find_element_by_xpath("/html/body/div/div[1]/header/div[3]/div/div/div[2]/form/button").click()
driver.find_element_by_xpath("/html/body/div/div[2]/div/div[3]/div[2]/ul/li/div/div[1]/div/a[1]/img").click()
driver.find_element_by_name("Submit").click()
time.sleep(5)
driver.close()
