from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

s = Service("C:\\Users\\nagua\\PycharmProjects\\SeleniumExamples\\drivers\\chromedriver")
driver = webdriver.Chrome(service=s)
driver.maximize_window()

driver.get("https://www.bing.com/account/general?ru=https%3a%2f%2fwww.bing.com%2f&FORM=O2HV46&sh=0")


p1=driver.find_element(By.ID, "hp_ap_none").click()

p1=driver.find_element(By.ID, "hp_ap_none").is_selected()
print(p1)


time.sleep(5)
driver.quit()

