🔐 Secure Password Generator
A simple Python script that generates strong, random passwords using the secrets module.
It supports lowercase, uppercase, digits, and punctuation, and prints the result with ANSI-colored formatting.

📌 Features
- Cryptographically secure password generation (secrets module).
- Supports all character sets:
- Lowercase letters
- Uppercase letters
- Digits
- Special characters (punctuation)
- Shuffles characters for extra randomness.
- Colored console output using a custom Ansi module.

🚀 Requirements
- Python 3.8+
- Libraries:
- secrets (built-in)
- string (built-in)
- Ansi (custom ANSI formatting module)
⚠️ If you don’t have the Ansi module, you can replace it with colorama or remove the formatting.


📂 Usage
- Clone or download this repository.
- Run the script:
python3 main.py
- Enter the desired password length when prompted.

📝 Example
Enter the length of the password : 12
Generated Password :
aB9$zQ!mX@2f



⚡ Notes
- The password length is user-defined. For strong security, use at least 12–16 characters.
- Since it uses Python’s secrets module, the randomness is suitable for cryptographic use.
- The script includes punctuation characters, so some generated passwords may contain symbols like @, #, %, etc.
