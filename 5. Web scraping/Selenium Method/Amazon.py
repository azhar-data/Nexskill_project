
import csv
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
 
URL = "https://www.amazon.com/"
 
# 1. Open Chrome and go to the page
driver = webdriver.Chrome()
driver.get(URL)
time.sleep(6)  # wait for page to load (if a captcha shows, solve it by hand now)
 
# 2. Scroll down so more products load
for i in range(6):
    driver.execute_script("window.scrollBy(0, 800);")
    time.sleep(1)
 
# 3. Find all product links (every Amazon product link contains "/dp/")
links = driver.find_elements(By.CSS_SELECTOR, "a[href*='/dp/']")
 
# 4. Collect title and link (skip duplicates and empty ones)
data = []
seen = set()
for a in links:
    url = a.get_attribute("href").split("?")[0]   # remove tracking junk
    title = a.text.strip()
    if not title:
        # many links only have an image, so use the image's alt text
        try:
            title = a.find_element(By.TAG_NAME, "img").get_attribute("alt")
        except Exception:
            continue
    if title and url not in seen:
        seen.add(url)
        data.append([title, url])
 
driver.quit()
 
# 5. Save to CSV
with open("amazon_products.csv", "w", newline="", encoding="utf-8-sig") as f:
    writer = csv.writer(f)
    writer.writerow(["Title", "Link"])
    writer.writerows(data)
 
print("Saved", len(data), "products to amazon_products.csv")