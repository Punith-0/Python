import Ansi as an
import datetime as dt
from zoneinfo import ZoneInfo as zn
from typing import Any

class WeatherDisplay :
    def __init__(self , weather_data : dict[str , Any]) -> None:
        self.data = weather_data 

    def display_data(self) -> None:
        try:
            if self.data is None:
                print(f"{an.RED}No weather data to display.\nCheck city name \n\n{an.RESET}")
                return

            print(f"\n{an.BOLD}Date : {an.RESET}{dt.datetime.now().strftime('%d-%m-%Y')}")
            print(f"{an.BOLD}Country : {an.RESET}{self.data['sys']['country']}")
            print(f"{an.BOLD} Weather in {an.HIGHLIGHT}{an.GREEN}{self.data['name']} {an.RESET}")
            print(f"{an.BOLD}Temperature : {an.RESET}{self.data['main']['temp']}°C")
            print(f"{an.BOLD}Humidity : {an.RESET}{self.data['main']['humidity']}%")
            print(f"{an.BOLD}Visibility : {an.RESET}{self.data['visibility']/1000} km")
            print(f"{an.GREEN}\nDone for the day .......{an.RESET}\n\n\n")

        except KeyError as ke:
            print(f"{an.RED}Key error occurred while displaying data: {ke}{an.RESET}")

            


