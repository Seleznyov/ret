from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.queues_page import QueuesPage
import pytest
import allure
from selenium.webdriver.common.action_chains import ActionChains

from random import randint
from .api import get_use
import time

#Перед тестом меняем мок делаем так чтобы заявка пошла на верефикацию
# Прогнать заявку на этап Верефикация
# Взять фин заявки
fin = "T614552"

@pytest.fixture(scope="function", autouse=True)
def setup(browser):
    link = "https://vtb.pstlabs.by/vtb-retail/#/login"
    login_page = LoginPage(browser, link)
    login_page.open()
    # Проверка страницы логина
    login_page.should_be_login_page()

@pytest.mark.parametrize('name', ["vtb_admin","vtb_under","vtb_limit_owner","vtb_risk_boss","vtb_auditor","vtb_risk_admin"])
def test_view(browser, name):
    login_page = LoginPage(browser, browser.current_url)
    login_page.authorization(name=name, password="")
    maine_page = MainPage(browser, browser.current_url)
    maine_page.page_open_queues()
    time.sleep(2)
    queues_page = QueuesPage(browser, browser.current_url)
    queues_page.should_be_queues_page()
    queues_page.find_app(fin=fin)
    queues_page.open_app()
    time.sleep(5)
    queues_page.verification_view()

@pytest.mark.parametrize('name', ["vtb_credit_manager","vtb_call_center","vtb_call_center_boss",
                                  "vtb_dsa","vtb_dsa_boss","vtb_credit_admin",
                                  "vtb_analyst","vtb_partner","vtb_document_control",
                                   "vtb_business_boss","vtb_business_admin"])
def test_not_view(browser, name):
    login_page = LoginPage(browser, browser.current_url)
    login_page.authorization(name=name, password="$EcUr!t@s")
    maine_page = MainPage(browser, browser.current_url)
    maine_page.page_open_queues()
    time.sleep(2)
    queues_page = QueuesPage(browser, browser.current_url)
    queues_page.should_be_queues_page()
    queues_page.find_app(fin=fin)
    time.sleep(3)
    queues_page.open_app()
    time.sleep(3)
    queues_page.verification_is_not_view()


