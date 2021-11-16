import pytest

from core.drivers.DriverManager import DriverManager
from core.global_variables import BASE_URI
from core.pages.DestinationSection import DestinationSection
from core.pages.MenuSection import MenuSection
from core.pages.SpaceAndBeyondSection import SpaceAndBeyondSection


@pytest.fixture(autouse=True, scope='class')
def initialize_driver():
    """
    This fixture initialize the driver before to execute class test and after quit from driver when all test of
    class was executed
    """
    DriverManager()
    yield
    DriverManager().driver.quit()


class TestUIDestinations:

    @pytest.fixture(autouse=True, scope='function')
    def go_to_home_page(self):
        DriverManager().driver.get(BASE_URI)

    def test_login_and_logout(self):
        """
        This test that si possible login page and logout from page
        """
        menu = MenuSection()
        login_page = menu.login()
        login_page.login_page(username='yury', password='yver')
        menu.logout()

    def test_price_destination(self):
        """
        This test verify that all destination elements in page are lower that price in slide element
        """
        destination_section = DestinationSection()
        destination_section.move_price_slide()
        price_list_elements = destination_section.select_all_price_destination()
        price_limit = destination_section.priceInput.getAttribute('value')
        price_limit = float(price_limit.replace('%', ''))
        for price_element in price_list_elements:
            price_destination = float(price_element.text.replace('$', ''))
            assert price_destination <= price_limit

    def test_checkout_destination(self):
        """
        This test verify the checkout destination, fill all values in form and click in pay now
        """
        menu = MenuSection()
        login_page = menu.login()
        login_page.login_page(username='yury', password='yver')
        destination_destination = DestinationSection()
        checkout_section = destination_destination.select_specific_destination('Shenji')
        checkout_section.fill_form_checkout('yury', 'yury@gmail.com', '123-45-6789', 419, '/resources/image.jpeg',
                                            12356)

    @pytest.mark.parametrize("department_date, returning_date, adults, children", [
        (18, 20, 3, 1),
        (18, 20, 3, 3),
        (18, 20, 1, 3),
        (18, 20, 1, 4)
    ])
    def test_customized_destination(self, department_date, returning_date, adults, children):
        """
        This test verify that after configure the search of destination, the title should contains this information.
        """
        setup_destination = SpaceAndBeyondSection()
        setup_destination.select_department_date(department_date)
        setup_destination.select_returning_date(returning_date)
        setup_destination.select_adults(adults)
        setup_destination.select_children(children)
        expected_title = '{} travelers, Nov {} – {}'.format(adults + children, department_date, returning_date)
        destination_section = DestinationSection()
        destination_section.travelerLbl.text
        assert destination_section.travelerLbl.text == expected_title, "Expecting title should be {} but actual " \
                                                                       "is {}".format(expected_title,
                                                                                      destination_section
                                                                                      .travelerLbl.text)

    def test_verify_load_more_button(self):
        """
        Test to very that after click in load more button destination item should be more
        """
        destination_section = DestinationSection()
        old_destination_list = destination_section.select_all_price_destination()
        destination_section.LoadMoreBtn.click_button()
        actual_destination_list = destination_section.select_all_price_destination()
        assert len(actual_destination_list) > len(old_destination_list), "Actual destination list {} should be " \
                                                                         "more {}after click in load more " \
                                                                         "button".format(len(actual_destination_list),
                                                                                         len(old_destination_list))

    def test_verify_destination_drop_down(self):
        """
        Test to very that after select a launch all item should be related with it
        """
        destination_section = DestinationSection()
        launch_name = 'Shaheying'
        destination_section.select_launch_drop_down(launch_name)
        all_destination = destination_section.select_all_destination()
        for destination in all_destination:
            assert launch_name in destination.text, "Destination should contains {} " \
                                                    "but actual is {}".format(launch_name, destination.text)
