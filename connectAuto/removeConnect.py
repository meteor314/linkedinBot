#!/bin/python3
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import numpy as np
from selenium.common.exceptions import InvalidSessionIdException
options = Options()
#options.add_argument('--profile-directory=Profile 1')
options.add_argument("--user-data-dir=/home/kali/.config/google-chrome/Profile 1") #you need to change the profile path (you cand find this on chrome://version/ )
chrome_path = r"./chromedriver"
options.page_load_strategy = 'normal'

driver = webdriver.Chrome(chrome_path, options=options)

driver.get('https://linkedin.com')


cookie = driver.get_cookie("spectroscopyId") #if we have this cookies that means user s are already connected !
if(not cookie): #void
    driver.execute_script("alert('Please connect and restart the program')");
    #print(len(cookies))
    driver.get('https://www.linkedin.com/login/fr?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin')
    driver.sleep(60)

else:
    driver.get('https://www.linkedin.com/mynetwork/invitation-manager/sent/')
    driver.maximize_window()
    time.sleep(3)


"""
###################### use cookies to know if the user is alreday connected or not. 
split cookies  :
let arrayCookies = [];
const getCookies = document.cookie;
for (i = 0; i <= getCookies.length ;i++) {
	arrayCookies = getCookies.split(";") 
}
console.log(arrayCookies)
-------------------------- Not connected -----

[
  "JSESSIONID=ajax:3689318932468671733",
  " lang=v=2&lang=fr-fr",
  " bcookie=\"v=2&93a707d6-7b34-49ba-8077-8c088e7da7bb\"",
  " li_gc=********/i75YQnuGvt1rdom7qrucMPnuqK+ghFxUKKu4cvoA=",
  " lidc=\"b=VGST04:s=V:r=V:a=V:p=V:g=2470:u=1:x=1:i=1633007520:t=1633093920:v=2:sig=AQGCYQwKbqrnnkBDODoPmopS2iebf501\"",
  " li_alerts=e30=",
  " G_ENABLED_IDPS=google"
]

-------Connected ---------------

[
    "bcookie=\"v=2&fa1db627-41b0-4282-82d7-d058116b6872\"",
    " li_alerts=e30=",
    " G_ENABLED_IDPS=google",
    " li_gc=MTsyMTsxNjMyODE2************I7MDIxVsbYSDtOTDk/MwXIQlEkBJMPapptJaau6ghClkAfmuI=",
    " liap=true",
    " JSESSIONID=\"ajax:2658083966840652003\"",
    " timezone=Europe/Paris",
    " lidc=\"b=OB77:s=O:r=O:a=O:p=O:g=2446:u=16:x=1:i=1633005688:t=1633047774:v=2:sig=AQHxu9ur9ru4DoHDF7YPVogUV-6dd2xD\"",
    " lang=v=2&lang=en-us",
    " spectroscopyId=*-cfa9-4b84-920b-*",
    " li_mc=***************************="
]


connectedArray = [
    "bcookie=\"v=2&fa1db627-41b0-4282-82d7-d058116b6872\"",
    " li_alerts=e30=",
    " G_ENABLED_IDPS=google",
    " li_gc=MTsyMTsxNjMyODE2************I7MDIxVsbYSDtOTDk/MwXIQlEkBJMPapptJaau6ghClkAfmuI=",
    " liap=true",
    " JSESSIONID=\"ajax:2658083966840652003\"",
    " timezone=Europe/Paris",
    " lidc=\"b=OB77:s=O:r=O:a=O:p=O:g=2446:u=16:x=1:i=1633005688:t=1633047774:v=2:sig=AQHxu9ur9ru4DoHDF7YPVogUV-6dd2xD\"",
    " lang=v=2&lang=en-us",
    " spectroscopyId=*-cfa9-4b84-920b-*",
    " li_mc=***************************="
]
notConnectedAray  = [
  "JSESSIONID=ajax:3689318932468671733",
  " lang=v=2&lang=fr-fr",
  " bcookie=\"v=2&93a707d6-7b34-49ba-8077-8c088e7da7bb\"",
  " li_gc=********/i75YQnuGvt1rdom7qrucMPnuqK+ghFxUKKu4cvoA=",
  " lidc=\"b=VGST04:s=V:r=V:a=V:p=V:g=2470:u=1:x=1:i=1633007520:t=1633093920:v=2:sig=AQGCYQwKbqrnnkBDODoPmopS2iebf501\"",
  " li_alerts=e30=",
  " G_ENABLED_IDPS=google"
]

print(np.array_equal(connectedArray,notConnectedAray))
"""
print(cookie)



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

