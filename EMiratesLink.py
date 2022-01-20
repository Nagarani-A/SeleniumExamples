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

text2 = "Travel information"

driver.get("https://www.emirates.com/ae/english/")

# p1=driver.find_elements(By.TAG_NAME, "q")

driver.find_element(By.XPATH, "//*[@id='onetrust-accept-btn-handler']").click()

driver.find_element(By.XPATH, "//a[@data-link='MANAGE']").click()
p1 = driver.find_element(By.XPATH, "//a[@data-link='MANAGE:Before you fly']")
ActionChains(driver).move_to_element(p1).perform()

val = driver.find_element(By.XPATH,
                          "//div[@class='third-level-menu__list-item-link-holder' and @role='heading']/a")

for element in range(len(val)):
    text1 = val[element].text
    if text1 == text2:
        print(text1)
        val[element].click()
        break

print("Test completed")

time.sleep(5)
driver.quit()
