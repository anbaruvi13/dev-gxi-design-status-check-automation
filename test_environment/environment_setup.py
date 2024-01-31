import unittest
from selenium import webdriver
from test_utility import create_log
import os


class EnvironmentSetup(unittest.TestCase):
    driver = None

    @classmethod
    def setUpClass(self):
        # use_browser = os.environ.get("BROWSER").lower()
        use_browser = 'chrome'
        print("Select browser is " + use_browser)

        if use_browser == 'ie':
            create_log.create_log("Execution started in Internet Explorer...")
            self.driver = webdriver.Edge()
            ie_driver = "web_drivers/IEDriverServer.exe"
            self.driver = webdriver.Ie()
            create_log.create_log("Internet Explorer opened successfully")
        elif use_browser == 'chrome':
            create_log.create_log("Execution started in Chrome...")
            self.driver = webdriver.Chrome()
            create_log.create_log("Chrome opened successfully")
        else:
            create_log.create_log(
                "Execution started in chrome since valid browser was not selected in the config file...")
            self.driver = webdriver.Chrome()
            create_log.create_log("Chrome opened successfully")

        self.driver.maximize_window()
        base_url = "https://search.ipindia.gov.in/DesignApplicationStatus/"
        self.driver.get(base_url)
        create_log.create_log("Home Page Loading...")
        self.driver.implicitly_wait(10)

    @classmethod
    def tearDownClass(self):
        if self.driver != None:
            self.driver.close()
            self.driver.quit()
            pass
