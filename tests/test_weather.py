import os
import pytest
import requests
from weather_app.weather import fetch_current_weather, WeatherError


def test_missing_api_key():
    with pytest.raises(WeatherError):
        fetch_current_weather("London", api_key="")


def test_invalid_location(monkeypatch):
    # simulate an API response with an error code
    class DummyResponse:
        def __init__(self, json_data, status_code=404):
            self._json = json_data
            self.status_code = status_code

        def json(self):
            return self._json

    def fake_get(*args, **kwargs):
        return DummyResponse({"cod": 404, "message": "city not found"})

    monkeypatch.setattr("requests.get", fake_get)

    with pytest.raises(WeatherError) as excinfo:
        fetch_current_weather("Nowhere", api_key="fake")
    assert "city not found" in str(excinfo.value)
