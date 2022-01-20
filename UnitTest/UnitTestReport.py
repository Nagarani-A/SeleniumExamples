import unittest
import HTMLTestRunner
from selenium.webdriver import ActionChains
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

import time


class MyTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        s = Service("C:\\Users\\nagua\\PycharmProjects\\SeleniumExamples\\drivers\\chromedriver")
        cls.driver = webdriver.Chrome(service=s)
        cls.driver.get("http://demo.automationtesting.in/Windows.html")
        cls.driver.maximize_window()
        time.sleep(5)


    def test_multiple(self):
        self.driver.find_element(By.XPATH, "//*[@id='Tabbed']/a/button").click()

        time.sleep(5)

    @classmethod
    def tearDownClass(cls):
        time.sleep(5)
        cls.driver.quit()




if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner())

