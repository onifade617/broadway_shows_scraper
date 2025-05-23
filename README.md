
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
## Project Structure

- `show_time.py`: Main scraping script that extracts show details from IBDB.
- `scheduler.py`: Runs the scraping script every 24 hours using the `schedule` library.
- `requirements.txt`: Lists all the required Python packages.
- `ibdb_shows.csv`: Output CSV file with the scraped show data.

---

## How `show_time.py` Works

This script uses **Selenium** and **BeautifulSoup** to scrape information from the IBDB website.

### Key Steps:

1. **Set Up Selenium WebDriver**: Initializes a Chrome browser instance.
2. **Load Show Listings Page**: Navigates to the IBDB shows page.
3. **Parse HTML Content**: Uses BeautifulSoup to parse dynamically loaded content.
4. **Extract Show Links**: Gathers URLs of individual show pages.
5. **Scrape Individual Show Data**:
   - Show Title
   - Image Link
   - Show Type
   - Performance Info
   - Venue Name
   - Show Date
6. **Save Data**: Outputs all collected data into a CSV file called `ibdb_shows.csv`.

---

## How `scheduler.py` Works

This script uses the **schedule** library to automate the running of the scraper.

### Key Steps:

1. Imports required libraries (`schedule`, `time`, `datetime`, and `subprocess`).
2. Defines a function `run_scraper()` to call `show_time.py`.
3. Schedules the function to run every 24 hours.
4. Enters an infinite loop to keep checking and running pending tasks.

---

## Requirements

### Python Version
- Python 3.7 or newer

### Python Packages
- `selenium`
- `beautifulsoup4`
- `pandas`
- `requests`
- `re` 
- `schedule`

---

## Setup Instructions

### 1. Clone or Download This Repository

```bash
git clone https://github.com/onifade617/broadway_shows_scraper.git


```



### 3. Install Dependencies

```bash
pip install -r requirements.txt
```







---

## 🚀 Usage

## Running the Scripts

### Run Scraper Manually

```bash
python show_time.py
```
This script uses **Selenium** and **BeautifulSoup** to scrape information from the IBDB website.

### Key Steps:

1. **Set Up Selenium WebDriver**: Initializes a Chrome browser instance.
2. **Load Show Listings Page**: Navigates to the IBDB shows page.
3. **Parse HTML Content**: Uses BeautifulSoup to parse dynamically loaded content.
4. **Extract Show Links**: Gathers URLs of individual show pages.
5. **Scrape Individual Show Data**:
   - Show Title
   - Image Link
   - Show Type
   - Performance Info
   - Venue Name
   - Show Date
   - Scraped Time
6. **Save Data**: Outputs all collected data into a CSV file called `ibdb_shows.csv`.

---
### Run the Scheduler

```bash
python scheduler.py
```
## How `scheduler.py` Works

This script uses the **schedule** library to automate the running of the scraper.

### Key Steps:

1. Imports required libraries (`schedule`, `time`, `datetime`, and `subprocess`).
2. Defines a function `run_scraper()` to call `show_time.py`.
3. Schedules the function to run once in every 24 hours.
4. Enters an infinite loop to keep checking and running pending tasks.



## ⚠️ Notes

- Make sure you have Google Chrome installed and the corresponding [ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/) available in your PATH.
- JavaScript content is dynamically loaded, hence the need for Selenium.
