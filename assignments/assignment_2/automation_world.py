import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)

driver.get("https://www.automationworld.com")
time.sleep(5)
driver.find_element(By.XPATH, "//div[@class='close-olytics-image-bottom-middarkblue']").click()
driver.find_element(By.LINK_TEXT, "Subscribe").click()

driver.switch_to.window(driver.window_handles[1])

driver.find_element(By.ID, "id24_344").click()

driver.find_element(By.ID, "id1").send_keys("Hardik")
driver.find_element(By.ID, "id2").send_keys("Gosai")
driver.find_element(By.ID, "id10").send_keys("Engineerr")
driver.find_element(By.ID, "id195").send_keys("www.Einfo.com")
driver.find_element(By.ID, "id3").send_keys("Einfo")
driver.find_element(By.ID, "id11").send_keys("123456789")
Select(driver.find_element(By.ID, "id7")).select_by_value('189')
driver.find_element(By.ID, "id6").send_keys("chennai")

driver.find_element(By.XPATH, "//input[@value='Submit']").click()

error_message = driver.find_element(By.XPATH, "//li[normalize-space()='Email Address is required.']").text
print("Error Message: ", error_message)

time.sleep(3)
driver.quit()
