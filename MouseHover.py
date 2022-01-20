
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

driver.get("https://www.w3schools.com/html/")

# p1=driver.find_elements(By.TAG_NAME, "q")

driver.find_element(By.XPATH, "//*[@id='navbtn_exercises']").click()
p1 = driver.find_elements(By.XPATH, "//*[@id='nav_exercises']/div/div/div[3]/h3/a")
ActionChains(driver).move_to_element(p1).perform()

time.sleep(3)
driver.quit()
