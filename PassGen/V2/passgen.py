import secrets
import string 

def passgen(len :int) ->str :
    l_c : str = string.ascii_lowercase 
    u_c : str = string.ascii_uppercase
    dig : str = string.digits
    s_c : str = string.punctuation 
    temp = l_c + u_c + dig + s_c
    Password : str = ''.join(secrets.choice(temp) for _ in range(len))
    print(Password)
    return Password

if __name__ == "__main__":
    passgen(12)
