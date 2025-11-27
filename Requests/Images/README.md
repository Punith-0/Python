🖼️ Image Downloader Script
A simple Python script to download images from the web using a given URL.
It retries failed downloads up to 3 times and provides colored console output using ANSI formatting.

📌 Features
- Download images directly from a URL.
- Save with a custom filename and extension (.png, .jpg, .jpeg).
- Retry logic (3 attempts) for handling timeouts or errors.
- Colored console messages for success, retry, and error states.

🚀 Requirements
- Python 3.8+
- Libraries:
- requests (for HTTP requests)
- Ansi (custom ANSI formatting module for colored output)
Install dependencies:
pip install requests


⚠️ Note: The Ansi module is a custom utility. If you don’t have it, you can replace the ANSI codes with plain text or use libraries like colorama.


📂 Usage
- Clone or download this repository.
- Run the script:
python3 download_images.py
- Enter:
- The image URL (must be a direct link to the image, not a webpage).
- The filename with extension (e.g., cat.png, photo.jpg).

📝 Example
Enter Images url from the web : https://example.com/cat.jpg
Enter name of the image with extenssion(png , jpg , jpeg) : my_cat.jpg
Image downloaded successfully in your project folder.



⚡ Notes
- Ensure the URL points directly to an image file. If the URL returns HTML or JSON, the saved file may not open as an image.
- Timeout is set to 2 seconds per request. You can adjust this in the code.
- The script retries up to 3 times before failing.
