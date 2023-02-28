import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(3)
driver.get("https://nasscom.in/")

action = webdriver.ActionChains(driver)

action.move_to_element(driver.find_element(By.LINK_TEXT, 'Membership')).perform()
driver.find_element(By.LINK_TEXT, 'Members Listing').click()

action.move_to_element(driver.find_element(By.LINK_TEXT, 'Membership'))\
    .move_to_element(driver.find_element(By.XPATH, "//a[text()='Become a Member']")).perform()

driver.find_element(By.LINK_TEXT, "Membership Benefits").click()

time.sleep(3)
driver.quit()
