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

'''fr=driver.find_element(By.CLASS_NAME,"demo-frame")
driver.switch_to.frame(fr)
driver.find_element(By.ID,"datepicker").send_keys("01/01/2022")'''

# or

fr = driver.find_element(By.CLASS_NAME, "demo-frame")
driver.switch_to.frame(fr)
driver.find_element(By.ID, "datepicker").click()
driver.find_element(By.XPATH,"//*[@id='ui-datepicker-div']/div/a[1]/span").click()

driver.find_element(By.LINK_TEXT,"31").click()

time.sleep(3)
driver.quit()
