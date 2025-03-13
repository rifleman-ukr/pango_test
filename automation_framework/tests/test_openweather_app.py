import pytest
from automation_framework.config.test_data import TestData

def test_configure_celsius(driver, location_popup, main_page, settings_page, units_page):
    if location_popup.is_popup_displayed():
        location_popup.allow_while_using()

    assert main_page.is_page_open(), "Main page should be open"
    main_page.open_settings()
    assert settings_page.is_page_open(), "Settings page should be open"
    settings_page.open_customize_units()
    assert units_page.is_page_open(), "Units page should be open"
    units_page.switch_to_celsius()
    units_page.go_back()
    assert settings_page.is_page_open(), "Settings page should be open"
    settings_page.go_back()
    assert main_page.is_page_open(), "Main page should be open"
    assert main_page.is_temp_in_celsius(), "Temperature should be in celsius"

@pytest.mark.parametrize("city", TestData.cities)
def test_comparative_temperature_analysis(city, db, driver, main_page):
    assert main_page.is_page_open(), "Main page should be open"
    main_page.choose_city(city)
    assert main_page.is_city_displayed(city), f"Weather for {city} should be displayed"
    app_temp = main_page.get_celsius_temp()
    db_temp = db.get_weather_data(city)["temperature"]
    db.update_weather_data(city=city,
                           app_temp=app_temp)
    assert round(db_temp) == app_temp, f"App temperature is {app_temp} while {db_temp} stored from API call"

