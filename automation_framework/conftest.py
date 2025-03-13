import os

import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options

from automation_framework.utilities.api_helpers import ApiHelper
from automation_framework.utilities.config import config
from automation_framework.utilities.db_helpers import DatabaseHelper


@pytest.fixture(scope="module")
def api():
    return ApiHelper()

@pytest.fixture(scope="module")
def db():
    database = DatabaseHelper()
    database.create_tables()
    yield database
    database.terminate_db()

@pytest.fixture(scope="session")
def driver():
    desired_capabilities = {
        "platformName": config.get("ANDROID", "PLATFORM"),
        "deviceName": config.get("ANDROID", "DEVICE"),
        "automationName": config.get("ANDROID", "AUTOMATION"),
        "app": os.path.join(os.getcwd(), "../../OpenWeather_1.1.7_APKPure.apk")
    }
    options = UiAutomator2Options().load_capabilities(desired_capabilities)
    driver = webdriver.Remote(f'http://localhost:{config.get("ANDROID", "PORT")}', options=options)
    driver.implicitly_wait(5000)
    yield driver
    driver.quit()