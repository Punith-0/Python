📅 Date Checker v2
A Python utility that allows users to input a date (with optional time) and checks whether that date has already passed or is still upcoming.
This is an improved version of v1, with modular input functions for year, month, day, and optional hour/minute, making the code more structured and reusable.

📌 Features
- Modular input functions:
- get_year() → validates year input.
- get_month() → validates month input.
- get_day(year, month) → validates day input based on month/year using calendar.monthrange().
- get_hour_minute() → optional hour/minute input with validation.
- Timezone-aware datetime using Asia/Kolkata.
- Validation & error handling:
- Ensures year > 0.
- Month between 1–12.
- Day within valid range for the given month/year.
- Hour between 0–23, minute between 0–59.
- Comparison logic:
- If the date has passed → prints a message.
- If the date is upcoming → shows how much time is left.
- ANSI-colored output for better readability.

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
├── inputdatev2.py    # Contains modular input functions and input_date()
├── KnowPassDatev2.py           # Entry point, imports and runs the functions



📝 Usage
- Clone or download this repository.
- Run the main script:
python KnowPassDatev2.py
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

⚡ Improvements in v2 over v1
- Modularized input handling (separate functions for year, month, day, hour/minute).
- Better error handling with clear retry prompts.
- Cleaner structure for easier maintenance and extension.
