from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from core.pages.BasePage import BasePage
from core.pages.LoginPage import LoginPage


class MenuSection(BasePage):
    # define locators dictionary where key name will became WebElement using PageFactory
    locators = {
        "loginBtn": ('class_name', 'NavButton__nav-button___34wHC'),
        "userBtn": ('XPATH', '//span[contains(text(), "Hello")]//parent::button'),
        "logoutBtn": ('XPATH', '//a[contains(text(), "Log out")]'),
        **BasePage.locators
    }

    def logout(self):
        self.driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.CONTROL + Keys.HOME)
        self.userBtn.click_button()
        self.logoutBtn.click_button()

    def login(self):
        self.driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.CONTROL + Keys.HOME)
        self.loginBtn.click_button()
        return LoginPage()
