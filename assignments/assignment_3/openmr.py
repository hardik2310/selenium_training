from datetime import date

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("http://demo.openemr.io/b/openemr/")

driver.find_element(By.ID, 'authUser').send_keys('admin')
driver.find_element(By.ID, 'clearPass').send_keys('pass')
Select(driver.find_element(By.XPATH, '//select[@name=\'languageChoice\']')).select_by_visible_text('English (Indian)')
driver.find_element(By.ID, 'login-button').click()

action = webdriver.ActionChains(driver)

driver.find_element(By.XPATH, '//div[normalize-space()=\'Patient\']').click()
driver.find_element(By.XPATH, '//div[normalize-space()=\'New/Search\']').click()

driver.switch_to.frame(driver.find_element(By.XPATH, '//*[@id="framesDisplay"]/div[3]/iframe'))
driver.find_element(By.ID, 'form_fname').send_keys('John')
driver.find_element(By.ID, 'form_lname').send_keys('Dev')
driver.find_element(By.ID, 'form_DOB').send_keys(str(date.today()))
Select(driver.find_element(By.ID, 'form_sex')).select_by_visible_text('Male')
driver.find_element(By.ID, 'create').click()

driver.switch_to.default_content()

driver.switch_to.frame(driver.find_element(By.XPATH, "//iframe[@id='modalframe']"))
driver.find_element(By.XPATH, "//input[@value='Confirm Create New Patient']").click()

driver.switch_to.default_content()

wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.alert_is_present())

actual_alert = driver.switch_to.alert.text
print('Alert Text :: ', actual_alert)
driver.switch_to.alert.accept()

time.sleep(3)

driver.find_element(By.XPATH, '//div[@class=\'closeDlgIframe\']').click()

patient_name = driver.find_element(By.XPATH, '//*[@id="attendantData"]//a/span').text
print('\n\nPatient Name :: ', patient_name)

driver.switch_to.frame(driver.find_element(By.XPATH, "//iframe[@name='pat']"))

print('\n\nPatient Name At Another Place :: ', driver.find_element(By.XPATH, "//h2[contains(text(),'Medical Record Dashboard')]").text)

time.sleep(3)
driver.quit()
