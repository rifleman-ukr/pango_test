from appium.webdriver.common.appiumby import AppiumBy
from selenium.common import NoSuchElementException

from automation_framework.conftest import driver


class UnitsPage:
    def __init__(self, driver):
        self.driver = driver
        self._title = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("°C")')
        self._back_button = (AppiumBy.ACCESSIBILITY_ID, 'Navigate up')
        self._celsius_switch = (AppiumBy.ACCESSIBILITY_ID, '°C')

    def is_page_open(self):
        try:
            self.driver.find_element(*self._title)
        except NoSuchElementException:
            return False
        else:
            return True

    def go_back(self):
        self.driver.find_element(*self._back_button).click()

    def switch_to_celsius(self):
        self.driver.find_element(*self._celsius_switch).click()
