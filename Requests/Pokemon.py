import requests
import Ansi as an
import PokeApi as pa

def main() -> None :
    p_name :str = str(input("Enter Pokemon Name: ")).lower().strip()
    p_data = pa.pokemon_data(p_name)
    if p_data :
        print(f"{an.GREEN}Name : {p_data['name']} {an.RESET}")
        print(f"{an.GREEN}Height : {p_data['height']}{an.RESET}")
        print(f"{an.GREEN}Pokedex id : {p_data['id']}{an.RESET}")
        print(f"{an.GREEN}Type :  {[t['type']['name'] for t in p_data['types']]}{an.RESET}")
    else :
        print(f"{an.RED}No Data Found for the Pokemon :{p_name}{an.RESET}")

if __name__ == '__main__':
    main()