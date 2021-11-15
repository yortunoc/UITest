from selenium import webdriver

from core.global_variables import PATH_CHROME_DRIVER


class ChromeDriver:

    @staticmethod
    def get_driver():
        """
        This method initialize the Chrome driver and return the instance
        :return:  the instance chrome driver
        """
        driver = webdriver.Chrome(PATH_CHROME_DRIVER)
        return driver
