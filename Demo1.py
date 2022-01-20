from selenium import webdriver

browser = webdriver.Firefox(executable_path="C:/Drivers/geckodriver-v0.26.0-win64/geckodriver.exe")
browser.get('http://selenium.dev/')


# due to the compatibility issues this will shows error