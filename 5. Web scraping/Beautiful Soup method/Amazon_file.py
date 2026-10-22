from bs4 import BeautifulSoup
import csv

with open("Smart Home Devices & Systems.html", "r", encoding="utf-8") as file:
    html = file.read()

soup = BeautifulSoup(html, "html.parser")

products = soup.find_all("img", class_="ucw-widget-product-card-image")

data = []

for product in products:
    name = product.get("alt")

    card = product.find_parent(
        "div",
        class_="ucw-widget-product-card"
    )

    price_box = card.find(
        "div",
        class_="ucw-widget-product-card-price"
    )
    price = price_box.find(
        "span",
        class_="a-offscreen"
    ).get_text(strip=True)

    rating = card.find(
        "span",
        class_="a-icon-alt"
    ).get_text(strip=True)

    reviews = card.find(
        "span",
        class_="a-size-base a-color-secondary"
    ).get_text(strip=True)

    product_data = {
        "Product": name,
        "Price": price,
        "Rating": rating,
        "Reviews": reviews
    }

    data.append(product_data)

print(data)

with open("amazon_smart_home_products.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(
        file,
        fieldnames=["Product", "Price", "Rating", "Reviews"]
    )

    writer.writeheader()
    writer.writerows(data)