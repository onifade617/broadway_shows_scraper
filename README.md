
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
git clone https://github.com/onifade617/broadway_shows_scraper
cd ibdb-scraper
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

If you don't have a `requirements.txt` yet, create one with:

```bash
pip install selenium beautifulsoup4 pandas requests lxml
pip freeze > requirements.txt
```

### 4. Install ChromeDriver

- Download from: https://sites.google.com/chromium.org/driver/
- Place it in your system PATH or specify the path explicitly in the script:

```python
driver = webdriver.Chrome(executable_path='/path/to/chromedriver')
```

---

## 🚀 Usage

To run the scraper:

```bash
python ibdb_scraper.py
```

The script will:
- Launch a Chrome browser using Selenium
- Navigate to the IBDB Shows page
- Scrape relevant data from each show detail page
- Save the collected information into `ibdb_shows.csv`

---

## 📄 Output Format

A sample of the CSV output:

| Title     | Date     | Image Link | Theatre Name | Performance | Show Type | Detail_Link |
|-----------|----------|------------|---------------|-------------|-----------|-------------|
| Wicked    | Jun 15, 2025 | https://...jpg | Gershwin Theatre | Musical Performance | Musical | https://www.ibdb.com/... |

---

## ⚠️ Notes

- The scraper uses `time.sleep()` to wait for pages to load. You can replace this with `WebDriverWait` for better control.
- Scraping large websites may violate terms of service. Use responsibly.
- If the website layout changes, class names and logic may need updating.

---

## 📬 Contact

Feel free to contribute or report issues on GitHub.

---

