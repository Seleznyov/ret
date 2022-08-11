from .base_page import BasePage
from .locators import AuthorizationUserLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert "login" in self.browser.current_url,"url is not correct"

    def authorization(self, name, password):
        Name = self.browser.find_element(*AuthorizationUserLocators.Name)
        Name.send_keys(name)
        Password = self.browser.find_element(*AuthorizationUserLocators.Password)
        Password.send_keys(password)
        Button = self.browser.find_element(*AuthorizationUserLocators.Button)
        Button.click()
