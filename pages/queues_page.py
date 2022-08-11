from .base_page import BasePage
from .locators import BasePageLocators

class QueuesPage(BasePage):
    def should_be_queues_page(self):
        self.should_be_login_url()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert "queues" in self.browser.current_url, "url is not correct"

    def open_app(self):
        SearchResult = self.browser.find_element(*BasePageLocators.SearchResult)
        SearchResult.click()