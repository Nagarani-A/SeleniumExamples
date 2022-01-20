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

driver.get("http://demo.automationtesting.in/Windows.html")

driver.find_element(By.XPATH,"//*[@id='Tabbed']/a/button").click()

print(driver.current_window_handle)
handles=driver.window_handles

for handle in handles:
    driver.switch_to.window(handle)
    print(driver.title)
    if driver.title=="Selenium":
        driver.close()


time.sleep(5)
driver.quit()
