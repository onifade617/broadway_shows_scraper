import schedule
import time
from datetime import datetime, date
import subprocess
import os

# Constants for file names
LOG_FILE = "scrape_log.txt"          # File to log each successful scrape with timestamp
VERSION_FILE = "scrape_version.txt"  # File to store the last scrape date
SCRAPER_SCRIPT = "show_time.py"           # Name of the scraping script to run

# Function to check if the scraper has already run today
def already_scraped_today():
    if os.path.exists(VERSION_FILE):  # Check if version file exists
        with open(VERSION_FILE, "r") as f:
            last_scrape = f.read().strip()  # Read the last scrape date
            return last_scrape == str(date.today())  # Compare with today’s date
    return False  # If version file doesn’t exist, assume it hasn’t run today

# Function to log the current datetime when the scraper runs
def log_scrape_time():
    now = datetime.now()  # Get current date and time
    with open(LOG_FILE, "a") as log:  # Open log file in append mode
        log.write(f"Scrape run at {now}\n")  # Append timestamp to the log file

# Function to update the version file with today’s date
def update_version():
    with open(VERSION_FILE, "w") as f:  # Open version file in write mode
        f.write(str(date.today()))  # Overwrite with today’s date

# Function that runs the scraper, handles logging and versioning
def run_scraper():
    # Skip if the scraper has already run today
    if already_scraped_today():
        print(f"[{datetime.now()}] Scraper already ran today. Skipping.")
        return

    # Otherwise, proceed to run the scraper
    print(f"[{datetime.now()}] Running {SCRAPER_SCRIPT}...")
    try:
        # Run the scraper using subprocess
        subprocess.run(["python", SCRAPER_SCRIPT], check=True)
        log_scrape_time()  # Log the timestamp of the run
        update_version()   # Update version to mark it has run today
        print(f"[{datetime.now()}] Scraper finished successfully.")
    except subprocess.CalledProcessError as e:
        # If an error occurs while running the script, log the error
        print(f"[{datetime.now()}] Error running scraper: {e}")

# Schedule the scraper to run once every 24 hours
schedule.every(24).hours.do(run_scraper)

# Keep the scheduler running continuously
print("Scheduler is running. Press Ctrl+C to stop.")
while True:
    schedule.run_pending()  # Check and run scheduled jobs
    time.sleep(60)  # Wait one minute before checking again
