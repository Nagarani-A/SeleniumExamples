from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

import time

s = Service("C:\\Users\\nagua\\PycharmProjects\\SeleniumExamples\\drivers\\chromedriver")
driver = webdriver.Chrome(service=s)

driver.get("https://jqueryui.com/draggable/")
driver.maximize_window()

# or

fr = driver.find_element(By.CLASS_NAME, "demo-frame")
driver.switch_to.frame(fr)

obj = driver.find_element(By.ID, "draggable")
# offset if we dont know the vaue for x n y
ActionChains(driver).drag_and_drop_by_offset(obj,80,80).perform()

# perform used to do operation on browser
time.sleep(3)
driver.quit()
