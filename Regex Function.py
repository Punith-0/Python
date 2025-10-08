# THIS PYTHON CODE IS A SEMI AUTOMATED REGEX MATCHER WITH CUSTOM OR DEFAULT PATTERN
# INCLUDED FUNCTIONS SUCH AS 'MATCH', 'SEARCH' AND 'FINDALL'
# NOTE: NO r STRING IS REQUIRED WHILE THE PATTERN INPUT — IT CAN AUTO COMPILE THE PATTERN

# IMPORTING THE PACKAGES USED IN THE FULFILMENT OF THE PROJECT
import re

# THE ANSI SEQUENCE FOR THE OUTPUT CUSTOMISATION
RESET = "\033[0m"
GREEN = "\033[32m"
RED = "\033[31m"
HIGHLIGHT = "\033[7m"
BOLD = "\033[1m"

# CUSTOM PATTERN CODE BLOCK
def pattern1():
    k = input("Enter a pattern: ")
    try:
        return re.compile(k)
    except re.error:
        return None

# PRE DEFINED PATTERN CODE BLOCK
def pattern2():
    return re.compile(r"^[Aa].*[Zz]$")

# MATCH SEQUENCE USER DEFINED FUNCTION
def match(pat):
    TEXT = str(input('Enter text to match: '))
    if pat is None:
        print("Invalid pattern")
        exit()
    else:
        print('Matching to the pattern...')
        res = pat.match(TEXT)
        if res:
            print(f'{GREEN}{BOLD}{HIGHLIGHT}The pattern is matched.{RESET}')
        else:
            print(f'{RED}{BOLD}{HIGHLIGHT}Pattern does not match.{RESET}')
    x = int(input('Want to do more matching (0.YES | 1.NO): '))
    if x == 0:
        main()
    else:
        print('Exiting...')
        exit()

# FINDALL SEQUENCE USER DEFINED FUNCTION
def find(pat):
    TEXT = str(input('Enter some text to match: '))
    if pat is None:
        print("Invalid pattern")
        exit()
    else:
        print('Matching to the pattern...')
        res = pat.findall(TEXT)
        if res:
            print(f'{GREEN}{BOLD}{HIGHLIGHT}The pattern is found.\n{res}{RESET}')
        else:
            print(f'{RED}{BOLD}{HIGHLIGHT}Pattern is not found.{RESET}')
    x = int(input('Find more items in the pattern (0.YES | 1.NO): '))
    if x == 0:
        main()
    else:
        print('Exiting...')
        exit()

# SEARCH SEQUENCE USER DEFINED FUNCTION
def search(pat):
    TEXT = str(input('Enter some text to match: '))
    if pat is None:
        print("Invalid pattern")
        exit()
    else:
        print('Matching to the pattern...')
        res = pat.search(TEXT)
        if res:
            print(f'{GREEN}{BOLD}{HIGHLIGHT}The pattern is searched: {res.group()}.{RESET}')
        else:
            print(f'{RED}{BOLD}{HIGHLIGHT}Pattern not available.{RESET}')
    x = int(input('Initiate more search algorithm (0.YES | 1.NO): '))
    if x == 0:
        main()
    else:
        print('Exiting...')
        exit()

# MAIN FUNCTION 'CONTROLS EVERYTHING IN THE PROGRAM'
def main():
    st = int(input("Enter 0 to start or 1 to exit: "))
    ch = int(input("1.Match\n2.Search\n3.Findall\nChoose: "))
    pa = int(input('Enter\n0 -> Custom Pattern\n1 -> Default Pattern "^[Aa].*[Zz]$"\nChoose: '))
    
    if pa == 0:
        pat = pattern1()
    else:
        pat = pattern2()
    
    if st == 0:
        if ch == 1:
            match(pat)
        elif ch == 2:
            search(pat)
        else:
            find(pat)
    else:
        print("Exiting...")
        exit()

# FUNCTION CALL TO START EXECUTING THE PROGRAM
main()
