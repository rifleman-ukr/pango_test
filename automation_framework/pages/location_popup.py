from selenium.common import NoSuchElementException

from appium.webdriver.common.appiumby import AppiumBy

class LocationPopup:
    def __init__(self, driver):
        self.driver = driver
        self._popup_locator = (AppiumBy.ID, "com.android.permissioncontroller:id/grant_dialog")
        self._allow_while_using_button_locator = (AppiumBy.ID, "com.android.permissioncontroller:id/permission_allow_foreground_only_button")
        self._allow_now_button_locator = (AppiumBy.ID, "com.android.permissioncontroller:id/permission_allow_one_time_button")
        self._dont_allow_button_locator = (AppiumBy.ID, "com.android.permissioncontroller:id/permission_deny_button")

    def is_popup_displayed(self):
        try:
            self.driver.find_element(*self._popup_locator)
        except NoSuchElementException:
            return False
        else:
            return True

    def allow_while_using(self):
        self.driver.find_element(*self._allow_while_using_button_locator).click()