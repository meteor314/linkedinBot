#!/bin/python3
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.common.exceptions import InvalidSessionIdException
options = Options()
#options.add_argument('--profile-directory=Profile 1')
options.add_argument("--user-data-dir=/home/kali/.config/google-chrome/Profile 1") #you need to change the profile path (you cand find this on chrome://version/ )
chrome_path = r"./chromedriver"
options.page_load_strategy = 'normal'

driver = webdriver.Chrome(chrome_path, options=options)

driver.get('https://www.linkedin.com/mynetwork/invitation-manager/sent/')
driver.maximize_window()
time.sleep(3)

all_buttons = driver.find_elements_by_tag_name("button")
connect_buttons = [btn for btn in all_buttons if btn.text == "Withdraw"]
for btn in connect_buttons:
    time.sleep(1)
    try:
        driver.execute_script("arguments[0].click();", btn)
        time.sleep(1)
        send = driver.find_element_by_class_name("artdeco-button--primary")
        driver.execute_script("arguments[0].click();", send)
        time.sleep(1)

    except Exception as e:
        print(e)

js = 'window.scrollTo(0, document.documentElement.scrollHeight)'  # scroll to the bottom of the page.
driver.execute_script(js)
"""
btnNext = driver.find_element_by_xpath("//button[@aria-label='Next']")
driver.execute_script("arguments[0].click();", btnNext)

"""

