import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://github.com/login")

driver.find_element(By.ID, 'login_field').send_keys('hello')
driver.find_element(By.ID, 'password').send_keys('89hello')
driver.find_element(By.CLASS_NAME, 'js-sign-in-button').click()

time.sleep(3)

driver.quit()
