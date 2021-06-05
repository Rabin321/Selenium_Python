import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox(executable_path="F:\geckodriver.exe")
driver.get("https://www.lambdatest.com/selenium-automation")

driver.find_element_by_id("useremail").send_keys("Hello@gmail.com")
driver.find_element_by_xpath("/html/body/div[2]/section[1]/div/div/form/div/button").click()  # start testing button
# start testing button click garepaxi naya url kholxa so siddhai garna paudaina.

# explicit wait
wait = WebDriverWait(driver, 10)

element = wait.until(EC. element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div/div/div/form/div[4]/label/samp")))
element.click()


