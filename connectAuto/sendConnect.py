#!/bin/python3
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.common.exceptions import InvalidSessionIdException

options = Options()
options.add_argument("--user-data-dir=/home/kali/.config/google-chrome/Profile 1") #you need to change the profile path (you cand find this on chrome://version/ )
chrome_path = r"./chromedriver"
options.page_load_strategy = 'normal'

driver = webdriver.Chrome(chrome_path, chrome_options=options)

driver.get('https://www.linkedin.com')
time.sleep(2)



driver.get("https://www.linkedin.com/search/results/people/?network=%5B%22S%22%5D&origin=FACETED_SEARCH&page=3")
time.sleep(2)

all_buttons = driver.find_elements_by_tag_name("button")
i = 0
lists_url = []
while i <= 100 :
    link = "https://www.linkedin.com/search/results/people/?network=%5B%22S%22%5D&origin=FACETED_SEARCH" \
           "&page=" + str(i)
    lists_url.append(link)
    i = i +1
#print(lists_url)
try :
    for list_url in lists_url[2:] :
        time.sleep(3)
        try :
            connect_buttons = [btn for btn in all_buttons if btn.text == "Connect"]
            for btn in connect_buttons:
                time.sleep(1)
                try:
                    driver.execute_script("arguments[0].click();", btn)
                    time.sleep(2)
                    send = driver.find_element_by_xpath("//button[@aria-label='Send now']")
                    driver.execute_script("arguments[0].click();", send)
                    close = driver.find_element_by_xpath("//button[@aria-label='Dismiss']")
                    driver.execute_script("arguments[0].click();", close)
                    time.sleep(1)

                except Exception as e:
                    print(e)

            js = 'window.scrollTo(0, document.documentElement.scrollHeight)'  # scroll to the bottom of the page.
            driver.execute_script(js)
            btnNext = driver.find_element_by_xpath("//button[@aria-label='Next']")
            driver.execute_script("arguments[0].click();", btnNext)

            """print(list_url)
            driver.execute_script('window.open("{}", "_blank");'.format(list_url))
            time.sleep(5)
            driver.switch_to.window(driver.window_handles[-1])  # switch to the tab recently open """
            #driver.close()
            time.sleep(7)
            #driver.get(lists_url)

        except Exception as e :
            print(e)
        time.sleep(3)


except Exception as e :
    print(e)