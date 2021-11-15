from core.pages.BasePage import BasePage


class LoginPage(BasePage):
    # define locators dictionary where key name will became WebElement using PageFactory

    locators = {
        "loginInput": ('XPATH', '//span[contains(text(), "Username")]//parent::div/input'),
        "passwordInput": ('XPATH', '//span[contains(text(), "Password")]//parent::div/input'),
        "singinBtn": ('XPATH', '//button[@form="login"]'),
        "cancelBtn": ('XPATH', '//button[contains(text(), "Cancel")]'),
        **BasePage.locators
    }

    def login_page(self, username, password):
        """
        This method fill the form and login into page
        :param username: The user name to login
        :param password: The password to login
        """
        self.loginInput.set_text(username)
        self.passwordInput.set_text(password)
        self.singinBtn.click_button()
