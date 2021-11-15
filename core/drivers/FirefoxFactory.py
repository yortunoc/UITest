from selenium import webdriver

from core.global_variables import PATH_FIREFOX_DRIVER


class FirefoxDriver:

    @staticmethod
    def get_driver():
        """
        This method initialize the Firefox driver and return the instance
        :return:  the instance firefox driver
        """
        driver = webdriver.Firefox(PATH_FIREFOX_DRIVER)
        return driver
