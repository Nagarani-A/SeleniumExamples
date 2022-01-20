from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

s = Service("C:\\Users\\nagua\\PycharmProjects\\SeleniumExamples\\drivers\\chromedriver")
driver = webdriver.Chrome(service=s)
driver.maximize_window()

driver.get("https://www.bing.com/account/general?ru=https%3a%2f%2fwww.bing.com%2f&FORM=O2HV65")


p1=driver.find_element(By.ID, "newsnt").is_selected()
print(p1)

if p1:
    print("Already checked")
else:
    driver.find_element(By.ID, "newsnt").click()
    print("Checked successfully")

time.sleep(5)
driver.quit()

