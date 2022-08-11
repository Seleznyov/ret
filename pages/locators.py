from selenium.webdriver.common.by import By

class BasePageLocators():
    USER_ICON = (By.CSS_SELECTOR, ".profile-picture")
    Queues = (By.XPATH, "//span[contains(text(),'Очереди')]")
    SearchByFin = (By.XPATH, "//div[1]/app-search-field[1]/div[1]/input[1]")
    SearchButton = (By.XPATH, "//div[1]/app-search-field[1]/div[1]/mat-app-button[1]/button[1]")
    SearchResult = (By.XPATH, "//tbody/tr[1]")
    StatusApp = (By.XPATH, "//div[contains(text(),'Задача пользователя')]")
    VerificationTab = (By.XPATH, "//div[@class='mat-tab-labels']//div[contains(text(),'Верификация')]")

class AuthorizationUserLocators():
    Name = (By.CSS_SELECTOR, "[placeholder='Имя пользователя']")
    Password = (By.CSS_SELECTOR, "[placeholder='Пароль']")
    Button = (By.CSS_SELECTOR, "[class='mat-button mat-button-base semiRound blue size-medium color-white hover-blue custom-button-style']")

class ShortForm():
    Product_type = (By.CSS_SELECTOR, "[class='search-select-label ng-star-inserted']")
    Choose_first = (By.XPATH, "//span[contains(text(),' Кредит наличными (ЗП проект)')]")
    Credit_amount = (By.CSS_SELECTOR, "input[placeholder='Сумма кредита, AZN *']")
    Phone = (By.CSS_SELECTOR, "input[placeholder='Мобильный телефон  *']")
    Income = (By.CSS_SELECTOR, "input[placeholder='Доход согласно выписке со счета *']")
    Fin = (By.CSS_SELECTOR, "input[placeholder='FIN-код *']")
    SendSMS = (By.XPATH, "//div[1]/div[1]/div[2]/div[1]/div[1]/mat-app-button[1]/button[1]")
    InputCode = (By.XPATH, "//input[@id='mat-input-8']")
    Agreement = (By.XPATH, "//mat-tab-body/div[1]/app-credit-app[1]/form[1]/div[1]/perfect-scrollbar[1]/div[1]/div[1]/div[1]/div[1]/div[4]/div[1]//mat-app-slide-toggle[1]/mat-slide-toggle[1]/label[1]/div[1]")
    DsaOwner = (By.XPATH, "//perfect-scrollbar[1]/div[1]/div[1]/div[1]/div[2]/div[1]/mat-app-search-select[1]/div[1]/mat-form-field[1]/div[1]/div[1]/div[1]")
    ChoiceDsa = (By.XPATH, "//perfect-scrollbar[1]/div[1]/div[1]/div[1]/mat-option[1]/span[1]")
    CreateApp = (By.XPATH, "//mat-tab-body/div[1]/app-credit-app[1]/form[1]/div[2]/mat-app-button[1]/button[1]")

# class QueuesPage():
class AppLocators():
    Block1 = (By.XPATH, "//div[1]/app-layout-for-steps[1]/mat-accordion[1]/mat-expansion-panel[1]/mat-expansion-panel-header[1]/span[1]/mat-panel-title[1]/div[1]/div[2]")

