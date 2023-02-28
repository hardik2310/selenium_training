import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)

driver.get("https://www.medibuddy.in")

driver.find_element(By.LINK_TEXT, 'Login').click()
driver.find_element(By.XPATH, "//div[@class='coperate']").click()
time.sleep(2)
driver.find_element(By.XPATH, "//div[@class='coperate']").click()

driver.find_element(By.NAME, 'userName').send_keys('john')
driver.find_element(By.XPATH, "//div[@class='submitbtn']/button").click()
driver.find_element(By.NAME, 'password').send_keys('John123')

driver.find_element(By.XPATH, '//label[@class="showpass"]/input').click()
driver.find_element(By.XPATH, "//button[@type='submit']").click()

error_message = driver.find_element(By.XPATH, "//div[@class='alert alert-danger errorTxt']").text
time.sleep(2)
print("Error Message for login: ", error_message)

time.sleep(5)
driver.quit()
