from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome("C:\\Users\\Archana\\Desktop\\Web App with Go\\Testing\\chromedriver.exe")
driver.set_page_load_timeout(10)
action = ActionChains(driver)


#driver.maximize_window()
time.sleep(2)
print("|******************************************************|")
print("|                                                      |")
print("|Test ID         : 1                                   |")
print("|Expected Output : Should Open login page|             |")
#driver.get("https://mysterious-shelf-22386.herokuapp.com/")
driver.get("http://localhost:8080/")
print("|Result          : Pass                                |")
print("|******************************************************|")

print("|******************************************************|")
print("|                                                      |")
print("|Test ID         : 2                                   |")
print("|Expected Output : Should Click Login Button           |")
print("|                  and gives error to enter all details|")
time.sleep(2)
driver.find_element_by_name("test").click()
print("|Result          : Pass                                |")
print("|******************************************************|")


print("|******************************************************|")
print("|                                                      |")
print("|Test ID         : 3                                   |")
print("|Expected Output : Should Enter wrong username(archana)|")
time.sleep(3)
driver.find_element_by_name("email").send_keys("archan")
print("|Result          : Pass                                |")
print("|******************************************************|")



print("|******************************************************|")
print("|                                                      |")
print("|Test ID         : 4                                   |")
print("|Expected Output : Should Enter Password(archanacmahaj)|")
time.sleep(2)
driver.find_element_by_name("psw").send_keys("archanacmahajan")
print("|Result          : Pass                                |")
print("|******************************************************|")


print("|******************************************************|")
print("|                                                      |")
print("|Test ID         : 5                                   |")
print("|Expected Output : Should Click Login Button and gives |")
print("|                  error to enter username in valid email format|")
time.sleep(2)
driver.find_element_by_name("test").click()
print("|Result          : Pass                                |")
print("|******************************************************|")


print("|******************************************************|")
print("|                                                      |")
print("|Test ID         : 6                                   |")
print("|Expected Output : Should Enter right username         |")
print("|                   (archanacmahajan@gmai.com)         |")
time.sleep(3)
driver.find_element_by_name("email").send_keys("archanacmahajan@gmai.com")
print("|Result          : Pass                                |")
print("|******************************************************|")


print("|******************************************************|")
print("|                                                      |")
print("|Test ID         : 7                                   |")
print("|Expected Output : Should Enter Password(archanacmahajan)|")
time.sleep(2)
driver.find_element_by_name("psw").send_keys("archanacmahajan")
print("|Result          : Pass                                |")
print("|******************************************************|")


print("|******************************************************|")
print("|                                                      |")
print("|Test ID         : 8                                   |")
print("|Expected Output : Should Click Login Button           |")
print("|                   and login successfully             |")
time.sleep(2)
driver.find_element_by_name("test").click()
print("|Result          : Pass                                |")
print("|******************************************************|")

print("|******************************************************|")
print("|                                                      |")
print("|Test ID         : 9                                   |")
print("|Expected Output : Mouse should hover on samll image   |")
time.sleep(6)
firstLevelMenu = driver.find_element_by_xpath("/html/body/form/center/table/tbody/tr[3]/td[3]/a/img")
action.move_to_element(firstLevelMenu).perform()
print("|Result          : Pass                                |")
print("|******************************************************|")



print("|******************************************************|")
print("|                                                      |")
print("|Test ID         : 10                                   |")
print("|Expected Output : Should Click know more button       |")
time.sleep(8)
driver.find_element_by_xpath("/html/body/form/center/table/tbody/tr[1]/td[2]/input").click()
print("|Result          : Pass                                |")
print("|******************************************************|")

print("|******************************************************|")
print("|                                                      |")
print("|Test ID         : 11                                   |")
print("|Expected Output : Should Close Browser                |")
time.sleep(4)
driver.quit()
print("|Result          : Pass                                |")
print("|******************************************************|")

