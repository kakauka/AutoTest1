from selenium.webdriver.common.by import By
from util import driver

# Locators Routine tasks
btn_save_routine= '//*[@id="routinetask_form"]/div/div[7]/input[1]'
btn_routine_tasks = '#content-main > div.app-activities.module > table > tbody > tr.model-routinetask > th > a'
btn_addroutine_tasks = '//*[@id="content-main"]/ul/li/a'
input_activity_code_routine = '/html/body/div[1]/div[3]/div/div[1]/div/form/div/fieldset/div[1]/div/input'
input_title = '//*[@id="id_title"]'
input_description = '//*[@id="id_description"]'
checkbox_moderation = '//*[@id="id_is_moderation_required"]'
choose_format = '//*[@id="id_format"]'
choose_format_readtext = '//*[@id="id_format"]/option[2]'
successfully_routinetask = '//*[@id="main"]/div/ul/li/a'

# Locators Story tasks
btn_story_tasks = '//*[@id="content-main"]/div[2]/table/tbody/tr[2]/th/a'
btn_addstory_tasks = '//*[@id="content-main"]/ul/li/a'
input_activity_code_story = '//*[@id="id_code"]'
btn_save_story = '//*[@id="storytask_form"]/div/div[5]/input[1]'

# Exit button
btn_exit = '//*[@id="user-tools"]/a[3]'
btn_home = '//*[@id="container"]/div[2]/a'

# Function
def find_elementcss(css_selector):
    return driver.find_element(By.CSS_SELECTOR, value=css_selector)

def find_element(xpath):
    return driver.find_element(By.XPATH, value=xpath)

def exit():
    find_element(btn_exit).click()
    find_element(btn_home).click()