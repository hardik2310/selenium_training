import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Edge()
driver.maximize_window()
driver.implicitly_wait(5)

driver.get("https://www.oracle.com/in/database/")

driver.find_element(By.ID, 'acctBtnLabel').click()
driver.find_element(By.LINK_TEXT, 'Sign-In').click()

# Not Working from here
print(driver.title + '\n' + driver.current_url + '\n' + driver.find_element(By.XPATH, '//h2').text)

driver.find_element(By.ID, "sso_username").send_keys('John')
driver.find_element(By.ID, "ssopassword").send_keys("John@123")
driver.find_element(By.ID, "signin_button").click()

time.sleep(3)

error_message = driver.find_element(By.XPATH, "//div[contains(text(),'Invalid')]").text
print(error_message)

time.sleep(3)
driver.quit()
