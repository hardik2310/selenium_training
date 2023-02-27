import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.facebook.com/login/")
print(driver.title)

ele = driver.find_element(By.ID, 'email')
ele.send_keys('abcdd')

ele_pass = driver.find_element(By.ID, 'pass')
ele_pass.send_keys('password')

login_button = driver.find_element(By.ID, 'loginbutton')
login_button.click()

time.sleep(3)

driver.quit()
