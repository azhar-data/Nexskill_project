import csv
import re
from bs4 import BeautifulSoup
 
# 1. Read the saved page
with open("page.html", encoding="utf-8", errors="ignore") as f:
    soup = BeautifulSoup(f.read(), "html.parser")
 
# 2. Pattern for a price like "$499.99" or "$27.99 to $51.29"
PRICE = r"\$[\d,]+(?:\.\d+)?(?:\s*to\s*\$[\d,]+(?:\.\d+)?)?"
 
data = []
seen = set()
 
# 3. Find every piece of text that contains a price
for node in soup.find_all(string=re.compile(r"\$\s?[\d,]+")):
 
    # 4. Go up until we reach the product box (the one that has a link inside)
    box = node.parent
    for _ in range(8):
        if box.find("a", href=True):
            break
        box = box.parent
    if box is None or box.name in ("body", "html"):
        continue
 
    link_tag = box.find("a", href=True)
    if not link_tag:
        continue
    link = link_tag["href"].split("?")[0]
    if link in seen:
        continue
 
    # 5. Title: use a heading if there is one, else the longest line of text
    heading = box.find(["h3", "h2"])
    if heading:
        title = heading.get_text(" ", strip=True)
    else:
        lines = [l for l in box.get_text("\n", strip=True).split("\n") if "$" not in l]
        title = max(lines, key=len) if lines else ""
 
    price_match = re.search(PRICE, box.get_text(" ", strip=True))
    price = price_match.group(0) if price_match else "N/A"
 
    if title:
        seen.add(link)
        data.append([title, price, link])
 
# 6. Save to CSV
with open("ebay_products.csv", "w", newline="", encoding="utf-8-sig") as f:
    writer = csv.writer(f)
    writer.writerow(["Title", "Price", "Link"])
    writer.writerows(data)
 
print("Saved", len(data), "listings to ebay_products.csv")