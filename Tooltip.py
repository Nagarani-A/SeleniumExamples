from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

import time

s = Service("C:\\Users\\nagua\\PycharmProjects\\SeleniumExamples\\drivers\\chromedriver")
driver = webdriver.Chrome(service=s)

driver.get("https://jqueryui.com/tooltip/")
driver.maximize_window()

# or

fr = driver.find_element(By.CLASS_NAME, "demo-frame")
driver.switch_to.frame(fr)

obj = driver.find_element(By.ID,"age")
p1=obj.get_attribute("title")
print("Tooltip message is :", p1)


# perform used to do operation on browser
time.sleep(3)
driver.quit()
