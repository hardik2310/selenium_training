from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://www.google.com/")

action = webdriver.ActionChains(driver)

action.key_down(webdriver.Keys.SHIFT).pause(1) \
    .send_keys("Hello world").key_up(webdriver.Keys.SHIFT).pause(1) \
    .send_keys(webdriver.Keys.ARROW_DOWN).send_keys(webdriver.Keys.ARROW_DOWN) \
    .send_keys(webdriver.Keys.ARROW_DOWN).pause(1).send_keys(webdriver.Keys.ENTER).perform()

time.sleep(5)
driver.quit()
