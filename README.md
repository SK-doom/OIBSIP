## Basic Weather App

A simple command-line Python application that fetches current weather data for a
user-specified location using the OpenWeatherMap API. Designed for beginners to
learn about API integration, user input handling, and error handling.

### Setup

1. Create a Python virtual environment and activate it:
   ```sh
   python -m venv venv
   venv\Scripts\activate    # Windows
   ```
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
3. Obtain an API key from [OpenWeatherMap](https://openweathermap.org/)
   and set it in your environment:
   ```sh
   set OWM_API_KEY=your_api_key_here   # PowerShell/cmd
   ```

### Usage

Run the CLI with a location argument or enter it when prompted:

```sh
python -m weather_app.cli London
```  
or:
```sh
python -m weather_app.cli
# then type a city name or ZIP code when asked
```

The app will display temperature, humidity, and general conditions.

### Running tests

A rudimentary pytest suite is provided. Install pytest:

```sh
pip install pytest
```

and run:

```sh
python -m pytest
```

The tests exercise error handling logic without hitting the real API.
