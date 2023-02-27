import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(3)
driver.get("https://netbanking.hdfcbank.com/netbanking/")


driver.switch_to.frame(driver.find_element(By.NAME, 'login_page'))
driver.find_element(By.NAME, 'fldLoginUserId').send_keys('john')
driver.find_element(By.LINK_TEXT, "CONTINUE").click()
driver.switch_to.default_content()

time.sleep(3)
driver.quit()
