from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time


s = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s)


driver.get("https://www.bing.com/")

driver.maximize_window()

driver.find_element(By.NAME, "q").send_keys("Nagarani")

driver.find_element(By.ID, "search_icon").click()

time.sleep(5)
driver.quit()


