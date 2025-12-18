# Automated Amazon Price Tracker 🛒💰

A command-line tool that scrapes Amazon product pages, checks if the price is below your target, and sends you an email alert.

## Features
- User-provided Amazon URL and target price
- Web scraping with requests + BeautifulSoup
- Robust price parsing (handles missing/changing selectors)
- Email alerts via Gmail SMTP
- Secrets safely stored in ignored `config.py`
