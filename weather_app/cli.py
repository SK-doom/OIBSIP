import os
import sys
from weather_app.weather import fetch_current_weather, WeatherError


def main():
    """Command-line entrypoint for the weather app."""
    if len(sys.argv) > 1:
        location = " ".join(sys.argv[1:])
    else:
        location = input("Enter a city name or ZIP code: ").strip()

    if not location:
        print("No location provided, exiting.")
        sys.exit(1)

    api_key = os.environ.get("OWM_API_KEY")

    try:
        data = fetch_current_weather(location, api_key)
    except WeatherError as exc:
        print(f"Error: {exc}")
        sys.exit(1)

    # display a subset of fields
    name = data.get("name")
    main = data.get("main", {})
    weather_desc = ", ".join(w["description"] for w in data.get("weather", []))

    print(f"Weather for {name}:")
    print(f"  Condition: {weather_desc}")
    print(f"  Temperature: {main.get('temp')}°C")
    print(f"  Humidity: {main.get('humidity')} %")


if __name__ == "__main__":
    main()
