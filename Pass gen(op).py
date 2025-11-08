import random
import string
def passgen(length:int , dig:bool = True , spec:bool = True)->None:
    lower_c = string.ascii_lowercase
    upper_c = string.ascii_uppercase
    digit = string.digits
    special_c = string.punctuation
    if(dig and spec):
        temp = lower_c + upper_c + digit + special_c
    elif(dig):
        temp = lower_c + upper_c + digit 
    elif(spec):
        temp = lower_c + upper_c + special_c
    else:
        temp = lower_c + upper_c
    try :
        if(length <= len(temp)):
            Password = "".join(random.sample(temp , length))
            print(f'Password :  {Password}')
    except ValueError:
        print(f"The max length of password u can have is {len(temp)}")
        print("Enter Length Again :")
        passgen(num() , dig , spec)
def num()->int :
    try :
        l = int(input("Enter the length of Password :"))
        return l ;
    except ValueError:
        print("Enter a valid intege number :")
        return 0
def isdig()-> bool :
    try :
        a = int(input("Do u want digits in ur password (0|1) :"))
        if a not in (0, 1):
            raise ValueError("Input muist be 0 or 1 .....")
        return bool(a);
    except ValueError:
        print("Default is true")
        return bool(1);
def isspecc() ->bool :
    try :
        a = int(input("Do u want special charcters in ur password (0|1) :"))
        if a not in (0, 1):
            raise ValueError("Input muist be 0 or 1 .....")
        return bool(a);
    except ValueError:
        print("Default is true")
        return bool(1);
def main():
    l = num()
    d = isdig()
    s = isspecc()
    if l> 0 :
        passgen(l , d ,s)
    else :
        print('Enter a valid number greater than zero')
main()