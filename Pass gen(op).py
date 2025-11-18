import random
import string
import Ansi as an
def passgen(length:int , dig:bool = True , spec:bool = True)->str:
    lower_c = string.ascii_lowercase
    upper_c = string.ascii_uppercase
    digit = string.digits
    special_c = string.punctuation
    temp = lower_c + upper_c
    if(dig and spec):
        temp += digit + special_c
    elif(dig):
        temp  += digit
    elif(spec):
        temp += special_c
    else:
        temp
    Password = ''.join(random.choices(temp , k = length))
    return Password

def num()->int :
    try :
        l : int = int(input("Enter the length of Password :"))
        return l ;
    except ValueError:
        print(f"{an.RED}Enter a valid integer number :{an.RESET}")
        return 0

def isdig()-> bool :
    try :
        a :int = int(input("Do u want digits in ur password (0|1) :"))
        if a not in (0, 1):
            raise ValueError(f"{an.RED}Input must be 0 or 1 ....{an.RESET}")
        return bool(a);
    except ValueError:
        print(f"{an.GREEN}Default is true{an.RESET}")
        return True

def isspecc() ->bool :
    try :
        a : int = int(input("Do u want special charcters in ur password (0|1) :"))
        if a not in (0, 1):
            raise ValueError(f"{an.RED}Input muist be 0 or 1 ....{an.RESET}.")
        return bool(a);
    except ValueError:
        print(f"{an.GREEN}Default is true{an.RESET}")
        return True

def main():
    l = num()
    d = isdig()
    s = isspecc()
    if l> 0 :
        print(f'{an.GREEN}Password :{an.RESET} {passgen(l , d ,s)}')
    else :
        print(f'{an.BOLD}{an.RED}Enter a valid number greater than zero{an.RESET}')

if __name__ == '__main__':
    main()