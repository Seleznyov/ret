from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .locators import BasePageLocators, ShortForm,AppLocators,Decision_Final

import time
import requests

class BasePage():
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def is_not_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True
        return False

    def should_be_authorized_user(self):
        assert self.is_element_present(*BasePageLocators.USER_ICON), "User icon is not presented, probably unauthorised user"

    def short_form(self,amount,phone,income,fin):
        Product_type = self.browser.find_element(*ShortForm.Product_type)
        Product_type.click()
        Choose_first = self.browser.find_element(*ShortForm.Choose_first)
        Choose_first.click()
        Credit_amount = self.browser.find_element(*ShortForm.Credit_amount)
        Credit_amount.send_keys(amount)
        Income = self.browser.find_element(*ShortForm.Income)
        Income.send_keys(income)
        Phone = self.browser.find_element(*ShortForm.Phone)
        Phone.send_keys(phone)
        Fin =self.browser.find_element(*ShortForm.Fin)
        Fin.send_keys(fin)
        time.sleep(1)

        Agreement=self.browser.find_element(*ShortForm.Agreement)
        Agreement.click()

        DsaOwner = self.browser.find_element(*ShortForm.DsaOwner)
        # скролл к эдементу
        DsaOwner.location_once_scrolled_into_view
        DsaOwner.click()
        ChoiceDsa = self.browser.find_element(*ShortForm.ChoiceDsa)

        ChoiceDsa.click()
        CreateApp = self.browser.find_element(*ShortForm.CreateApp)
        CreateApp.click()

    def find_app(self,fin):
        SearchByFin = self.browser.find_element(*BasePageLocators.SearchByFin)
        SearchByFin.send_keys(fin)
        SearchButton = self.browser.find_element(*BasePageLocators.SearchButton)
        SearchButton.click()

    def should_be_app_presence(self):
        assert self.is_element_present(*BasePageLocators.SearchResult), "app is not presented, probably not correct fin"

    def should_be_app_open(self):
        assert self.is_element_present(*AppLocators.Block1), "app is not open"

    def status_app(self):
        assert self.is_element_present(*BasePageLocators.StatusApp), "status app is not USER_TASK"

    def verification_view(self):
        assert self.is_element_present(*BasePageLocators.VerificationTab), "tab  is not present"

    def verification_is_not_view(self):
        assert self.is_not_element_present(*BasePageLocators.VerificationTab), "tab  is not present"

    def add_document_on_decision_final(self):
        RightArrow = self.browser.find_element(*Decision_Final.RightArrow)
        RightArrow.click()
        DocumentsTab = self.browser.find_element(*Decision_Final.DocumentsTab)
        DocumentsTab.click()

        AddFile = self.browser.find_element(*Decision_Final.AddFile)
        AddFile.click()
        TypeFile = self.browser.find_element(*Decision_Final.TypeFile)
        TypeFile.click()
        TypeFileAgreement = self.browser.find_element(*Decision_Final.TypeFileAgreement)
        TypeFileAgreement.click()
        ButtonSelectFile = self.browser.find_element(*Decision_Final.ButtonSelectFile)
        ButtonSelectFile.send_keys("D:/CDP/ret/files/TestFile.pdf")
        DownloadFile = self.browser.find_element(*Decision_Final.DownloadFile)
        DownloadFile.click()
        time.sleep(3)
        AddFile = self.browser.find_element(*Decision_Final.AddFile)
        AddFile.click()
        TypeFile = self.browser.find_element(*Decision_Final.TypeFile)
        TypeFile.click()
        TypeFilFatca = self.browser.find_element(*Decision_Final.TypeFilFatca)
        TypeFilFatca.click()
        ButtonSelectFile = self.browser.find_element(*Decision_Final.ButtonSelectFile)
        ButtonSelectFile.send_keys("D:/CDP/ret/files/TestFile.pdf")
        DownloadFile = self.browser.find_element(*Decision_Final.DownloadFile)
        DownloadFile.click()








