import random
import string
def passgen(length:int)->None:
    lower_c = string.ascii_lowercase
    upper_c = string.ascii_uppercase
    digit = string.digits
    special_c = string.punctuation
    temp = lower_c + upper_c + digit + special_c
    # print(len(temp))
    try :
        if(length <= len(temp)):
            Password = "".join(random.choice(temp , length))
            print(f'Password :  {Password}')
    except ValueError:
        print(f"The max length of password u can have is {len(temp)}")
        print("Enter Length Again :")
        passgen(num())
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
main()