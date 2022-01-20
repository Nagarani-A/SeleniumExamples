from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

s = Service("C:\\Users\\nagua\\PycharmProjects\\SeleniumExamples\\drivers\\chromedriver")
driver = webdriver.Chrome(service=s)
driver.maximize_window()

driver.get("https://www.bing.com/account/general?ru=https%3a%2f%2fwww.bing.com%2f&FORM=O2HV46&sh=0")

dd=driver.find_element(By.ID, "rpp")

s=Select(dd)

#s.select_by_index(1)
#or
#s.select_by_value("50")

s.select_by_visible_text("Auto")

p1=s.options#it will give all the webelementss and store in variable
print(p1)

#to print the values in the dropdown
for element in p1:
    p2=element.get_attribute("value")
    print(p2)

time.sleep(5)
driver.quit()

