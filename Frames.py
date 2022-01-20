from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

s = Service("C:\\Users\\nagua\\PycharmProjects\\SeleniumExamples\\drivers\\chromedriver")
driver = webdriver.Chrome(service=s)


driver.get("https://jqueryui.com/datepicker/")
driver.maximize_window()




fr=driver.find_element(By.CLASS_NAME,"demo-frame")
driver.switch_to.frame(fr)
driver.find_element(By.ID,"datepicker").click()

#To comeback browser
# driver.switch_to.default_content()

time.sleep(3)
driver.quit()
