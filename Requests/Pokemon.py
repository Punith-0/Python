import requests
import Ansi as an

url = "https://pokeapi.co/api/v2/"

def pokemon_data(Pokemon_name) -> dict[any , any]:
    URL = f"{url}pokemon/{Pokemon_name}"
    response = requests.get(URL)
    if (response.status_code == 200):
        return response.json()
    else:
        print(f"{an.RED}Error Occurred {response.status_code} {an.RESET}")
        return None

p_name :str = str(input("Enter Pokemon Name: ")).lower()
p_data = pokemon_data(p_name)
print(f"{an.GREEN}Name : {p_data['name']} {an.RESET}")
print(f"{an.GREEN}Height : {p_data['height']}{an.RESET}")
print(f"{an.GREEN}Pokedex id : {p_data['id']}{an.RESET}")
print(f"{an.GREEN}Type :  {[t['type']['name'] for t in p_data['types']]}{an.RESET}")
