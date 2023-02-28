from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.select import Select


driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://www.online.citibank.co.in/")

driver.find_element(By.CLASS_NAME, "fancybox-close").click()
driver.find_element(By.CLASS_NAME, "txtSign").click()

driver.switch_to.window(driver.window_handles[1])

driver.find_element(By.XPATH, "//div[contains(text(),'Forgot User ID?')]").click()

driver.find_element(By.XPATH, "//a[@class='sbToggle']").click()
driver.find_element(By.XPATH, "//a[@rel='Credit Card']").click()
driver.find_element(By.ID, "citiCard1").send_keys("4545")
driver.find_element(By.ID, "citiCard2").send_keys("5656")
driver.find_element(By.ID, "citiCard3").send_keys("8887")
driver.find_element(By.ID, "citiCard4").send_keys("9998")
driver.find_element(By.ID, "cvvnumber").send_keys("123")

# driver.execute_script("document.querySelector('#bill-date-long').value='23/02/2023'")
driver.find_element(By.ID, "bill-date-long").click()
Select(driver.find_element(By.CLASS_NAME, "ui-datepicker-year")).select_by_value('2022')
Select(driver.find_element(By.CLASS_NAME, "ui-datepicker-month")).select_by_visible_text('Apr')
driver.find_element(By.LINK_TEXT, "14").click()

driver.find_element(By.XPATH, "//input[@value='PROCEED']").click()

error_message = driver.find_element(By.CLASS_NAME, "ui-dialog-content").text
print("Error Message: ", error_message)

time.sleep(3)
driver.quit()
