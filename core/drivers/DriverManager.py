from selenium.webdriver.support.wait import WebDriverWait

from core.drivers.FactoryDriver import FactoryDriver
from core.global_variables import DRIVER, IMPLICIT_WAIT, EXPLICIT_WAIT, BASE_URI


class SingletonMeta(type):
    """
    The Singleton class can be implemented in different ways in Python. Some
    possible methods include: base class, decorator, metaclass. We will use the
    metaclass because it is best suited for this purpose.
    """

    _instances = {}

    def __call__(cls, *args, **kwargs):
        """
        Possible changes to the value of the `__init__` argument do not affect
        the returned instance.
        """
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class DriverManager(metaclass=SingletonMeta):
    instance = None

    def __init__(self, driver_type=DRIVER, base_uri=BASE_URI):
        self.base_uri = base_uri
        self.driver = FactoryDriver.get_driver_manager(driver_type)
        self.set_waits()
        self.driver.maximize_window()
        # self.wait

    def set_waits(self, implicit_wait=IMPLICIT_WAIT, explicit_wait=EXPLICIT_WAIT):
        self.driver.implicitly_wait(implicit_wait)
        wait = WebDriverWait(self.driver, explicit_wait)
        # self.driver.implicitly_wait(explicit_wait)

