import random
import string
def passgen(length:int)->str:
    lower_c = string.ascii_lowercase
    upper_c = string.ascii_uppercase
    digit = string.digits
    special_c = string.punctuation
    temp = lower_c + upper_c + digit + special_c
    Password = "".join(random.choices(temp , k = length))
    print(f'Password :  {Password}')
    return Password

def num()->int :
    try :
        l = int(input("Enter the length of Password :"))
        return l ;
    except ValueError:
        print("Enter a valid integer number :")
        return 0

def main():
    l = num()
    if l> 0 :
        passgen(l)
    else :
        print('Enter a valid number greater than zero')

if __name__ == '__main__':
    main()