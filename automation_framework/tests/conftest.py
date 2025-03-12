import pytest

from automation_framework.pages.location_popup import LocationPopup
from automation_framework.pages.main_page import MainPage
from automation_framework.pages.settings_page import SettingsPage
from automation_framework.pages.units_page import UnitsPage


@pytest.fixture(scope="module")
def location_popup(driver):
    return LocationPopup(driver)

@pytest.fixture(scope="module")
def main_page(driver):
    return MainPage(driver)

@pytest.fixture(scope="module")
def settings_page(driver):
    return SettingsPage(driver)

@pytest.fixture(scope="module")
def units_page(driver):
    return UnitsPage(driver)
