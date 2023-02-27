import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(3)

driver.get("https://www.db4free.net/")
driver.find_element(By.PARTIAL_LINK_TEXT, 'phpMyAdmin').click()

driver.switch_to.window(driver.window_handles[1])

driver.find_element(By.ID, "input_username").send_keys('abcd')
driver.find_element(By.ID, "input_password").send_keys("welcome@123")
driver.find_element(By.ID, "input_go").click()

time.sleep(5)
driver.close()
driver.quit()
