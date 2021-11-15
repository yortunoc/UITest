from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from core.global_variables import EXPLICIT_WAIT
from core.pages.BasePage import BasePage
from core.pages.CheckoutSection import CheckoutSection


class DestinationSection(BasePage):
    # define locators dictionary where key name will became WebElement using PageFactory
    locators = {
        "travelerLbl": ('XPATH', '//h3[contains(text(), "traveler")]'),
        "LoadMoreBtn": ('XPATH', '//button[contains(text(), "Load more")]'),
        "priceSlideBar": ('class_name', 'PurpleSlider__innerknob___2wxLd'),
        "priceInput": ('XPATH', '//div[contains(@class,"PurpleSlider__input___3H1SF")]/input'),
        **BasePage.locators
    }

    def select_specific_destination(self, name_destination):
        book_xpath = '//h5[contains(text(), "{}")]//parent::div//parent::div//following-sibling::div//child::button'
        bookBtn = self.driver.find_element(By.XPATH, book_xpath.format(name_destination))
        WebDriverWait(self.driver, EXPLICIT_WAIT).until(EC.element_to_be_clickable(bookBtn))
        bookBtn.click()
        return CheckoutSection()

    def move_price_slide(self):
        ActionChains(self.driver).drag_and_drop_by_offset(self.priceSlideBar, -200, 0).perform()

    def select_all_price_destination(self):
        price_list_destination = '//button[contains(text(), "Book" )]//parent::div/span'
        price_list_elements = self.driver.find_elements(By.XPATH, price_list_destination)
        return price_list_elements
