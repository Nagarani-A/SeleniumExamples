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

driver.execute_script("window.location='https://www.bing.com/'")
driver.execute_script("document.getElementById('sb_form_q').value='Rani'")
driver.execute_script("document.getElementById('sb_form_go').click();")

driver.quit()