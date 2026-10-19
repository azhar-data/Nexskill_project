
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
 
# 1. Load data
df = pd.read_csv("seaBorn/Real_Estate_Sales_2001-2022_GL-Short.csv")
print(df.head())
print(df.info())
 
sns.set_theme(style="whitegrid")
 
# 2. Histogram - sale amount
plt.figure(figsize=(8, 5))
sns.histplot(data=df, x="Sale Amount", bins=30)
plt.title("Sale Amount Distribution")
plt.tight_layout()
plt.show()
plt.close()
 
# 3. Count plot - property type
plt.figure(figsize=(8, 5))
sns.countplot(data=df, y="Property Type")
plt.title("Sales by Property Type")
plt.tight_layout()
plt.show()
plt.close()
 
# 4. Count plot - top 10 towns
plt.figure(figsize=(8, 6))
sns.countplot(data=df, y="Town", order=df["Town"].value_counts().head(10).index)
plt.title("Top 10 Towns by Number of Sales")
plt.tight_layout()
plt.show()
plt.close()
 
# 5. Box plot - sale amount by property type
plt.figure(figsize=(9, 5))
sns.boxplot(data=df, x="Property Type", y="Sale Amount")
plt.xticks(rotation=20)
plt.title("Sale Amount by Property Type")
plt.tight_layout()
plt.show()
plt.close()
 
# 6. Scatter plot - assessed value vs sale amount
plt.figure(figsize=(8, 6))
sns.scatterplot(data=df, x="Assessed Value", y="Sale Amount", hue="Property Type")
plt.title("Assessed Value vs Sale Amount")
plt.tight_layout()
plt.show()
plt.close()
 
# 7. Heatmap - correlation
plt.figure(figsize=(6, 5))
sns.heatmap(df[["Assessed Value", "Sale Amount", "Sales Ratio"]].corr(),
            annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.tight_layout()
plt.show()
plt.close()