# auto-scroller 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver =webdriver.Chrome()
driver.get("https://edition.cnn.com/")
driver.maximize_window()

scroll_pause_time = 1
scroll_height = 1000

driver.quit()