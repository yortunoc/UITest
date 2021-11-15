from core.drivers.ChormeDriver import ChromeDriver
from core.drivers.FirefoxFactory import FirefoxDriver


class FactoryDriver:

    @staticmethod
    def get_driver_manager(driver_type):
        """
        This method gets driver object
        :param driver_type: the name of driver
        :return: Driver object
        """
        if 'chrome' == driver_type:
            return ChromeDriver.get_driver()
        if 'firefox' == driver_type:
            return FirefoxDriver.get_driver()
