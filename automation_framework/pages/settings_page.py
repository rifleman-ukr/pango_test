from appium.webdriver.common.appiumby import AppiumBy
from selenium.common import NoSuchElementException

from automation_framework.conftest import driver


class SettingsPage:
    def __init__(self, driver):
        self.driver = driver
        self._title = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Settings")')
        self._customize_units_button = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Customize units")')
        self._back_button = (AppiumBy.ACCESSIBILITY_ID, 'Navigate up')

    def is_page_open(self):
        try:
            self.driver.find_element(*self._title)
        except NoSuchElementException:
            return False
        else:
            return True

    def go_back(self):
        self.driver.find_element(*self._back_button).click()

    def open_customize_units(self):
        self.driver.find_element(*self._customize_units_button).click()
