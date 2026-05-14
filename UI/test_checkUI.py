import allure
import pytest
from playwright.sync_api import Page, expect
from pytest_playwright.pytest_playwright import page

@allure.title("Проверка авторизации на сайте apex.ru c корректными login и password")
@allure.tag("Позитивный кейс")

@pytest.mark.UITest
@pytest.mark.critReg
def test_auth_right(page: Page, user_config):
    with allure.step(f"Заходим на {user_config.piUrlUI}"):
        page.goto(user_config.piUrlUI)
    with allure.step("Клик по первой кнопке Войти"):
        page.locator("span.white_dashed:text('Войти')").click()
    with allure.step("Заполнение формы по login и password"):
        page.locator("#DIALOG_login_user_login").fill(user_config.piUserValid)
        page.locator("#DIALOG_login_user_passwd").fill(user_config.piPassValid)
    with allure.step("Клик по кнопке отправки login и password на авторизацию"):
        page.locator('input.BUTTON_round_color[value="Войти"]').click()
    with allure.step("Проверяем ошибку авторизации"):
        expect(page.get_by_text('Харитонов Алексей')).to_be_visible()

@allure.title("Проверка авторизации на сайте apex.ru c некорректными login и password")
@allure.tag("Негативный кейс")
@pytest.mark.UITest
@pytest.mark.critReg
def test_auth_not_right(page: Page, user_config):
    with allure.step(f"Заходим на {user_config.piUrlUI}"):
        page.goto(user_config.piUrlUI)
    with allure.step("Клик по первой кнопке Войти"):
        page.locator("span.white_dashed:text('Войти')").click()
    with allure.step("Заполнение формы по login и password"):
        page.locator("#DIALOG_login_user_login").fill(user_config.piUserNotValid)
        page.locator("#DIALOG_login_user_passwd").fill(user_config.piPassNotValid)
    with allure.step("Клик по кнопке отправки login и password на авторизацию"):
        page.locator('input.BUTTON_round_color[value="Войти"]').click()
    with allure.step("Проверяем ошибку авторизации"):
        expect(page.get_by_text('Неверный пароль!')).to_be_visible()

