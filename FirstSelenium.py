from selenium import webdriver
from selenium.webdriver.chrome.service import Service

s = Service("D:\chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.maximize_window()
driver.get('https://www.google.com/')
myPageTitle = driver.title
print(myPageTitle)
assert  "Google" in myPageTitle
driver.quit()
print(driver.quit())
