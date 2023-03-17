from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://netbanking.hdfcbank.com/netbanking/IpinResetUsingOTP.htm")
driver.find_element(By.XPATH, "//img[@alt='Go']").send_keys(r"pathoffile")

time.sleep(5)
driver.quit()
