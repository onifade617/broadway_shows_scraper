import schedule
import time
from datetime import datetime
import subprocess

def run_scraper():
    print(f"[{datetime.now()}] Running scraper script...")
    try:
        subprocess.run(["python", "show_time.py"], check=True)
        print(f"[{datetime.now()}] Scraper finished successfully.")
    except subprocess.CalledProcessError as e:
        print(f"[{datetime.now()}] Error running scraper: {e}")

# Schedule to run every hour
schedule.every(24).hours.do(run_scraper)

print("Scheduler is running. Press Ctrl+C to stop.")
while True:
    schedule.run_pending()
    time.sleep(60)
