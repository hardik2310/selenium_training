import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(3)
driver.get("https://netbanking.hdfcbank.com/netbanking/IpinResetUsingOTP.htm")

driver.find_element(By.XPATH, "//img[@alt='Go']").click()

actual_alert = driver.switch_to.alert.text
print(actual_alert)
driver.switch_to.alert.accept()

time.sleep(3)
driver.quit()
