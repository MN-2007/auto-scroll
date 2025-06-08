# auto-scroller 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver =webdriver.Chrome()
driver.get("https://edition.cnn.com/")
driver.maximize_window()

scroll_pause = 0.1
scroll_height = 500
scroll_step = 10


last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    for _ in range(0, 1000, scroll_step):
        driver.execute_script(f"window.scrollBy(0, {scroll_height});")
        time.sleep(scroll_pause)
    
    time.sleep(1)

    new_height = driver.execute_script("return window.pageYOffset + window.innerHeight;")
    if new_height >= last_height:
        break

driver.quit()