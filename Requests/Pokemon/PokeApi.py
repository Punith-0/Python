import requests
import Ansi as an
import datetime as dt
from zoneinfo import ZoneInfo as zn
from typing import Any

class Pokemon:
    
    def pokemon_data(self , url : str , Pokemon_name : str)  -> dict[str , Any] | None:
        URL = f"{url}pokemon/{Pokemon_name}"
        response = requests.get(URL)
        if (response.status_code == 200):
            print(f"{an.GREEN}API accessed : {self.date_time()}{an.RESET}")
            # print(f"{an.GREEN}API accessed : {response.headers['Date']} {an.RESET}")
            return response.json()
        else:
            print(f"{an.RED}Error Occurred {response.status_code} {an.RESET}")
            return None

    def date_time(self) -> str :
        date = dt.datetime.strftime(dt.datetime.now(tz = zn("Asia/Kolkata")) , "%a , %d-%b-%Y %H:%M:%S %Z")
        return date
    
    def format_data(self , data : dict[str, Any]) -> dict[str, Any]:
        # This method can be used to format or extract specific data if needed
        return data
