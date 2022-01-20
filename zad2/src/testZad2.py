import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class MyTestCase(unittest.TestCase):
    def test_title(self):
        driver = webdriver.Chrome(executable_path='C:/Users/48531/OneDrive/Pulpit/Testowanie/laboratorium-15-Meruszka/zad2/driver/chromedriver.exe')
        driver.get("https://www.google.com/")
        driver.find_element_by_class_name("gLFyf gsfi").send_keys('Kotki')
        driver.find_element_by_id("search_button_homepage").submit()
        self.assertEqual(driver.title, "Selenium at DuckDuckGo")
        driver.quit()

