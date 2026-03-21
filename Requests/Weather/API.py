import requests 
import Ansi as an 
import os
from dotenv import load_dotenv
from typing import Any
load_dotenv()

class Weather:
    key = os.getenv("W_key")
    url = os.getenv("W_API")


    def get_weather(self, city: str) -> dict[str, Any] | None:
        URL = f"{self.url}?q={city}&appid={self.key}&units=metric"

        tries = 3

        for attempt in range(1, tries + 1):
            try:
                r = requests.get(URL, timeout=10)
                data = r.json()

                if r.status_code == 200 and data.get("cod") == 200:
                    print(f"{an.GREEN}\nAPI Accessed Successfully{an.RESET}")
                    return data

                elif r.status_code == 401:
                    print(f"{an.RED}Invalid API key!{an.RESET}")
                    return None

                else:
                    print(f"{an.RED}API Error: {data.get('message')}{an.RESET}")
                    return None

            except requests.exceptions.Timeout as te:
                print(f"{an.RED}Attempt {attempt}: Timeout → {te}{an.RESET}")

            except requests.exceptions.ConnectionError as ce:
                print(f"{an.RED}Attempt {attempt}: Connection Error → {ce}{an.RESET}")

            except requests.exceptions.RequestException as re:
                print(f"{an.RED}Attempt {attempt}: {re}{an.RESET}")

        print(f"{an.RED}\nAll attempts to access the API have failed.{an.RESET}")
        return None
            
if __name__ == "__main__" :
    pass
