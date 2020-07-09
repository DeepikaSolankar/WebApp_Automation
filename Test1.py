from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome("C:\Users\DEEPIKA\PycharmProjects\FirstSeleniumTest\Drivers\chromedriver.exe")
driver.set_page_load_timeout(10)

driver.get("https://mysterious-shelf-22386.herokuapp.com/")
driver.find_element_by_name("email").send_keys("bcde@gmail.com")
driver.find_element_by_name("psw").send_keys("123456tyrhf")
driver.find_element_by_name("test").send_keys(Keys.ENTER)
#window_after = driver.window_handles[1]
#driver.switch_to.window(window_after)
time.sleep(20)
driver.quit()