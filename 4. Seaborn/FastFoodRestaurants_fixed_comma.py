
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
 
# 1. Load data
df = pd.read_csv("seaBorn/FastFoodRestaurants_fixed_comma.csv")
print(df.head())
print(df.info())
 
sns.set_theme(style="whitegrid")
 
# 2. Top 10 chains
plt.figure(figsize=(9, 5))
sns.countplot(data=df, y="name", order=df["name"].value_counts().head(10).index)
plt.title("Top 10 Fast Food Chains")
plt.tight_layout()
plt.savefig("s1_top_chains.png")
plt.show()
plt.close()
 
# 3. Top 10 states
plt.figure(figsize=(9, 5))
sns.countplot(data=df, y="province", order=df["province"].value_counts().head(10).index)
plt.title("Top 10 States")
plt.tight_layout()
plt.savefig("s2_top_states.png")
plt.show()
plt.close()
 
# 4. Top 10 cities
plt.figure(figsize=(9, 5))
sns.countplot(data=df, y="city", order=df["city"].value_counts().head(10).index)
plt.title("Top 10 Cities")
plt.tight_layout()
plt.savefig("s3_top_cities.png")
plt.show()
plt.close()
 
# 5. Map of all restaurants (keep only the lower 48 states)
us = df[df["latitude"].between(24, 50) & df["longitude"].between(-125, -66)]
plt.figure(figsize=(11, 6))
sns.scatterplot(data=us, x="longitude", y="latitude", s=5, alpha=0.4)
plt.title("All Restaurants (lower 48 states)")
plt.tight_layout()
plt.savefig("s4_map.png")
plt.show()
plt.close()
 
# 6. Map of the top 3 chains
top3 = df["name"].value_counts().head(3).index
plt.figure(figsize=(11, 6))
sns.scatterplot(data=us[us["name"].isin(top3)], x="longitude", y="latitude",
                hue="name", s=10, alpha=0.6)
plt.title("Top 3 Chains")
plt.tight_layout()
plt.savefig("s5_top3_map.png")
plt.show()
plt.close()
 
# 7. Heatmap - top 5 chains by top 8 states
top5 = df["name"].value_counts().head(5).index
states8 = df["province"].value_counts().head(8).index
sub = df[df["name"].isin(top5) & df["province"].isin(states8)]
table = pd.crosstab(sub["name"], sub["province"])
plt.figure(figsize=(9, 4))
sns.heatmap(table, annot=True, fmt="d", cmap="YlOrRd")
plt.title("Restaurants per Chain and State")
plt.tight_layout()
plt.savefig("s6_heatmap.png")
plt.show()
plt.close()