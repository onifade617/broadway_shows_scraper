# === Import required libraries ===
from selenium import webdriver
from bs4 import BeautifulSoup
import time
import re
import requests
import pandas as pd

# === Set up the Chrome WebDriver ===
driver = webdriver.Chrome()
driver.set_page_load_timeout(300)  # Set a timeout limit for page load

# === List to store scraped data ===
data = []

# === Open the target webpage ===
driver.get("https://www.ibdb.com/shows")
time.sleep(5)  # Allow time for JavaScript to load the content

# === Get the HTML content and parse it with BeautifulSoup ===
soup = BeautifulSoup(driver.page_source, "html.parser")
base_url = "https://www.ibdb.com"  # Base URL for building full links

# === Navigate to the container holding all show cards ===
heading = soup.find("div", class_="page-wrapper xtrr")\
    .find("div", class_="shows-page")\
    .find("div", class_="row bgcolor-greyWhite2")\
    .find("div", class_="xt-c-box row")\
    .find("div", id="current")\
    .find("div", class_="row show-images xt-iblocks")\
    .find_all("div", class_="xt-iblock")

# === Loop through each show card to extract individual show links ===
for link in heading:
    link_indv = link.find("div", class_="xt-iblock-inner")\
        .find("a", href=True)
    if link_indv:
        full_url = base_url + link_indv['href']

        for attempt in range(2):  # Maximum of 2 attempts
            try:
                driver.get(full_url)
                time.sleep(5)
                break  # Break out of loop if successful
            except Exception as e:
                print(f"[Attempt {attempt+1}] Error loading {full_url}: {e}")
                if attempt == 1:  # On second failure
                    print(f"Skipping {full_url} after two failed attempts.")
                    continue  # Move to the next show
                
        # === Parse the individual show page ===
        show_soup = BeautifulSoup(driver.page_source, "html.parser")
        base_bar1 = show_soup.find("body", class_="winOS")
        print(show_soup.prettify())  # (Optional) print full HTML structure

        # === Defensive check for base container ===
        base_bar2 = base_bar1.find("div", class_="page-wrapper xtrr")
        if base_bar1 is None:
            print("Could not find: page-wrapper xtrr")
            exit()

        # === Drill down to show detail section ===
        base_bar = base_bar1.find("div", class_=re.compile("^production-page"))\
            .find("div", class_=re.compile("^xt-c-box"))\
            .find("div", class_="row xt-fixed-sidebar-row")

        # === Navigate to image/title/type container ===
        img_type_title = base_bar.find("div", class_=re.compile("col l4 m10 push-m1 s12 s12 xt-l-col-left"))\
            .find("div", class_=re.compile("production-info-panel"))\
            .find("div", class_=re.compile("xt-fixed-sidebar"))\
            .find("div", class_=re.compile("jsfixed-placeholder"))\
            .find("div", class_=re.compile("jsfixed-block"))

        # === Extract the logo/title section ===
        img_title = img_type_title.find("div", class_=re.compile("xt-fixed-block main-logo-wrapper"))\
            .find("div", class_=re.compile("row logo"))\
            .find("div", class_=re.compile("col s12"))\
            .find("div", class_=re.compile("logo-block xt-logo-block sdf"))

        # === Extract Show Image URL ===
        image = img_title.find("div", class_=re.compile("xt-logo-img"))\
            .find("img")['src']

        # === Extract Show Title ===
        title = img_title.find("div", class_="title")\
            .find("div").find("h3").text

        # === Extract Show Type (e.g. Musical, Play) ===
        show_type = img_type_title.find("div", attrs={"data-id": "part-b"})\
            .find("div", class_="row wrapper hide-on-small-and-down")\
            .find("div")\
            .find("i").text

        # === Extract Performance Info (e.g., Broadway, Off-Broadway) ===
        perform = img_type_title.find("div", attrs={"data-id": "part-b"})\
            .find("div", class_="xt-info-block")\
            .find_all("div", class_="row wrapper")

        third_instance = perform[1].find(class_='col s7 m6 l7 txt-paddings vertical-divider')\
            .find("div", class_="xt-main-title").text

        # === Locate the venue and date section ===
        venue_date_parent = base_bar.find("div", class_=re.compile("col l8 m12 def-text s12 xt-l-col-right"))\
            .find_all("div", class_="row")

        # Try to find the div with id='venues' (fallback from index 1 to 2)
        venue_container = venue_date_parent[1]
        venues_div = venue_container.find(id="venues")
        if not venues_div:
            venue_container = venue_date_parent[2]
            venues_div = venue_container.find(id="venues")

        if not venues_div:
            raise Exception("Missing div with id='venues' in both venue_date_parent[1] and [2]")

        # === Extract Theatre Name and Opening Date ===
        theatre_div = venues_div.find("div", class_=re.compile("col s12 m4 theatre"))
        if not theatre_div:
            raise Exception("Missing theatre div")

        row_blocks = theatre_div.find_all("div", class_="row")
        if len(row_blocks) < 2:
            raise Exception("Unexpected number of row divs in theatre block")

        venue = row_blocks[1].find("a").text.strip()
        date = row_blocks[1].find("i").text.strip()

        # === Store all extracted data in a dictionary ===
        data.append({
            "Title": title,
            "Date": date,
            "Image Link": image,
            "Theatre Name": venue,
            "Performance": third_instance,
            "Show Type": show_type,
            "Detail_Link": full_url
        })

        print(data)  # (Optional) print each extracted data entry

# === Convert data to DataFrame and save to CSV ===
df = pd.DataFrame(data)
df.to_csv("ibdb_shows.csv", index=False)
print("Scraping completed and data saved to 'ibdb_shows.csv'.")

# === Clean up: Close the browser ===
driver.quit()




