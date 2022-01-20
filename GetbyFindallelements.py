from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
#import time

s = Service("C:\\Users\\nagua\\PycharmProjects\\SeleniumExamples\\drivers\\chromedriver")
driver = webdriver.Chrome(service=s)
driver.maximize_window()

driver.get("https://www.w3schools.com/html/")


#p1=driver.find_elements(By.TAG_NAME, "rani")
p1=driver.find_elements(By.TAG_NAME, "a")


print(len(p1))
 
# to print the values in the dropdown
for element in range(len(p1)):
    if p1[element].is_displayed():
        print(p1[element].text)

#time.sleep(3)
driver.quit()
