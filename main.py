# auto-scroller 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver =webdriver.Chrome()
driver.get("https://logilook.com/content/3-terms-and-conditions-of-use")
driver.maximize_window()

time.sleep(3)

scroll_pause = 0.00000001
scroll_height = 1
scroll_step = 1


last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    for _ in range(0, 1000, scroll_step):
        driver.execute_script(f"window.scrollBy(0, {scroll_height});")
        time.sleep(scroll_pause)
    

    new_height = driver.execute_script("return window.pageYOffset + window.innerHeight;")
    if new_height >= last_height:
        break

driver.quit()