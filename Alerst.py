from selenium.webdriver import Keys, ActionChains
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

import time

s = Service("C:\\Users\\nagua\\PycharmProjects\\SeleniumExamples\\drivers\\chromedriver")
driver = webdriver.Chrome(service=s)
driver.maximize_window()
driver.implicitly_wait(10)

driver.get("http://testautomationpractice.blogspot.com/")

driver.find_element(By.XPATH,"//*[@id='HTML9']/div[1]/button").click()

#OK
driver.switch_to.alert.accept()

#cancel
#driver.switch_to.alert().dismiss()

time.sleep(5)
driver.quit()
