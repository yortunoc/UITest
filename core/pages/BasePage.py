from seleniumpagefactory.Pagefactory import PageFactory

from core.drivers.DriverManager import DriverManager
from core.global_variables import EXPLICIT_WAIT


class BasePage(PageFactory):

    def __init__(self, driverManager=DriverManager(), timeout=EXPLICIT_WAIT):
        super().__init__()
        self.driver = driverManager.driver
        self.timeout = timeout

    locators = {
        "headerSection": ('class_name', 'theme__appBar___wbg0y TopBar__appBar___2z5Ld'),
        "footerSection": ('class_name', 'Footer__footer___JO_yR'),
        "baseLoadPage": ('XPATH', '//h2[text()="Your next destination"]')
    }
