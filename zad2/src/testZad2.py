import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class MyTestCase(unittest.TestCase):
    def test_title(self):
        driver = webdriver.Chrome(executable_path='C:/Users/48531/OneDrive/Pulpit/Testowanie/laboratorium-15-Meruszka/zad2/driver/chromedriver.exe')
        driver.get("https://www.duckduckgo.com/")
        driver.implicitly_wait(10)
        try:
            driver.find_element(by='id',value="search_form_input_homepage").send_keys('Kotki')
            driver.find_element(by='id', value="search_button_homepage").submit()
            links = driver.find_element(by='id', value="links")
            driver.implicitly_wait(10)
            tab = links.find_elements(by='tag name', value='a')
            driver.implicitly_wait(10)
            print(tab[0].get_attribute('href'))
            print(tab[2].get_attribute('href'))
        except:
            print("Coś poszło nie tak")
        driver.quit()

MyTestCase().test_title()