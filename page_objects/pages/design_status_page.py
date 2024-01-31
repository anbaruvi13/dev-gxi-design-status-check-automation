from test_utility.utility_methods import UtilMethods
from page_objects.locators.design_page_locator import DesignStatusPageLocator


class DesignStatusPage(object):

    def __init__(self, driver):
        self.driver = driver
        self.util_obj = UtilMethods(self.driver)
        self.application_number_text_box_xpath = DesignStatusPageLocator.application_number_text_box_xpath
        self.captcha_xpath = DesignStatusPageLocator.captcha_xpath
        self.captcha_text_box_xpath = DesignStatusPageLocator.captcha_text_box_xpath
        self.show_us_button_xpath = DesignStatusPageLocator.show_us_button_xpath

    def design_status_check(self):
        print("This test run")
        return True
