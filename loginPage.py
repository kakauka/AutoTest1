from selenium.webdriver.common.by import By
from util import driver
from basePage import find_element


# Locators Auth
input_username_auth = '//*[@id="id_username"]'
input_password_auth = '//*[@id="id_password"]'
find_button_login = '//*[@id="login-form"]/div[3]/input'



def auth():
    find_element(input_username_auth).send_keys("testuser")
    find_element(input_password_auth).send_keys('testpass')
    find_element(find_button_login).click()
