import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
 
# ---------------------------------------------------------------
# 1. Load and clean
# ---------------------------------------------------------------
df = pd.read_csv("seaBorn/RealEstate-USA.csv")
print(df.shape)
print(df.isna().sum())
 
# prev_sold_date is completely empty; state and status have only one value
df = df.drop(columns=["prev_sold_date"])

 
# Helpful new columns
df["price_per_sqft"] = df["price"] / df["house_size"]
 
# Rows that have a bedroom count (6 means "6 or more")
bed_df = df.dropna(subset=["bed"]).copy()
bed_df["bed_group"] = bed_df["bed"].clip(upper=6).astype(int)
 
# Remove obvious outliers for the plots that compare house size
clean = df[(df["house_size"] < 10000) & (df["price"] < 5_000_000)]
 
# Keep only the 8 cities with the most listings
top_cities = df["city"].value_counts().head(8).index.tolist()
city_df = df[df["city"].isin(top_cities)]
 
sns.set_theme(style="whitegrid")
 
 
def finish(title, filename=None):
    """Set the title, save, show and CLOSE the figure so charts never overlap."""
    plt.title(title)
    plt.tight_layout()
    if filename:
        plt.savefig(filename)
    plt.show()
    plt.close("all")
 
 
# 2. Missing values (yellow = missing)
plt.figure(figsize=(9, 5))
sns.heatmap(df.isna(), cbar=False, yticklabels=False, cmap="viridis")
finish("Missing Values", "r1_missing_values.png")
 
# 3. Price distribution (log scale because a few listings are huge)
plt.figure(figsize=(8, 5))
sns.histplot(data=df, x="price", log_scale=True, kde=True, bins=30)
finish("Price Distribution (log scale)", "r2_price_hist.png")
 
# 4. Count of listings per bedroom number
plt.figure(figsize=(8, 5))
sns.countplot(data=bed_df, x="bed_group")
finish("Listings by Bedrooms (6 = 6 or more)", "r3_bedrooms_count.png")
 
# 5. Price by bedrooms (log scale)
plt.figure(figsize=(8, 5))
sns.boxplot(data=bed_df, x="bed_group", y="price")
plt.yscale("log")
finish("Price by Bedrooms (log scale)", "r4_price_by_bedrooms.png")
 
# 6. Listings and median price by city
median_price = (city_df.groupby("city")["price"].median()
                .reindex(top_cities).reset_index())
fig, axes = plt.subplots(1, 2, figsize=(14, 5))
sns.countplot(data=city_df, y="city", order=top_cities, ax=axes[0])
axes[0].set_title("Listings per City (top 8)")
sns.barplot(data=median_price, y="city", x="price", order=top_cities, ax=axes[1])
axes[1].set_title("Median Price per City (top 8)")
plt.tight_layout()
plt.savefig("r5_cities.png")
plt.show()
plt.close("all")
 
# 7. House size vs price
plt.figure(figsize=(8, 5))
sns.regplot(data=clean, x="house_size", y="price",
            scatter_kws={"alpha": 0.5}, line_kws={"color": "red"})
finish("House Size vs Price (outliers removed)", "r6_size_vs_price.png")
 
# 8. Price per square foot by city
plt.figure(figsize=(9, 5))
sns.boxplot(data=city_df[city_df["price_per_sqft"] < 1000],
            x="city", y="price_per_sqft", order=top_cities)
plt.xticks(rotation=45)
finish("Price per Sq Ft by City", "r7_price_per_sqft.png")
 
# 9. Bedrooms vs bathrooms heatmap (median price)
pivot = bed_df.pivot_table(index="bed_group", columns="bath",
                           values="price", aggfunc="median")
plt.figure(figsize=(9, 5))
sns.heatmap(pivot, annot=True, fmt=".0f", cmap="YlOrRd")
finish("Median Price: Bedrooms vs Bathrooms", "r8_bed_bath_heatmap.png")
 
# 10. Correlation heatmap
cols = ["price", "bed", "bath", "acre_lot", "house_size"]
plt.figure(figsize=(7, 5))
sns.heatmap(clean[cols].corr(), annot=True, cmap="coolwarm", center=0)
finish("Correlation Heatmap", "r9_correlation.png")
 
# 11. Pair plot (creates its own figure)
sns.pairplot(clean[["price", "bed", "bath", "house_size"]].dropna())
plt.savefig("r10_pairplot.png")
plt.show()
plt.close("all")
 
# 12. Lot size vs price (log scales), coloured by bedrooms
plt.figure(figsize=(8, 5))
sns.scatterplot(data=bed_df, x="acre_lot", y="price", hue="bed_group", palette="viridis")
plt.xscale("log")
plt.yscale("log")
finish("Lot Size vs Price (log-log)", "r11_lot_vs_price.png")
 