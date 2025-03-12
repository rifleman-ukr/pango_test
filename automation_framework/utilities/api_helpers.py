
import json

import requests

from automation_framework.utilities.config import config


class ApiHelper:
    BASE_URL = config.get("API", "BASE_URL")
    API_KEY = config.get("API", "API_KEY")
    PARAMS = f"&units={config.get("API", "UNITS")}&lang={config.get("API", "LANG")}"

    def get_current_weather(self, data, method="q"):
        response = []
        if isinstance(data, str):
            data = [data]
        for city in data:
            _response = requests.get(f"{self.BASE_URL}weather?{method}={city}&appid={self.API_KEY}{self.PARAMS}")
            response.append(_response)
        return response

    def get_average_temperature(self, data, method="q"):
        response = requests.get(f"{self.BASE_URL}forecast?{method}={data}&appid={self.API_KEY}{self.PARAMS}")
        assert response.status_code == 200, "Status code should be 200"
        data = json.loads(response.text)
        _temperature = []
        for forecast in data["list"]:
            _temperature.append(forecast["main"]["temp"])
        return sum(_temperature) / len(_temperature)
