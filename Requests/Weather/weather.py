import Ansi as an 
from weatherdisplay import WeatherDisplay as wd
from API import Weather as w

def main() -> None :
    city : str = str(input("\nEnter the city :"))
    city = ''.join(city).strip()
    weather = w()
    data = weather.get_weather(city)
    display = wd(data)
    display.display_data()

if __name__ == "__main__" :
    main()