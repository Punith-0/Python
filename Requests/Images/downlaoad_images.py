import requests
from requests.exceptions import Timeout
import Ansi as an

def main() -> None :
    url = str(input("Enter Images url from the web : "))
    url = "".join(url.strip())
    name : str = input("Enter name of the image with extenssion(png , jpg , jpeg) : ")
    s = download_image(url , name)
    if s :
        print(f"{an.GREEN}{an.BOLD}Image downloaded successfully in your project folder.{an.RESET}")
    else :
        print(f"{an.HIGHLIGHT}{an.BOLD}{an.RED}RETRY{an.RESET}")

def download_image(url: str , name : str) -> bool  :
    tries : int = 3
    success : bool = False
    for attempt in range(1 , tries + 1):
        try:
            r = requests.get(url , timeout = 2)
            with open(name , "wb") as f:
                # print(r.content)
                f.write(r.content)
            success = True
            return success
            
        except Timeout as te:
            print(f"{an.RED}Attempt {attempt} Request timed out -> {te}{an.RESET}")
        except Exception as e :
            print(f"Attempt {attempt} An error occured {e}{an.RESET}")
            print(f"{an.RED}Chaeck the url and try again.{an.RESET}")
    else:
        print(f"{an.RED}All attempts to download the image have failed.{an.RESET}")
        return success

if __name__ == "__main__":
    main()
        