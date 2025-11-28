import PokeApi as pa
import Ansi as an

def main() -> None :
    po = pa.Pokemon()
    print()
    p_name :str = str(input("Enter Pokemon Name: ")).lower().strip()
    p_data = po.pokemon_data("https://pokeapi.co/api/v2/" , p_name)
    if p_data :
        print(f"{an.BOLD}{an.GREEN}  POKEDEX OPEN  {an.RESET}")
        print(f"\t{an.GREEN}Name : {p_data['name'].capitalize()} {an.RESET}")
        print(f"\t{an.GREEN}Height : {p_data['height']}{an.RESET}")
        print(f"\t{an.GREEN}Pokedex id : {p_data['id']}{an.RESET}")
        types = ", ".join([t['type']['name'] for t in p_data['types']])
        print(f"\t{an.GREEN}Type : {types}{an.RESET}")
        print(f"{an.BOLD}{an.GREEN}  POKEDEX CLOSE {an.RESET}")
    else :
        print(f"{an.RED}No Data Found for the Pokemon : {p_name}{an.RESET}")

if __name__ == '__main__':
    main()