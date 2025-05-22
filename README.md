
# Broadway Production Show Scraper

This Python script scrapes current Broadway production show listings from [IBDB.com](https://www.ibdb.com/shows), extracting details such as:

- 🎫 Show Title  
- 🖼️ Poster Image URL  
- 🎭 Show Type  
- 🎤 Performance Description  
- 🏛️ Theatre Name  
- 📅 Date  
- 🔗 Detail Page Link

The extracted data is saved into a CSV file named `ibdb_shows.csv`.

---

## 🛠️ Requirements

### Python Version
- Python 3.7 or newer

### Python Packages
- `selenium`
- `beautifulsoup4`
- `pandas`
- `requests`
- `re` 

---

## 🔧 Setup Instructions

### 1. Clone or Download This Repository

```bash
git clone https://github.com/onifade617
cd broadway_shows_scraper
```

### 2. Create a Virtual Environment (Optional)

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```





---

## 🚀 Usage

To run the scraper:

```bash
python show_time.py
```

The script will:
- Launch a Chrome browser using Selenium
- Navigate to the IBDB Shows page
- Scrape relevant data from each show detail page
- Save the collected information into `ibdb_shows.csv`



## ⚠️ Notes

- The scraper uses `time.sleep()` to wait for pages to load. You can replace this with `WebDriverWait` for better control.
- Scraping large websites may violate terms of service. Use responsibly.
- If the website layout changes, class names and logic may need updating.

---

## 📬 Contact

Feel free to contribute or report issues on GitHub.

---

