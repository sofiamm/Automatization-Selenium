from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome('/Users/sofiamora/chromedriver/chromedriver')
browser.get('https://www.demoblaze.com/index.html')

browser.implicitly_wait(20)
browser.get('https://www.demoblaze.com/prod.html?idp_=1')

product_btn = browser.find_element(By.CSS_SELECTOR, 'a.btn-success')
product_btn.click()

WebDriverWait(browser, 10).until(EC.alert_is_present())
browser.switch_to.alert.accept()

browser.get('https://www.demoblaze.com/cart.html')