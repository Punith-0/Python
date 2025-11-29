import requests 
import Ansi as an 

class Weather:
    key = '02a0adfbb3cfd673c7ab1b58163c72f3'
    url = f'http://api.openweathermap.org/data/2.5/weather/'

    def get_weather(self , city : str) -> dict[str , Any] | None :
        URL = f"{self.url}?q={city}&appid={self.key}&units=metric"
        
        tries = 3
        for attempt in range(1 , tries + 1):
            r = requests.get(URL , timeout=10)
            try :
                if r.status_code == 200 :
                    print(f"{an.GREEN}\nAPI Accessed Successfully{an.RESET}")
                    return r.json()
            except requests.exceptions.Timeout as te :
                print(f"{an.RED}Attempt {attempt} of {tries} failed: Timeout occurred {te}.{an.RESET}")
            except requests.exceptions.RequestException as re :
                print(f"{an.RED}Attempt {attempt} of {tries} failed: {re}{an.RESET}")
            except request.exceptions.HTTPError as he :
                print(f"{an.RED}Attempt {attempt} of {tries} failed: HTTP error occurred - {he}{an.RESET}")
        else :
            print(f"{an.RED}\n\nAll attempts to access the API have failed.{an.RESET}")
            return None
            
if __name__ == "__main__" :
    pass
