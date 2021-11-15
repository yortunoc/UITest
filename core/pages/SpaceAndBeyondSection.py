from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver import Keys, ActionChains
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
        actions = ActionChains(self.driver)
        actions.move_to_element(self.departmentInput).perform()
        # self.driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.CONTROL + Keys.HOME)
        self.departmentInput.click_button()
        self.select_day_and_ok(day)

    def select_returning_date(self, day):
        actions = ActionChains(self.driver)
        actions.move_to_element(self.returnIngInput).perform()
        # self.driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.CONTROL + Keys.HOME)
        self.returnIngInput.click_button()
        self.select_day_and_ok(day)

    def select_adults(self, adults):
        self.adultsInput.click_button()
        self.select_list('Adults', adults)

    def select_children(self, children):
        self.childrenInput.click_button()
        self.select_list('Children', children)

    def select_day_and_ok(self, day):
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
        element_xpath = '//li[contains(text(), "{}")]//parent::ul/li[text()="{}"]'.format(name, value)
        element = self.driver.find_element(By.XPATH, element_xpath)
        WebDriverWait(self.driver, EXPLICIT_WAIT).until(
            EC.element_to_be_clickable(element))
        element.click()
