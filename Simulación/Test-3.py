#Librerias
from lib2to3.pgen2 import driver
from unicodedata import name
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest

itempag = ["Apple monitor 24"]

class navCategorias_unittest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r'C:\\dChrome\\chromedriver.exe')
    def test_navLaptop(self):
        driver = self.driver
        driver.get ("https://www.demoblaze.com/")
        categoria = driver.find_element_by_xpath("/html/body/div[5]/div/div[1]/div/a[4]")
        categoria.send_keys(Keys.ENTER)
        time.sleep(3)
        categoria = driver.find_element_by_xpath("/html/body/div[5]/div/div[1]/div/a[3]")
        categoria.send_keys(Keys.ENTER)
        time.sleep(3)
        categoria = driver.find_element_by_xpath("/html/body/div[5]/div/div[1]/div/a[2]")
        categoria.send_keys(Keys.ENTER)
        time.sleep(3)
        categoria = driver.find_element_by_xpath("/html/body/div[5]/div/div[2]/div/div[7]/div/div/h4/a")
        categoria.send_keys(Keys.ENTER)
        time.sleep(3)
        textprecio = driver.find_element_by_class_name('price-container')
        print(textprecio.text)
        time.sleep(3)
    def tearDown(self) -> None:
        self.driver.close()
if __name__ == '__main__':
    unittest.main()