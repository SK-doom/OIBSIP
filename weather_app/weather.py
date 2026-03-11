import os
import requests

class WeatherError(Exception):
    """Custom exception for weather retrieval issues."""


def fetch_current_weather(location: str, api_key: str) -> dict:
    """Query the OpenWeatherMap API for current weather data.

    ``location`` may be a city name or ZIP code. ``api_key`` is required and
    normally pulled from an environment variable.

    Returns a dictionary with the relevant data or raises ``WeatherError`` on
    failure.
    """

    if not api_key:
        raise WeatherError("API key is missing. Set the OWM_API_KEY environment variable.")

    # Decide whether location looks like a ZIP code (all digits) or a city name
    payload = {"appid": api_key, "units": "metric"}
    if location.isdigit():
        payload["zip"] = location
    else:
        payload["q"] = location

    url = "https://api.openweathermap.org/data/2.5/weather"
    try:
        resp = requests.get(url, params=payload, timeout=10)
        data = resp.json()
    except requests.RequestException as exc:
        # network-level failures (DNS, timeout, etc.)
        raise WeatherError("Network error retrieving weather data") from exc
    except ValueError as exc:
        # invalid JSON
        raise WeatherError("Received malformed response from weather service") from exc

    # even if the HTTP status is not 200 we may still get JSON with an error
    status = getattr(resp, "status_code", None)
    if status is not None and status != 200:
        msg = data.get("message", "unknown error")
        raise WeatherError(f"API error: {msg}")

    if data.get("cod") != 200:
        msg = data.get("message", "unknown error")
        raise WeatherError(f"API error: {msg}")

    return data
