from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.queues_page import QueuesPage
import pytest
import allure

from selenium.webdriver.common.action_chains import ActionChains

from random import randint
from .api import get_use
import time


if get_use() == "Агент прямых продаж":
    fin = ('T' + str(randint(000000, 999999)))
    amount = str(randint(10000, 11111))

    @pytest.fixture(scope="function", autouse=True)
    def setup(browser):
        link = "https://vtb.pstlabs.by/vtb-retail/#/login"
        login_page = LoginPage(browser, link)
        login_page.open()
        # Проверка страницы логина
        login_page.should_be_login_page()
        # Вынести вверх
        login_page.authorization(name="sseleznev", password="test")

    def test_create_app(browser):
        maine_page = MainPage(browser, browser.current_url)
        # Проверка что пользователь перешел на dashboard
        maine_page.should_be_authorized_user()
        maine_page.short_form(amount=amount, phone='222222222', income='1010', fin=fin)
        # Хочу ещё перехватить сообщение "Заявка создана"

        maine_page.page_open_queues()
        #Добавил Ожидание для загрузки страницы
        time.sleep(2)


    def test_check_app(browser):
        maine_page = MainPage(browser, browser.current_url)
        maine_page.page_open_queues()
        # Добавил Ожидание для загрузки страницы
        time.sleep(2)
        queues_page = QueuesPage(browser, browser.current_url)
        # Проверка страницы Очереди
        queues_page.should_be_queues_page()
        queues_page.find_app(fin=fin)
        # Проверка что заявка существует, отображается в списке
        queues_page.should_be_app_presence()
        queues_page.open_app()
        queues_page.should_be_app_open()


    def test_check_status_app(browser):
        maine_page = MainPage(browser, browser.current_url)
        maine_page.page_open_queues()
        time.sleep(2)
        queues_page = QueuesPage(browser, browser.current_url)
        queues_page.should_be_queues_page()
        queues_page.find_app(fin=fin)
        time.sleep(5)
        queues_page.status_app()





