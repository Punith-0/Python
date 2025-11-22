import datetime as dt
from zoneinfo import ZoneInfo as zn
import Ansi as an

def is_date_passed(date_now : dt.datetime , date_user : dt.datetime ) -> None:
    if date_user < date_now :
        print(f"{an.BOLD}{an.RED}Date : {date_user} has already passed{an.RESET}")
    else :
        print(f"{an.GREEN }{an.BOLD}Date : {date_user} has not passed yet and is {an.RED}{date_user - date_now} {an.GREEN}away{an.RESET}")

if __name__ == "__main__":
    pass
    # date_now : dt.datetime = dt.datetime.now(tz = zn('Asia/Kolkata'))
    # date_user : dt.datetime = dt.datetime(2023, 12, 25, tzinfo=zn('Asia/Kolkata')) 
    # #Demo date ; Never gonna use in the main function just for testing purpose
    # is_date_passed(date_now , date_user) ;

   
# Do nothing as its a function class were gonna import it