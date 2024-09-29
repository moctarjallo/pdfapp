from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import time

driver = webdriver.Chrome()
driver.get("https://developers.facebook.com/apps/878666903782206/whatsapp-business/wa-dev-console/?business_id=1620644888498053")

# assert "Python" in driver.title
elem = driver.find_element(By.ID, "email")
elem.send_keys("moctarjallo@gmail.com")

elem = driver.find_element(By.ID, "pass")
elem.send_keys("Dj1nk@n!")

elem.send_keys(Keys.RETURN)

elem = driver.find_element(By.ID, "js_4d")
elem.click()

time.sleep(60)
# elem.clear()
# assert "No results found." not in driver.page_source
driver.close()

