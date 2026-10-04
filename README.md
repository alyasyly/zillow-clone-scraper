# Zillow Clone Scraper & Google Form Filler

A simple Python project that scrapes rental/property listings from a Zillow clone website and automatically fills a Google Form with the scraped data (address, price, and link).

## Features

- Scrapes property listings (address, price, link) from a Zillow clone page
- Cleans and normalizes the extracted data
- Automatically fills a Google Form using Selenium
- Submits multiple entries one after another

## Project Structure

```
.
├── main.py           # Entry point – runs the scraper and form filler
├── scraper.py        # Web scraping logic (BeautifulSoup + requests)
├── form_filler.py    # Google Form automation (Selenium)
└── .env              # Environment variables (FORM URL)
```

## Requirements

- Python 3.8+
- Google Chrome browser
- ChromeDriver (compatible with your Chrome version)

### Python packages

```bash
pip install requests beautifulsoup4 selenium python-dotenv
```

## Setup

1. Clone or download this project.

2. Create a `.env` file in the project root and add your Google Form URL:

   ```env
   FORM=https://docs.google.com/forms/d/e/your-form-id/viewform
   ```

3. Make sure Google Chrome and a matching ChromeDriver are installed and available in your system PATH.

## Usage

Run the main script:

```bash
python main.py
```

The script will:

1. Scrape all listings from the Zillow clone page.
2. Open Chrome and navigate to the Google Form.
3. Fill in Address, Price, and Link for each listing.
4. Submit the form and click “Submit another response” to continue with the next listing.

## How it Works

### `scraper.py`
- Fetches the page: `https://appbrewery.github.io/Zillow-Clone/`
- Parses the listings using BeautifulSoup
- Extracts and cleans:
  - Property address
  - Price (removes `+` and `/mo` suffixes)
  - Property link

### `form_filler.py`
- Uses Selenium with Chrome
- Locates the three text inputs on the Google Form
- Fills Address → Price → Link
- Submits the form and prepares for the next entry

### `main.py`
- Calls `get_data()` from the scraper
- Passes the list of dictionaries to `fill_form()`

## Notes

- The form must have **exactly three text input fields** in this order: Address, Price, Link.
- The “Submit” button and “Submit another response” link must match the XPath selectors used in `form_filler.py`.
- Chrome is launched with the `detach` option so the browser stays open after the script finishes (useful for debugging).

## Disclaimer

This project is intended for educational purposes only. Always respect the terms of service of any website you scrape and the robots.txt file. Do not use this script for commercial purposes or against sites that prohibit scraping.