import os
import sys
from functools import wraps
from unittest import TestCase

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from core.drivers.DriverManager import DriverManager
from core.global_variables import BASE_URI, EXPLICIT_WAIT
from core.pages.DestinationSection import DestinationSection
from core.pages.MenuSection import MenuSection
from core.pages.SpaceAndBeyondSection import SpaceAndBeyondSection


class TryTesting(TestCase):

    @classmethod
    def setUpClass(cls):
        driver_manager = DriverManager()
        cls.driver = driver_manager.driver

    def setUp(self):
        self.driver.get(BASE_URI)
        menu = MenuSection()
        WebDriverWait(self.driver, EXPLICIT_WAIT).until(EC.element_to_be_clickable(menu.baseLoadPage))

    def tearDown(self):
        if self._outcome.errors:
            self.driver.save_screenshot('Screenshots/{}.png'.format(self._testMethodName))

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    from functools import wraps

    def test_login_and_logout(self):
        menu = MenuSection()
        login_page = menu.login()
        login_page.login_page(username='yury', password='yver')
        menu.logout()

    # def test_price_destination(self):
    #     destination_destination = DestinationSection()
    #     destination_destination.move_price_slide()
    #     price_list_elements = destination_destination.select_all_price_destination()
    #     price_limit = destination_destination.priceInput.getAttribute('value')
    #     price_limit = float(price_limit.replace('%', ''))
    #     for price_element in price_list_elements:
    #         price_destination = float(price_element.text.replace('$', ''))
    #         print("{} ------ {}".format(price_destination, price_limit))
    #         assert price_destination <= price_limit

    def test_checkout_destination(self):
        destination_destination = DestinationSection()
        checkout_section = destination_destination.select_specific_destination('Shenji')
        checkout_section.fill_form_checkout('yury', 'yury@gmail.com', '123-45-6789', 419, 'path_image', 12356)

    # def test_customized_destination(self):
    #     setup_destination = SpaceAndBeyondSection()
    #     department_date = 18
    #     setup_destination.select_department_date(department_date)
    #     returning_date = 20
    #     setup_destination.select_returning_date(returning_date)
    #     adults = 2
    #     setup_destination.select_adults(adults)
    #     children = 3
    #     setup_destination.select_children(children)
    #
    #     expected_title = '{} travelers, Nov {} – {}'.format(adults + children, department_date, returning_date)
    #     destination_section = DestinationSection()
    #     destination_section.travelerLbl.text
    #     assert destination_section.travelerLbl.text == expected_title
