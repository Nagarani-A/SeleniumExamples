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

driver.get("https://www.w3schools.com/html/html_tables.asp")
'''#for first col
before="//*[@id='customers']/tbody/tr["
after= " ]/td[1]"

#for sec col
before1="//*[@id='customers']/tbody/tr["
after1= " ]/td[2]"'''
t1=driver.find_element(By.XPATH,"//*[@id='customers']/tbody")
t2=t1.find_elements(By.TAG_NAME,'tr')
print(len(t2))

before = "//tr["
after = " ]/td[1]"
after1 = " ]/td[2]"

for _ in range(2,len(t2)):
    xp1 = before + str(_) + after
    val = driver.find_element(By.XPATH, xp1).text
    print(val)

    xp2 = before + str(_) + after1
    val2 = driver.find_element(By.XPATH, xp2).text
    print(val2)

time.sleep(5)
driver.quit()
