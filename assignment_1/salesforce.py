import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.salesforce.com/in/form/signup/freetrial-sales/")

driver.find_element(By.NAME, 'UserFirstName').send_keys('John')
driver.find_element(By.NAME, 'UserLastName').send_keys('wick')
driver.find_element(By.NAME, 'UserEmail').send_keys('john@gmail.com')
driver.find_element(By.NAME, 'CompanyName').send_keys('eInfo')
Select(driver.find_element(By.NAME, 'UserTitle')).select_by_value('IT_Manager_AP')
Select(driver.find_element(By.NAME, 'CompanyEmployees')).select_by_value('250')
Select(driver.find_element(By.NAME, 'CompanyCountry')).select_by_visible_text('United Kingdom')

# driver.find_element(By.XPATH, "//select[@name='CompanyEmployees']/option[text()='101 - 500 employees']").click()
# driver.find_element(By.XPATH, "//select[@name='CompanyCountry']/option[text()='United Kingdom']").click()

driver.execute_script("arguments[0].click();", driver.find_element(By.ID, 'SubscriptionAgreement'))

driver.find_element(By.NAME, 'start my free trial').click()

# error_message = driver.find_element(By.CSS_SELECTOR, ".phoneInput div span").text
error_message = driver.find_element(By.XPATH, "//div[@class='phoneInput textFieldInput section']/div/span").text

assert error_message == 'Enter a valid phone number'

time.sleep(2)

driver.quit()
