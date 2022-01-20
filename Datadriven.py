
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import xlutils
from selenium import webdriver

import time

s = Service("C:\\Users\\nagua\\PycharmProjects\\SeleniumExamples\\drivers\\chromedriver")
driver = webdriver.Chrome(service=s)
driver.maximize_window()
driver.implicitly_wait(10)

driver.get("https://demo.guru99.com/selenium/newtours/index.php")


path="C:/Users/nagua/Desktop/SEwithPY/Testing.xlsx"

rows = xlutils.getrowcount(path,'Sheet1')

for r in range (2,rows+1):
    username=xlutils.readData(path,'Sheet1',r,1)
    password = xlutils.readData(path, 'Sheet1', r, 2)

    driver.find_elements(By.NAME,"userName").send_keys(username)
    driver.find_elements(By.NAME, "password").send_keys(password)

    if driver.title=="Find a flight: Mercury Tours":
        print("Test Passed")
        xlutils.writedata(path,'Sheet1',r,3,'Test Passed')
    else:
        print("Test Failed")
        xlutils.writedata(path, 'Sheet1', r, 3, 'Test Failed')

        driver.find_elements(By.LINK_TEXT,"Home").click()


