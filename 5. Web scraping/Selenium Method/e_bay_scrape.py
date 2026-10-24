import csv
import time
import requests
from bs4 import BeautifulSoup
 
SEARCH = "smartphone" 
PAGES = 3               
 
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                  "(KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.9",
    "Referer": "https://www.google.com/",
}
 
session = requests.Session()
session.headers.update(headers)
session.get("https://www.ebay.com/", timeout=20)   # visit home page first
time.sleep(2)
 
data = []
seen = set()
 
for page in range(1, PAGES + 1):
    url = f"https://www.ebay.com/sch/i.html?_nkw={SEARCH}&_pgn={page}"
    response = session.get(url, timeout=20)
    print(f"Page {page}: status {response.status_code}")
 
    if response.status_code != 200:
        print("eBay blocked this request. Wait a few minutes and try again.")
        break
 
    soup = BeautifulSoup(response.text, "html.parser")
 
    # Each listing is an <li> box (eBay uses one of these two class names)
    cards = soup.select("li.s-card, li.s-item")
    print(f"  Listings found: {len(cards)}")
 
    for card in cards:
        title_tag = card.select_one(".s-card__title, .s-item__title")
        price_tag = card.select_one(".s-card__price, .s-item__price")
        link_tag = card.select_one("a[href*='/itm/']")
 
        if not (title_tag and price_tag and link_tag):
            continue  # skip ads / empty boxes
 
        title = title_tag.get_text(" ", strip=True)
        title = title.replace("Opens in a new window or tab", "").replace("New Listing", "").strip()
        price = price_tag.get_text(" ", strip=True)
        link = link_tag["href"].split("?")[0]
 
        if title == "Shop on eBay" or link in seen:
            continue
 
        seen.add(link)
        data.append([title, price, link])
 
    time.sleep(2)   # be polite, don't hammer the site
 
# Save to CSV
with open("ebay_products.csv", "w", newline="", encoding="utf-8-sig") as f:
    writer = csv.writer(f)
    writer.writerow(["Title", "Price", "Link"])
    writer.writerows(data)
 
print("Saved", len(data), "listings to ebay_products.csv")
 
