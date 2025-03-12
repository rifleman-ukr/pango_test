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

def test_comparative_temperature_analysis():
    pass
