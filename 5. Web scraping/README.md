<div align="center">

# 🕷️ Web Scraping with Python

### Requests • BeautifulSoup • Selenium • Product Data • CSV Export

![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)
![BeautifulSoup](https://img.shields.io/badge/BeautifulSoup-HTML%20Parsing-2E8B57?style=for-the-badge)
![Selenium](https://img.shields.io/badge/Selenium-Browser%20Automation-43B02A?style=for-the-badge&logo=selenium&logoColor=white)
![Pandas](https://img.shields.io/badge/CSV%20Data-Structured%20Output-150458?style=for-the-badge&logo=pandas&logoColor=white)

**A practical learning collection for extracting structured information from web pages and saving results for further analysis.**

</div>

---

## 📚 Contents

- [Overview](#-overview)
- [Objectives](#-objectives)
- [Folder Structure](#-folder-structure)
- [Tools and Techniques](#-tools-and-techniques)
- [Examples in This Repository](#-examples-in-this-repository)
- [How Web Scraping Works](#-how-web-scraping-works)
- [Installation](#-installation)
- [Running the Scripts](#-running-the-scripts)
- [Common Problems](#-common-problems)
- [Responsible Scraping](#-responsible-scraping)
- [Future Improvements](#-future-improvements)
- [Author](#-author)

## 🔎 Overview

Web scraping is the process of extracting information from web pages and converting it into a structured format that can be searched, analyzed, or stored. This folder practices two approaches:

1. **BeautifulSoup:** parsing HTML and extracting information from saved web pages.
2. **Selenium:** controlling a browser to work with pages that render content dynamically.

The examples focus on product listings from online shopping websites such as Daraz, eBay, and Amazon. Depending on the script and the source page, extracted fields can include product titles, prices, ratings, reviews, and product links.

This is a learning collection rather than a claim that every script currently works against every live website. Website layouts and access rules can change, so selectors and page structure may need maintenance.

## 🎯 Objectives

- Understand HTML documents and DOM structure.
- Parse saved HTML using BeautifulSoup.
- Find elements using tags, classes, attributes, and CSS selectors.
- Use Selenium to open pages and interact with dynamically rendered content.
- Extract relevant text and links from product listings.
- Handle duplicate links and missing fields.
- Export collected data to CSV files.
- Understand why selectors can break when websites change.
- Practice responsible and respectful data collection.

## 🗂️ Folder Structure

```text
5. Web scraping/
├── README.md
├── Beautiful Soup method/
│   ├── Amazon_file.py
│   ├── daraz.py
│   ├── e_bay_scrape.py
│   ├── ebay_products.csv
│   └── saved HTML pages
└── Selenium Method/
    ├── Amazon.py
    ├── daraz_scrape.py
    ├── e_bay_scrape.py
    ├── amazon_products.csv
    ├── daraz_products.csv
    └── ebay_products.csv
```

The exact output files available may change as scripts are run. Some scripts expect a saved HTML file whose name must match the code, while others navigate to a live website.

## 🧰 Tools and Techniques

### BeautifulSoup

BeautifulSoup parses HTML and helps navigate page elements. It is useful when HTML has already been saved or retrieved through an allowed HTTP request.

Common operations include:

- `BeautifulSoup(html, "html.parser")`
- `find()` and `find_all()`
- `get_text(strip=True)`
- `get()` for HTML attributes
- CSS-like tag and class filtering

### Selenium

Selenium controls a real browser. It can be useful when content is loaded with JavaScript or when interaction is needed to display a page's contents. Browser automation is more resource-intensive than parsing saved HTML and can be less reliable if based on fixed delays.

The current examples use Chrome through Selenium WebDriver. Browser and driver setup depends on your installed Selenium version and browser environment.

### CSV output

The scripts use Python's `csv` module to write extracted records into CSV files. CSV makes it easy to inspect the results in a spreadsheet or load them into Pandas for cleaning, visualization, and analysis.

## 🛍️ Examples in This Repository

| Script / folder | What it demonstrates |
|---|---|
| `Beautiful Soup method/daraz.py` | Parses a saved HTML page and attempts to extract product name, price, rating, and review information. |
| `Beautiful Soup method/e_bay_scrape.py` | Reads saved HTML, identifies price-containing product areas, and saves product title, price, and link fields. |
| `Beautiful Soup method/Amazon_file.py` | Additional Amazon-related scraping practice; inspect its source and input requirements before running. |
| `Selenium Method/daraz_scrape.py` | Opens a Daraz search page, scrolls through product listings, and saves titles, prices, and links. |
| `Selenium Method/Amazon.py` | Opens Amazon, scrolls the page, and collects product titles and links from visible page elements. |
| `Selenium Method/e_bay_scrape.py` | Additional eBay-related browser-scraping practice. |

### Example output fields

Depending on the script, exported CSV data may include:

- `Title` or `Product`
- `Price`
- `Rating`
- `Reviews`
- `Link`

Not every script extracts every field. Verify the CSV header and sample rows after execution.

## 🔄 How Web Scraping Works

1. **Choose a permitted source:** confirm that automated access is allowed and consider an official API where available.
2. **Load the page:** read a saved HTML file or open the page with a browser.
3. **Inspect the HTML:** identify the product card and the elements containing the desired fields.
4. **Extract values:** collect text and relevant attributes, such as a product link.
5. **Clean the output:** normalize whitespace, remove duplicates, and handle missing fields.
6. **Save records:** write structured rows to a CSV file.
7. **Validate results:** inspect several output rows and compare them with the original source.
8. **Analyze further:** use Pandas and Seaborn to clean, summarize, and visualize the collected data.

## ⚙️ Installation

Recommended: Python 3.10 or later.

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it on Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

Install the libraries used by the examples:

```bash
python -m pip install --upgrade pip
pip install beautifulsoup4 selenium pandas requests
```

The scripts that only parse local HTML may need BeautifulSoup and the standard library. Selenium scripts require a working browser environment. Recent Selenium versions can often manage browser drivers automatically, but this depends on your system setup.

## ▶️ Running the Scripts

From the repository root, example commands are:

```bash
python "5. Web scraping/Beautiful Soup method/daraz.py"
python "5. Web scraping/Beautiful Soup method/e_bay_scrape.py"
python "5. Web scraping/Selenium Method/daraz_scrape.py"
python "5. Web scraping/Selenium Method/Amazon.py"
```

### Check input paths first

Some BeautifulSoup scripts open local files such as `page.html` or a saved Daraz HTML page. Make sure the file exists at the relative path expected by the script. If running from a different working directory, update the path or run from the folder the script expects.

Selenium scripts open live pages. They may take time, encounter access restrictions, or return no listings if the page structure has changed. Do not assume that a successful browser launch means that the scraper extracted valid data.

## 🧪 Validate the Results

After running a script:

1. Confirm the terminal reports the number of records saved, if the script prints one.
2. Open the output CSV and check the column names.
3. Check several titles, prices, and links against the source page.
4. Look for duplicate products, blank titles, missing prices, and malformed URLs.
5. Confirm that values have not been incorrectly associated with the wrong product card.
6. Record the collection date if the data may change over time.

## 🛠️ Common Problems

| Problem | Possible cause / next step |
|---|---|
| `FileNotFoundError` | A saved HTML or CSV path does not match the working directory. |
| No products found | HTML classes or CSS selectors may have changed, or content has not loaded. |
| Missing title or price | Some product cards have different layouts or unavailable fields. |
| Selenium cannot start Chrome | Check Chrome installation, Selenium version, and WebDriver configuration. |
| Page displays a CAPTCHA or access-denied page | Stop and follow the site's access process; do not attempt to bypass access controls. |
| Duplicate CSV rows | Normalize product URLs and deduplicate records before saving. |
| Script waits too long | Replace fixed sleeps with explicit Selenium waits for expected elements where permitted. |

## ⚖️ Responsible Scraping

Before collecting data from a website:

- Read its terms of service and applicable automated-access policies.
- Check its `robots.txt` guidance and any published rate limits.
- Prefer an official API or downloadable dataset when one is available and suitable.
- Send requests at a reasonable rate and avoid overloading services.
- Do not bypass CAPTCHAs, authentication, paywalls, or other access controls.
- Respect copyright, privacy, and data protection requirements.
- Store only the data needed for the intended analysis.
- Keep source URLs and collection dates where useful for traceability.

A page being publicly visible does not automatically mean every form of automated collection or reuse is permitted.

## 🚀 Future Improvements

- [ ] Use explicit waits in Selenium rather than fixed sleep durations.
- [ ] Move selectors and URLs into configuration variables.
- [ ] Add error handling for missing elements and unexpected page layouts.
- [ ] Normalize prices into numeric values while preserving the original text.
- [ ] Add deduplication and URL validation.
- [ ] Save logs and collection timestamps.
- [ ] Add a reusable scraper class or functions for shared behavior.
- [ ] Use Pandas to clean and analyze exported CSV files.
- [ ] Add tests using saved HTML fixtures rather than relying only on live websites.
- [ ] Document each source's access policy and dataset provenance.

## 🎓 Learning Outcomes

This folder provides practical experience in HTML parsing, browser automation, structured extraction, CSV storage, debugging selectors, and data validation. These techniques can support downstream data analysis and machine-learning projects when used responsibly.

## 👨‍💻 Author

**Muhammad Azhar**  
Python • Web Scraping • Data Analysis • Machine Learning

- GitHub: [@azhar-data](https://github.com/azhar-data)
- Repository: [Nexskill_project](https://github.com/azhar-data/Nexskill_project)

---

<div align="center">Collect data thoughtfully. Validate it carefully. Analyze it responsibly.</div>
