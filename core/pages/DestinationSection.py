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
        """
        This method select an specific destination to checkout
        :param name_destination: The name of destination
        :return: Instance of checkoutSection
        """
        book_xpath = '//h5[contains(text(), "{}")]//parent::div//parent::div//following-sibling::div//child::button'
        bookBtn = self.driver.find_element(By.XPATH, book_xpath.format(name_destination))
        WebDriverWait(self.driver, EXPLICIT_WAIT).until(EC.element_to_be_clickable(bookBtn))
        bookBtn.click()
        return CheckoutSection()

    def move_price_slide(self):
        """
        This method move the price slide
        """
        ActionChains(self.driver).drag_and_drop_by_offset(self.priceSlideBar, -200, 0).perform()

    def select_all_price_destination(self):
        """
        This methods gets all price of destination
        :return: the destination element with price information
        """
        price_list_destination = '//button[contains(text(), "Book" )]//parent::div/span'
        price_list_elements = self.driver.find_elements(By.XPATH, price_list_destination)
        return price_list_elements
