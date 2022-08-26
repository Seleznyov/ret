from .base_page import BasePage
from .locators import BasePageLocators

class MainPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)

    def should_be_main_page(self):
        self.should_be_main_url()

    def should_be_main_url(self):
        # реализуйте проверку на корректный url адрес
        assert "dashboard" in self.browser.current_url, "url is not correct"

    def page_open_queues(self):
        QueuesPage = self.browser.find_element(*BasePageLocators.Queues)
        QueuesPage.click()

    def open_app(self):
        SearchResult = self.browser.find_element(*BasePageLocators.SearchResult)
        SearchResult.click()