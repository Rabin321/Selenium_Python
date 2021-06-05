import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox(executable_path="F:\geckodriver.exe")
driver.get("https://www.expedia.com/")

driver.find_element_by_class_name("uitk-faux-input").send_keys("usa")
time.sleep(3)
driver.find_element_by_xpath("/html/body/section/div/div/button").click()

driver.find_element_by_id("d1-btn").clear()

driver.find_element_by_id("d1-btn").send_keys("jun 25")
time.sleep(2)

driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div[2]/div/div/div[3]/button").click()
driver.find_element_by_id("d1-btn").clear()
driver.find_element_by_id("d2-btn").send_keys("jun 29")
driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div[2]/div/div/div[3]/button").click()

driver.find_element_by_id("add-flight-switch").click()
#search button
driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/div[1]/div/div[1]/div[4]/div/div/div[2]/div/div/div/div[1]/div/form/div[3]/div[2]/button").click()
