from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

browser = webdriver.Chrome(
    executable_path='C:/chromedriver/chromedriver.exe')

browser.get('https://www.demoblaze.com/index.html')

time.sleep(3)

browser.get('https://www.demoblaze.com/prod.html?idp_=1')

time.sleep(3)

browser.get('https://www.demoblaze.com/prod.html?idp_=2')

time.sleep(3)

browser.get('https://www.demoblaze.com/prod.html?idp_=3')

time.sleep(3)

browser.get('https://www.demoblaze.com/prod.html?idp_=4')

time.sleep(3)

browser.get('https://www.demoblaze.com/prod.html?idp_=5')

time.sleep(3)
