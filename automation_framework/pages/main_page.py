from appium.webdriver.common.appiumby import AppiumBy
from selenium.common import NoSuchElementException
from automation_framework.pages.search_page import SearchPage


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

    def choose_city(self, city):
        self.driver.find_element(*self._search_bar).click()
        search_page = SearchPage(self.driver)
        assert search_page.is_page_open(), "Search page should be open"
        search_page.search_for(city)

    def is_city_displayed(self, city):
        if self.driver.find_elements(AppiumBy.XPATH, f"//*[contains(@text, '{city.capitalize()}')]"):
            return True
        else:
            return False

    def get_celsius_temp(self):
        return int(self.driver.find_elements(*self._celsius_temp)[0].text.replace("°C", ""))
