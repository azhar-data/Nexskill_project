# Simple Daraz scraper (saves to CSV)
# Install: pip install selenium
# Run:     python daraz_simple.py
 
import csv
import re
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
 
# 1. Open Chrome and go to Daraz search results
driver = webdriver.Chrome()
driver.get("https://www.daraz.pk/catalog/?q=laptop")
time.sleep(5)  # wait for page to load
 
# 2. Scroll down so all products load
for i in range(5):
    driver.execute_script("window.scrollBy(0, 800);")
    time.sleep(1)
 
# 3. Find all product boxes
products = driver.find_elements(By.CSS_SELECTOR, "[data-qa-locator='product-item']")
 
# 4. Collect title, price and link of each product
data = []
for p in products:
    link = p.find_element(By.CSS_SELECTOR, "a[title]")
    title = link.get_attribute("title")
    url = link.get_attribute("href")
 
    # price looks like "Rs. 85,000" inside the box text
    match = re.search(r"Rs\.?\s?[\d,]+", p.text)
    price = match.group(0) if match else "N/A"
 
    data.append([title, price, url])
 
driver.quit()
 
# 5. Save everything in a CSV file
with open("daraz_products.csv", "w", newline="", encoding="utf-8-sig") as f:
    writer = csv.writer(f)
    writer.writerow(["Title", "Price", "Link"])  # header row
    writer.writerows(data)
 
print("Saved", len(data), "products to daraz_products.csv")