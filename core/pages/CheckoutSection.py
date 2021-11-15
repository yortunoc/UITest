import os
import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from core.pages.BasePage import BasePage


class CheckoutSection(BasePage):
    # define locators dictionary where key name will became WebElement using PageFactory
    locators = {
        "nameInput": ('XPATH', '//span[text()="Name"]//preceding-sibling::input'),
        "emailInput": ('XPATH', '//span[text()="Email Address"]//preceding-sibling::input'),
        "ssnInput": ('XPATH', '//span[text()="Social Security Number"]//preceding-sibling::input'),
        "phoneInput": ('XPATH', '//span[text()="Phone Number"]//preceding-sibling::input'),
        "promoCodeInput": ('XPATH', '//span[text()="I have a promo code"]//preceding-sibling::input'),
        "applyCodeBtn": ('XPATH', '//button[text()="Apply"]'),
        "conditionChk": ('XPATH', '//label[@data-react-toolbox="checkbox"]'),
        "payNowBtn": ('XPATH', '//button[text()="Pay now"]'),
        "uploadFile": ('XPATH', '//div[@class="CustomerInfo__dropzone-box___27VMo"]//following-sibling::input'),
        **BasePage.locators
    }

    def fill_form_checkout(self, name, email, social_number, phone_number, path_image, promo_code=None):
        self.nameInput.set_text(name)
        self.emailInput.set_text(email)
        self.ssnInput.set_text(social_number)
        self.phoneInput.set_text(phone_number)

        if promo_code:
            self.promoCodeInput.set_text(promo_code)
            self.applyCodeBtn.click_button()
        upload_xpath = '//div[@class="CustomerInfo__dropzone-box___27VMo"]//following-sibling::input'
        self.driver.find_element(By.XPATH, upload_xpath).send_keys(os.getcwd() + "\\resources\\image.jpeg")
        self.conditionChk.click_button()
        self.payNowBtn.click_button()



