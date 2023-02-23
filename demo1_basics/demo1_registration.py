import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(3)

driver.get("https://www.facebook.com/")
print(driver.title)

driver.find_element(By.LINK_TEXT, "Create new account").click()

driver.find_element(By.NAME, "firstname",).send_keys("John")
driver.find_element(By.NAME, "lastname").send_keys("dina")
driver.find_element(By.ID, "password_step_input").send_keys("welcome123")
driver.find_element(By.XPATH, "//input[@name='sex']").click()
driver.find_element(By.NAME, "websubmit").click()

time.sleep(3)

driver.quit()
