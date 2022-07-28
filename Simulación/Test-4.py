from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome(
    executable_path='C:/chromedriver/chromedriver.exe')

browser.get('https://www.demoblaze.com/')

singup = browser.find_element(By.ID,'login2')
singup.click()

input_nombre = browser.find_element(By.ID,'loginusername')
input_nombre.send_keys('test:)')
input_password = browser.find_element(By.ID,'loginpassword')
input_password.send_keys('1234')

content = browser.find_element(By.XPATH,'/html/body/div[3]/div/div/div[3]/button[2]')
content.send_keys(Keys.ENTER)