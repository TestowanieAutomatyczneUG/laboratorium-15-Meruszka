import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class MyTestCase(unittest.TestCase):
    def test_title(self):
        driver = webdriver.Chrome(executable_path='C:/Users/48531/OneDrive/Pulpit/Testowanie/laboratorium-15-Meruszka/zad1/driver/chromedriver.exe')
        driver.get("https://duckduckgo.com/")
        driver.find_element_by_id("search_form_input_homepage").send_keys("Selenium")
        driver.find_element_by_id("search_button_homepage").submit()
        self.assertEqual(driver.title, "Selenium at DuckDuckGo")
        driver.quit()

