from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)

driver.get("https://www.royalcaribbean.com/")

popup_dialogue = driver.find_elements(By.XPATH, "//div[contains(@class,'notification-banner__close')]")
if len(popup_dialogue) > 0:
    popup_dialogue[0].click()

driver.find_element(By.ID, "rciHeaderSignIn").click()
# driver.find_element(By.LINK_TEXT, "Create an account").click()
driver.execute_script('arguments[0].click()', driver.find_element(By.LINK_TEXT, "Create an account"))

driver.find_element(By.XPATH, '//*[@data-placeholder="First name/Given name"]').send_keys("Dennis")
driver.find_element(By.XPATH, '//*[@data-placeholder="Last name/Surname"]').send_keys("Rich")

driver.find_element(By.XPATH, '//span[normalize-space(text())="Month"]').click()
driver.find_element(By.XPATH, "//span[contains(text(),'April')]").click()

driver.find_element(By.XPATH, '//span[normalize-space(text())="Day"]').click()
driver.find_element(By.XPATH, '//span[contains(text(),\'4\')]').click()

driver.find_element(By.XPATH, '//*[@data-placeholder="Year"]').send_keys("1990")

driver.find_element(By.XPATH, '//div/span[contains(text(),"Country/Region of residence")]').click()
driver.find_element(By.XPATH, '//span[normalize-space(text())="India"]').click()

driver.find_element(By.XPATH, '//*[@data-placeholder="Email address"]').send_keys("hardik.gosai@gmail.com")
driver.find_element(By.XPATH, '//*[@data-placeholder="Create new password"]').send_keys("Xyz@123456")

driver.find_element(By.XPATH, '//div/span[contains(text(),"Select one security question")]').click()
driver.find_element(By.XPATH, '//span[contains(text(),"What was your first car\'s make or model?")]').click()
driver.find_element(By.XPATH, '//*[@data-placeholder="Answer"]').send_keys("Maruti Alto")

driver.find_element(By.XPATH, '//div[@id="agreements"]/../mat-checkbox').click()

driver.find_element(By.XPATH, '//button[contains(text(), \'Done\')]').click()

time.sleep(3)
driver.quit()
