from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from core.global_variables import EXPLICIT_WAIT
from core.pages.BasePage import BasePage


class SpaceAndBeyondSection(BasePage):
    # define locators dictionary where key name will became WebElement using PageFactory
    locators = {
        "departmentInput": ('XPATH', '//label[contains(text(), "Departing")]//parent::div/input'),
        "returnIngInput": ('XPATH', '//label[contains(text(), "Returning")]//parent::div/input'),
        "adultsInput": ('XPATH', '//li[text()="Adults (18+)"]//parent::ul//parent::div//input'),
        "childrenInput": ('XPATH', '//li[text()="Children (0-7)"]//parent::ul//parent::div//input'),
        "destinationBtn": ('XPATH', '//button[contains(text(), "Select Destination")]'),
        "okDateBtn": ('XPATH', '//button[text()="Ok"]'),
        **BasePage.locators
    }

    def select_department_date(self, day):
        """
        This method select a date in department input
        :param day:  The day to select
        """
        actions = ActionChains(self.driver)
        actions.move_to_element(self.departmentInput).perform()
        self.departmentInput.click_button()
        self.select_day_and_ok(day)

    def select_returning_date(self, day):
        """
        This method select a date in returning input
        :param day:  The day to select
        """
        actions = ActionChains(self.driver)
        actions.move_to_element(self.returnIngInput).perform()
        self.returnIngInput.click_button()
        self.select_day_and_ok(day)

    def select_adults(self, adults=0):
        """
        This method select the number of adults
        :param adults: The number of adults
        """
        self.adultsInput.click_button()
        if adults != 0:
            self.select_list('Adults', adults)
        else:
            self.select_list('Adults', 'Adults (18+)')

    def select_children(self, children=0):
        """
        This method select the number of children
        :param children: The number of children
        """
        self.childrenInput.click_button()
        if children !=0:
            self.select_list('Children', children)
        else:
            self.select_list('Children', 'Children (0-7)')

    def select_day_and_ok(self, day):
        """
        This method find the element an select it after perform click in Ok button
        :param day: The day to select
        """
        day_xpath = '//span[text()="{}"]'.format(day)
        try:
            day_element = self.driver.find_element(By.XPATH, day_xpath)
            WebDriverWait(self.driver, EXPLICIT_WAIT).until(
                EC.element_to_be_clickable(day_element))
            day_element.click()
        except StaleElementReferenceException:
            day_element = self.driver.find_element(By.XPATH, day_xpath)
            WebDriverWait(self.driver, EXPLICIT_WAIT).until(
                EC.element_to_be_clickable(day_element))
            day_element.click()
        self.okDateBtn.click_button()

    def select_list(self, name, value):
        """
        This method select value from list and click on element
        :param name: The name of list
        :param value: The value of list
        """
        element_xpath = '//li[contains(text(), "{}")]//parent::ul/li[text()="{}"]'.format(name, value)
        element = self.driver.find_element(By.XPATH, element_xpath)
        WebDriverWait(self.driver, EXPLICIT_WAIT).until(
            EC.element_to_be_clickable(element))
        element.click()
