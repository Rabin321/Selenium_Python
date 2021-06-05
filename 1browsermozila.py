import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Firefox(executable_path="F:\geckodriver.exe")   #path where the driver is located => this is only firefox driver.
# seperate driver should be downloaded for seperate browsers.

driver.get("https://btcmovies.xyz/")

print(driver.title)      # Gives title of the page.
print(driver.current_url)  # returns the url of the page.
# print(driver.page_source)   # returns html code of page.
driver.find_element_by_xpath("/html/body/div[2]/header/div/div/div[3]/a[1]/span").click() #click on button or anything that open in next tab

time.sleep(5)
driver.close()  # close the driver In case of xpath it closes the parent tab.
# close command closes only one browser at a time. i.e focused browser.

# driver.quit() This command closes all the opened browsers.


