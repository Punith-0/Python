import datetime as dt
from zoneinfo import ZoneInfo as zn
import Ansi as an
import calendar as cal

def get_year() -> int:
    while True :
        try:
            year : int = int(input("Enter year (YYYY): "))
            if year < 1:
                raise ValueError(f'{an.RED}{an.BOLD}Year must be a postive integer{an.RESET}')
            return year
        except ValueError as e:
            print(f"{an.RED}Invalid input: {e}. Please try again.{an.RESET}")



def get_month() -> int :
    while True :
        try:
            month : int = int(input("Enter month (1 -12): "))
            if month < 1 or month >12 :
                raise ValueError(f'{an.RED}{an.BOLD}Month must be a between 1 and 12{an.RESET}')
            return month
        except ValueError as e:
            print(f"{an.RED}Invalid input: {e}. Please try again.{an.RESET}")


def get_day(year : int , month :int) -> int:
    m_d = cal.monthrange(year , month)[1]
    print(f"{an.HIGHLIGHT}Note : For the month {month} in year {year} , maximum days can be {m_d} {an.RESET}")
    while True :
        try:
            day : int = int(input(f"Enter day (1-{m_d}): "))
            if day < 1 or day > m_d :
                raise ValueError(f'{an.RED}{an.BOLD}Day must be between 1 and {m_d}{an.RESET}')
            return day
        except ValueError as e:
            print(f"{an.RED}Invalid input: {e}. Please try again.{an.RESET}")

def get_hour_minute() -> list[int] | None:
    while True :
        try :
            ui : int = int(input(f"{an.BOLD}Optional : can provide Hour and Minute : ({an.GREEN}0 = Yes | {an.RED} 1= No ) :{an.RESET} "))
            if ui == 0:
                while True :
                    try :
                        hour : int = int(input('Enter hour (0-23): '))
                        if not 0 <= hour <= 23:
                            raise ValueError("Hour must be between 0 and 23")
                        break
                    except ValueError as e:
                            print(f"{an.RED}Invalid input: {e}. Please try again.{an.RESET}")
                while True :
                    try :
                        minute : int = int(input('Enter minute (0-59): '))
                        if not 0 <= minute <= 59:
                            raise ValueError("Minute must be between 0 and 59")
                        break
                    except ValueError as e:
                            print(f"{an.RED}Invalid input: {e}. Please try again.{an.RESET}")
                return [hour , minute]
            elif ui == 1 :
                return None
            else :
                raise ValueError(f'{an.RED}{an.BOLD}Invalid choice for hour and minute input{an.RESET}')
        except ValueError as e:
            print(f"{an.RED}Invalid input: {e}. Please try again.{an.RESET}")

def input_date() -> dt.datetime:
    year : int = get_year()
    month : int = get_month()
    day : int = get_day(year , month)
    hour_minute = get_hour_minute()
    if hour_minute :
        date_user : dt.datetime = dt.datetime(year , month , day  , hour_minute[0] , hour_minute[1] , tzinfo =zn('Asia/Kolkata'))
        return date_user
    else :
        date_user : dt.datetime = dt.datetime(year , month , day , tzinfo =zn('Asia/Kolkata'))
        return date_user
    
if __name__ == '__main__' :
    pass
    #DO nothinh as its a function class were gonna import it
                    
