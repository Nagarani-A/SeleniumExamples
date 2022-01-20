
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

s = Service("C:\\Users\\nagua\\PycharmProjects\\SeleniumExamples\\drivers\\chromedriver")
driver = webdriver.Chrome(service=s)

driver.get("https://www.bing.com/")

driver.find_element(By.NAME, "q").send_keys("Nagarani")

driver.find_element(By.ID, "search_icon").click()

time.sleep(5)
driver.quit()
