import random
import string
import Ansi as an
def passgen(length:int)->str:
    lower_c = string.ascii_lowercase
    upper_c = string.ascii_uppercase
    digit = string.digits
    special_c = string.punctuation
    temp = lower_c + upper_c + digit + special_c
    Password = "".join(random.choices(temp , k = length))
    return Password

def num()->int :
    try :
        l = int(input("Enter the length of Password :"))
        return l
    except ValueError:
        print(f"{an.BOLD}{an.RED}Enter a valid integer number :{an.RESET}")
        return 0

def main():
    l = num()
    if l> 0 :
        print(f'{an.GREEN}Password :{an.RESET} {passgen(l)}')
    else :
        print(f'{an.BOLD}{an.RED}Enter a valid number greater than zero{an.RESET}')

if __name__ == '__main__':
    main()