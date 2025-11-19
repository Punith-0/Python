import requests
import Ansi as an


url = "https://pokeapi.co/api/v2/"


def pokemon_data(Pokemon_name : str)  -> dict[str , any]:
    URL = f"{url}pokemon/{Pokemon_name}"
    response = requests.get(URL)
    if (response.status_code == 200):
        print(f'{an.GREEN}API accessed : {response.headers['Date']} {an.RESET}')
        return response.json()
    else:
        print(f"{an.RED}Error Occurred {response.status_code} {an.RESET}")
        return None
    
