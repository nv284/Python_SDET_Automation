from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service = Service(executable_path=r"C:\Drivers\chromedriver-win64\chromedriver.exe")

driver = webdriver.Chrome(service=service)

driver.get("https://google.com")