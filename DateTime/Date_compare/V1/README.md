📅 Date Checker v1
A Python utility that lets users input a date (with optional time) and checks whether that date has already passed or is still upcoming.
It uses timezone-aware datetime objects (Asia/Kolkata) and provides clear, colored console output using ANSI formatting.

📌 Features
- Prompt user for year, month, and day with validation.
- Optional input for hour and minute.
- Handles invalid inputs gracefully with error messages.
- Uses calendar.monthrange() to validate maximum days in a month.
- Compares the user-provided date with the current date/time.
- Outputs:
- ✅ If the date is upcoming → shows how much time is left.
- ❌ If the date has passed → shows that it’s already gone.
- ANSI-colored console messages for better readability.

🚀 Requirements
- Python 3.9+ (needed for zoneinfo)
- Libraries:
- datetime (built-in)
- calendar (built-in)
- zoneinfo (built-in from Python 3.9+)
- Ansi (custom ANSI formatting module)
⚠️ If you don’t have the Ansi module, you can replace it with colorama or remove the formatting.


📂 Project Structure
├── funcdate.py       # Contains is_date_passed() function
├── inputdatev1.py    # Contains input_date() function
├── main.py           # Entry point, imports and runs the functions



📝 Usage
- Clone or download this repository.
- Run the main script:
python KnowPassDatev1.py
- Enter:
- Year (YYYY)
- Month (1–12)
- Day (validated against month/year)
- Optionally: Hour (0–23) and Minute (0–59)

💻 Example Run
Date Today : 2025-11-27 19:15:00+05:30
Enter year (YYYY): 2025
Enter month (1-12): 12
Note : For the month 12 in year 2025 , maximum days can be 31
Enter day (1-31): 25
Optional : can provide Hour and Minute : (0 = Yes | 1 = No ) : 1
Date : 2025-12-25 00:00:00+05:30 has not passed yet and is 27 days, 4:45:00 away



⚡ Notes
- Timezone is fixed to Asia/Kolkata.
- Input validation ensures no invalid dates (e.g., Feb 30).
- If you skip hour/minute, the date defaults to midnight (00:00).
