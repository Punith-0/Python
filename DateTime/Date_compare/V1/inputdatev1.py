import datetime as dt
from zoneinfo import ZoneInfo as zn
import Ansi as an
import calendar as cal

def input_date() -> dt.datetime:
    while True :
        try:
            year : int = int(input("Enter year (YYYY): "))
            if year < 1:
                raise ValueError(f'{an.RED}{an.BOLD}Year must be a postive integer{an.RESET}')
            
            month : int = int(input("Enter month (1-12): "))
            if month < 1 or month >12 :
                raise ValueError(f'{an.RED}{an.BOLD}Month must be between 1 and 12{an.RESET}')
            
            m_d = cal.monthrange(year , month)[1]
            print(f"{an.HIGHLIGHT}Note : For the month {month} in year {year} , maximum days can be {m_d} {an.RESET}")  
            day : int = int(input(f"Enter day (1-{m_d}): "))
            if day < 1 or day > m_d :
                raise ValueError(f'{an.RED}{an.BOLD}Day must be between 1 and {m_d}{an.RESET}')
            
        # day automaticaaly handled by the datetime module but runs in an infinite loop without any message
            ui: int = int(input(f"{an.BOLD}Optional : can provide Hour and Minute : ({an.GREEN}0 = Yes | {an.RED} 1= No ) :{an.RESET} "))
            if ui == 0 :
                hour = int(input("Enter hour (0-23): "))
                if not 0 <= hour <= 23:
                    raise ValueError("Hour must be between 0 and 23")

                minute = int(input("Enter minute (0-59): "))
                if not 0 <= minute <= 59:
                    raise ValueError("Minute must be between 0 and 59")
                date_user : dt.datetime = dt.datetime(year , month , day , hour , minute , tzinfo = zn('Asia/Kolkata'))
                return date_user
            elif ui == 1:
                date_user : dt.datetime = dt.datetime(year , month , day , tzinfo = zn('Asia/Kolkata'))
                return date_user
            else :
                raise ValueError(f'{an.RED}{an.BOLD}Invalid choice for hour and minute input{an.RESET}')

        except ValueError as ve:
            print(f"{an.RED}Invalid input: {ve}. Please try again.{an.RESET}")

if __name__ == "__main__":
    pass
    #DO nothinh as its a function class were gonna import it 