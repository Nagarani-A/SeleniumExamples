import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

s = Service("C:\\Users\\nagua\\PycharmProjects\\SeleniumExamples\\drivers\\chromedriver")
driver = webdriver.Chrome(service=s)

'''from selenium import webdriver

#driver = webdriver.Chrome(executable_path="C:/Drivers/chromedriver_win32/chromedriver.exe")

driver = webdriver.Chrome(executable_path="Drivers/chromedriver.exe")'''

driver.get("http://selenium.dev/")



