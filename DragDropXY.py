from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

import time

s = Service("C:\\Users\\nagua\\PycharmProjects\\SeleniumExamples\\drivers\\chromedriver")
driver = webdriver.Chrome(service=s)
driver.maximize_window()
driver.get("https://jqueryui.com/draggable/")


# or

fr = driver.find_element(By.CLASS_NAME, "demo-frame")
driver.switch_to.frame(fr)

obj = driver.find_element(By.ID, "draggable")

s=obj.size  #height and width
l=obj.location #x and y

print(obj.get_attribute("class"))  #what is specified in class description
print(s)
print(l)


# perform used to do operation on browser
time.sleep(3)
driver.quit()
