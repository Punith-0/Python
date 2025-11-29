🌦 Weather CLI Application
A simple Python command-line application that fetches and displays real-time weather data using the OpenWeatherMap API.
The app highlights key weather details like temperature, humidity, visibility, and location, with styled console output using ANSI escape codes.

📂 Project Structure
.
├── API.py              # Contains Weather class for API requests
├── weatherdisplay.py   # Contains WeatherDisplay class for formatted output
├── weather.py             # Entry point of the application
├── Ansi.py             # ANSI color/style codes for terminal output



⚙️ Features
- Fetches live weather data from OpenWeatherMap API.
- Displays:
- Current date
- Country
- City name
- Temperature (°C)
- Humidity (%)
- Visibility (km)
- Handles errors gracefully (e.g., invalid city names, API failures).
- Styled output with ANSI colors for better readability.

🚀 Usage
- Clone the repository:
git clone https://github.com/Punith-0/Weather.git
cd weather-cli
- Install dependencies:
pip install requests
- Run the application:
python main.py
- Enter a city name when prompted:
Enter the city : Bengaluru



🖥️ Example Output
Date : 29-11-2025
Country : IN
Weather in Bengaluru
Temperature : 20.51°C
Humidity : 70%
Visibility : 4.0 km

Done for the day .......



🌍 Sample API Response
Here’s a sample JSON response from OpenWeatherMap for Bengaluru:
{
  "base": "stations",
  "clouds": {"all": 40},
  "cod": 200,
  "coord": {"lat": 12.9762, "lon": 77.6033},
  "dt": 1764336991,
  "id": 1277333,
  "main": {
    "feels_like": 20.44,
    "grnd_level": 916,
    "humidity": 70,
    "pressure": 1014,
    "sea_level": 1014,
    "temp": 20.51,
    "temp_max": 20.83,
    "temp_min": 19.9
  },
  "name": "Bengaluru",
  "sys": {
    "country": "IN",
    "id": 2036502,
    "sunrise": 1764291278,
    "sunset": 1764332445,
    "type": 2
  },
  "timezone": 19800,
  "visibility": 4000,
  "weather": [
    {"description": "haze", "icon": "50n", "id": 721, "main": "Haze"}
  ],
  "wind": {"deg": 24, "gust": 16.99, "speed": 6.71}
}



🛠️ Requirements
- Python 3.10+
- requests library
- OpenWeatherMap API key (replace the placeholder in API.py)
