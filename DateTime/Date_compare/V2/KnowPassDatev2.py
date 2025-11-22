import datetime as dt
from zoneinfo import ZoneInfo as zn
import Ansi as an
import calendar as cal
from inputdatev2 import input_date
from funcdate import is_date_passed

def main() -> None:
    date_now :dt.datetime = dt.datetime.now(tz = zn('Asia/Kolkata')) # aware datetime object
    print(f"Date Today :{an.GREEN}{an.BOLD}{date_now}{an.RESET}")
    date_user : dt.datetime = input_date()
    is_date_passed(date_now , date_user)

if __name__ == "__main__":
    main()