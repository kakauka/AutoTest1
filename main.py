import allure
from selenium.webdriver.common.by import By
import pytest
import basePage
import util
import loginPage



@allure.feature('Авторизация111')
@allure.title("Успешная авторизация")
# @pytest.mark.parametrize("auth", ['testuser'])
def test_auth_success():
    """
       Успешная авторизация
    """
    success_login = True
    try:
        with allure.step(f"Ввод логина"):
            loginPage.find_element(loginPage.input_username_auth).send_keys("testuser")
        with allure.step(f"Ввод пароля"):
            loginPage.find_element(loginPage.input_password_auth).send_keys('testpass')
        with allure.step("Клик по кнопке 'Log in'"):
            loginPage.find_element(loginPage.find_button_login).click()
        with allure.step("Проверка входа в лк 'Title'"):
            assert util.driver.title == "Site administration | Django site admin"
        with allure.step(f"Выход из лк"):
            basePage.exit()
            assert util.driver.title == "Log in | Django site admin"
    except:
        allure.attach(util.driver.get_screenshot_as_png(), name='Screenshot', )
        success_login = False
    assert success_login == True


@allure.feature('Админка')
@allure.title("Создание Routine tasks")
# @pytest.mark.parametrize("auth", ['testuser'ss])
def test_add_routine_task():
    """
       Создание Routine tasks
    """
    add_task = True
    try:
        with allure.step(f"Авторизация"):
            loginPage.auth()
        with allure.step(f"Переход во вкладку 'Routine tasks'"):
            basePage.find_elementcss(basePage.btn_routine_tasks).click()
        with allure.step(f"Нажатие на кнопку 'ADD Routine tasks'"):
            basePage.find_element(basePage.btn_addroutine_tasks).click()
        with allure.step("Ввод текста в поле 'Activity code'"):
            basePage.find_element(basePage.input_activity_code_routine).send_keys('TestActivity')
        with allure.step("Ввод текста в поле 'Title'"):
            basePage.find_element(basePage.input_title).send_keys('TestTitle')
        with allure.step("Ввод текста в поле 'Description'"):
            basePage.find_element(basePage.input_description).send_keys('TestDescription')
        with allure.step("Поставить галочку 'Is moderation required'"):
            basePage.find_element(basePage.checkbox_moderation).click()
        with allure.step("Нажать на выбор формата"):
            basePage.find_element(basePage.choose_format).click()
        with allure.step("Выбрать формат 'Read text'"):
            basePage.find_element(basePage.choose_format_readtext).click()
        with allure.step("Нажать на кнопкк 'SAVE'"):
            basePage.find_element(basePage.btn_save_routine).click()
            assert basePage.find_element(basePage.successfully_routinetask).text == 'TestTitle (TestActivity)'
        with allure.step(f"Выход из лк"):
            basePage.exit()
    except:
        allure.attach(util.driver.get_screenshot_as_png(), name='Screenshot', )
        add_task = False
    assert add_task == True


@allure.feature('Админка')
@allure.title("Создание Story tasks")
def test_add_story_task():
    """
       Создание Story tasks
    """
    add_task = True
    try:
        with allure.step(f"Авторизация"):
            loginPage.auth()
        with allure.step(f"Переход во вкладку 'Story tasks'"):
            basePage.find_element(basePage.btn_story_tasks).click()
        with allure.step(f"Нажатие на кнопку 'ADD Story tasks'"):
            basePage.find_element(basePage.btn_addstory_tasks).click()
        with allure.step("Ввод текста в поле 'Activity code'"):
            basePage.find_element(basePage.input_activity_code_story).send_keys('TestStory')
        with allure.step("Ввод текста в поле 'Title'"):
            basePage.find_element(basePage.input_title).send_keys('TestTitleStory')
        with allure.step("Ввод текста в поле 'Description'"):
            basePage.find_element(basePage.input_description).send_keys('TestDescription')
        with allure.step("Поставить галочку 'Is moderation required'"):
            basePage.find_element(basePage.checkbox_moderation).click()
        with allure.step("Нажать на выбор формата"):
            basePage.find_element(basePage.choose_format).click()
        with allure.step("Выбрать формат 'Read text'"):
            basePage.find_element(basePage.choose_format_readtext).click()
        with allure.step("Нажать на кнопкк 'SAVE'"):
            basePage.find_element(basePage.btn_save_story).click()
            assert basePage.find_element(basePage.successfully_routinetask).text == 'TestTitleStory (TestStory)'
        with allure.step(f"Выход из лк"):
            basePage.exit()
    except:
        allure.attach(util.driver.get_screenshot_as_png(), name='Screenshot', )
        add_task = False
    assert add_task == True

# driver.quit()
