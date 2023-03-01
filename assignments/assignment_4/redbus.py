import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.redbus.in/")
driver.implicitly_wait(5)

driver.find_element(By.ID, 'signin-block').click()
driver.find_element(By.ID, 'signInLink').click()

driver.switch_to.frame(driver.find_element(By.XPATH, '//div[@class="modal"]//iframe'))
driver.find_element(By.ID, 'mobileNoInp').send_keys('7898')

print('Error Message :: ', driver.find_element(By.XPATH, '//input[@id="mobileNoInp"]/../span').text)
time.sleep(3)
driver.quit()
