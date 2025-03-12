import json

import pytest


@pytest.mark.parametrize("city", ["kyiv", ("kyiv", "lviv")])
def test_get_weather_data(api, db, city):
    weather = api.get_current_weather(city)
    for item in weather:
        assert item.status_code == 200, "Status code should be 200"

        data = json.loads(item.text)
        db.insert_weather_data(city=data["name"],
                               temperature=data['main']['temp'],
                               feels_like=data['main']['feels_like'])
        stored_temp = db.get_weather_data(data["name"])

        assert stored_temp["temperature"] == data["main"]["temp"], \
            "Stored temperature should be same as in response"
        assert stored_temp["feels_like"] == data["main"]["feels_like"], \
            "Stored feels like temperature should be same as in response"

@pytest.mark.parametrize("city_id", ["703448", ("703448", "702550")])
def test_get_weather_by_id(api, db, city_id):
    weather = api.get_current_weather(city_id, method='id')
    for item in weather:
        assert item.status_code == 200, "Status code should be 200"

        data = json.loads(item.text)
        db.insert_weather_data(city=data["name"],
                               temperature=data['main']['temp'],
                               feels_like=data['main']['feels_like'],
                               average=api.get_average_temperature(data["name"]))
        stored_temp = db.get_weather_data(data["name"])

        assert stored_temp["temperature"] == data["main"]["temp"], \
            "Stored temperature should be same as in response"
        assert stored_temp["feels_like"] == data["main"]["feels_like"], \
            "Stored feels like temperature should be same as in response"
        assert stored_temp["average"] == api.get_average_temperature(data["name"]), \
            "Stored feels like temperature should be same as in response"

        hot_city = db.get_hot_city()
        print(f"Highest average stored temperature is {hot_city[1]}° in {hot_city[0]}")

