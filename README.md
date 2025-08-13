# 🎬 TMDB CLI Movie Browser

A command-line tool to browse **The Movie Database (TMDb)** movies using Python and the [Rich](https://rich.readthedocs.io/) library for beautiful console output.  
Supports fetching **now playing**, **popular**, **top-rated**, and **upcoming** movies with detailed error handling.

---

## 📦 Features
- Fetches movie data from the TMDb API.
- Displays results in a **styled table**.
- Handles:
  - Network errors
  - Timeout errors
  - Invalid JSON responses
  - Empty results
  - API error messages
- Four movie categories:
  - 🎥 `playing` — Movies now playing in theaters.
  - 🔥 `popular` — Trending popular movies.
  - ⭐ `top` — Top-rated movies.
  - 📅 `upcoming` — Movies coming soon.

---

## 📋 Requirements

- Python **3.8+**
- [requests](https://pypi.org/project/requests/)
- [rich](https://pypi.org/project/rich/)

Install dependencies:
```bash
pip install requests rich
🔑 API Key Setup
This script requires a TMDb API key.

Create an account at TMDb.

Go to your account settings → API → Request an API key.

Replace the placeholder in the script:

my_api_key = "YOUR_API_KEY"
🚀 Usage
Run the script with the --type argument to choose the category:

python main.py --type playing
python main.py --type popular
python main.py --type top
python main.py --type upcoming
Example:

python main.py --type top
Output:

┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃                  Name                 ┃    Date    ┃                Description                   ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
┃ The Shawshank Redemption              ┃ 1994-09-23 ┃ Two imprisoned men bond over a number of ... ┃
┃ The Godfather                          ┃ 1972-03-14 ┃ Spanning the years 1945 to 1955, a chroni... ┃
└───────────────────────────────────────┴────────────┴──────────────────────────────────────────────┘

⚠ Error Handling
The script gracefully handles:

Network errors (e.g., no internet, DNS issues)

Timeouts (if the API is slow)

Non-200 HTTP status codes with API-provided error messages

Invalid JSON responses

Empty results from the API

Example error:

python main.py --type top
[red]Network error:[/red] HTTPSConnectionPool(host='api.themoviedb.org', port=443): Max retries exceeded...

📜 License
This project is for educational and personal use.
TMDb API usage is subject to TMDb's Terms of Service.

