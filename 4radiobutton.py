from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox(executable_path="F:\geckodriver.exe")

driver.get("http://demo.guru99.com/test/newtours/reservation.php")

round_Trip_radiobutton = driver.find_element_by_css_selector("input[value = roundtrip]")
print("Status of roundtrip radio button:", round_Trip_radiobutton.is_selected()) # conditional conditions returns boolean values only

one_Way_radiobutton = driver.find_element_by_css_selector("input[value = oneway]")
print("Status of one way radio button:", one_Way_radiobutton.is_selected())

