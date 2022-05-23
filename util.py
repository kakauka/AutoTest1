from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import allure
import pytest



chrome_options = Options()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome('C:/Work/selenium-web-driver/chromedriver.exe')
# driver = webdriver.Chrome('C:/Work/selenium-web-driver/chromedriver.exe,options=chrome_options) # отключает визибл
driver.implicitly_wait(5)
driver.get('https://sandbox.1-gadget.com/admin')

