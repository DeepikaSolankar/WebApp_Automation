from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
driver = webdriver.Chrome("C:\Users\DEEPIKA\PycharmProjects\FirstSeleniumTest\Drivers\chromedriver.exe")
action = ActionChains(driver)
time.sleep(1)
driver.maximize_window()
main = driver.get('http://www.amazon.in')
time.sleep(1)

driver.maximize_window()

# For Sign in
firstLevelMenu = driver.find_element_by_xpath('//*[@id="nav-link-accountList"]/span')
action.move_to_element(firstLevelMenu).perform()
time.sleep(1)

secondLevelMenu = driver.find_element_by_xpath('//*[@id="nav-flyout-ya-signin"]/a/span')
secondLevelMenu.click()
time.sleep(3)

signinelement = driver.find_element_by_id('ap_email')
signinelement.send_keys("8308930637")
time.sleep(1)

cont = driver.find_element_by_xpath('//*[@id="continue"]')
cont.click()
time.sleep(1)

passwordelement = driver.find_element_by_xpath('//*[@id="ap_password"]')
passwordelement.send_keys("Deepika@10")
time.sleep(1)

login = driver.find_element_by_xpath('//*[@id="signInSubmit"]')
login.click()
time.sleep(8)

# For Search Box
search1 = driver.find_element_by_xpath('//*[@id="twotabsearchtextbox"]')
search1.send_keys("pencil")
time.sleep(1)

# For Search Button
sr = driver.find_element_by_xpath('//*[@id="nav-search"]/form/div[2]/div/input')
sr.click()
time.sleep(4)

# For finding item
it1 = driver.find_element_by_xpath('//*[@id="search"]/div[1]/div[2]/div/span[3]/div[2]/div[3]/div/span/div/div/div[2]/h2/a/span')
driver.execute_script("arguments[0].scrollIntoView();", it1)
driver.execute_script("(arguments[0]).click();", it1)
time.sleep(5)

window_after = driver.window_handles[1]
driver.switch_to.window(window_after)

# For WishList
w1 = driver.find_element_by_xpath('//*[@id="add-to-wishlist-button-submit"]')
w1.click()
time.sleep(5)

#For View List
wish = driver.find_element_by_xpath('//*[@id="WLHUC_viewlist"]/span/span')
wish.click()
time.sleep(5)

#For add to cart
cart = driver.find_element_by_xpath('//*[@id="pab-ID801CSFN7JPU"]/span/a')
cart.click()
time.sleep(5)


#For View Cart
view= driver.find_element_by_xpath('//*[@id="nav-cart"]')
view.click()
time.sleep(5)

#Press amazon.in Button
ama=driver.find_element_by_xpath('//*[@id="nav-logo"]/a/span[1]')
ama.click()
time.sleep(5)

driver.quit()
