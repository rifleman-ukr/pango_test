from appium.webdriver.common.appiumby import AppiumBy
from selenium.common import NoSuchElementException


class SearchPage:
    def __init__(self, driver):
        self.driver = driver
        self._search_bar = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Search")')
        self._close_button = (AppiumBy.ACCESSIBILITY_ID, "Close the search screen")

    def is_page_open(self):
        try:
            self.driver.find_element(*self._search_bar)
        except NoSuchElementException:
            return False
        else:
            return True

    def close_search(self):
        self.driver.find_element(*self._close_button).click()

    def search_for(self, text):
        search_bar = self.driver.find_element(*self._search_bar)
        search_bar.click()
        search_bar.send_keys(text)
        self.driver.press_keycode(66)
        self.driver.find_elements(AppiumBy.XPATH, f"//*[contains(@text, '{text.capitalize()}')]")[0].click()
