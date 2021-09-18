#!/bin/python3
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import datetime
import random
#********** LOG IN *************
options = Options()
options.add_argument("--user-data-dir=/home/meteor314/.config/google-chrome/Profile 1") #you need to change the profile path (you cand find this on chrome://version/ )
chrome_path = r"/home/meteor314/Desktop/linkedin_bot/chromedriver"
options.page_load_strategy = 'normal'

driver = webdriver.Chrome(chrome_path, options=options)

driver.get('https://www.linkedin.com')
time.sleep(2)


#***************** ADD CONTACTS ***********************

driver.get("https://www.linkedin.com/search/results/people/?network=%5B%22S%22%5D&origin=FACETED_SEARCH&page=10")
time.sleep(2)

all_buttons = driver.find_elements_by_tag_name("button")
connect_buttons = [btn for btn in all_buttons if btn.text == "Connect"]

for btn in connect_buttons:
    driver.execute_script("arguments[0].click();", btn)
    time.sleep(2)
    send = driver.find_element_by_xpath("//button[@aria-label='Send now']")
    driver.execute_script("arguments[0].click();", send)
    close = driver.find_element_by_xpath("//button[@aria-label='Dismiss']")
    driver.execute_script("arguments[0].click();", close)
    time.sleep(2)