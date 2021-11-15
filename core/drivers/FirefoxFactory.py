
from selenium import webdriver

from core.global_variables import PATH_FIREFOX_DRIVER


class FirefoxDriver:

    @staticmethod
    def get_driver():
        driver = webdriver.Firefox(PATH_FIREFOX_DRIVER)
        return driver
