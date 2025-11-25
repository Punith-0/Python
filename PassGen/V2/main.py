import passgen as pg
import Ansi as an

def main() -> None:
    len : int = int(input("Enter the length of the password : "))
    print(f"{an.HIGHLIGHT}{an.BOLD}Generated Password : \n{an.GREEN}{pg.passgen(len)} {an.RESET}")

if __name__ == "__main__":
    main()