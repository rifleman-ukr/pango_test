from appium.webdriver.common.appiumby import AppiumBy
from selenium.common import NoSuchElementException
from automation_framework.conftest import driver


class MainPage:
    def __init__(self, driver):
        self.driver = driver
        self._search_bar = (AppiumBy.ACCESSIBILITY_ID, "Search")
        self._settings_button = (AppiumBy.ACCESSIBILITY_ID, "Go to settings")
        self._celsius_temp = (AppiumBy.XPATH, "//*[contains(@text, '°C')]")

    def is_page_open(self):
        try:
            self.driver.find_element(*self._search_bar)
        except NoSuchElementException:
            return False
        else:
            return True

    def open_settings(self):
        self.driver.find_element(*self._settings_button).click()

    def is_temp_in_celsius(self):
        try:
            self.driver.find_element(*self._celsius_temp)
        except NoSuchElementException:
            return False
        else:
            return True
