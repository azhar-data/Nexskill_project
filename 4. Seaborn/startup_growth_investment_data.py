import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
 
df = pd.read_csv("seaBorn/startup_growth_investment_data.csv")
sns.set_theme(style="whitegrid")
 
#  Histogram - growth rate

sns.histplot(data=df, x="Growth Rate (%)", kde=True)
plt.title("Growth Rate Distribution")
plt.show()


#  Violin plot - growth rate by industry
sns.violinplot(data=df, x="Industry", y="Growth Rate (%)")
plt.xticks(rotation=45)
plt.title("1. Violin Plot")
plt.tight_layout()
plt.show()
 
#  Boxen plot - valuation by industry
sns.boxenplot(data=df, x="Industry", y="Valuation (USD)")
plt.xticks(rotation=45)
plt.title("2. Boxen Plot")
plt.tight_layout()
plt.show()
 
#  Strip plot - growth by funding rounds (sample of 500 points)
sns.stripplot(data=df.sample(500, random_state=1), x="Funding Rounds", y="Growth Rate (%)")
plt.title("3. Strip Plot")
plt.show()
 
#  KDE plot - investment amount by industry
sns.kdeplot(data=df, x="Investment Amount (USD)", hue="Industry")
plt.title("4. KDE Plot")
plt.show()
 
# ECDF plot - valuation
sns.ecdfplot(data=df, x="Valuation (USD)")
plt.title("5. ECDF Plot")
plt.show()
 
#  Reg plot - scatter + regression line
sns.regplot(data=df, x="Investment Amount (USD)", y="Valuation (USD)",
            scatter_kws={"alpha": 0.3}, line_kws={"color": "red"})
plt.title("6. Reg Plot")
plt.show()
 
#  Joint plot - scatter with histograms on the sides
sns.jointplot(data=df, x="Investment Amount (USD)", y="Valuation (USD)", kind="hex")
plt.show()
 
#  Pair plot - all numeric columns together
sns.pairplot(df[["Investment Amount (USD)", "Valuation (USD)",
                 "Number of Investors", "Growth Rate (%)"]].sample(500, random_state=1))
plt.show()
 
#  Cat plot - average valuation by country
sns.catplot(data=df, x="Country", y="Valuation (USD)", kind="bar", height=5, aspect=2)
plt.xticks(rotation=45)
plt.show()
 
#  Displot with columns - growth histogram for each industry
sns.displot(data=df, x="Growth Rate (%)", col="Industry", col_wrap=4, height=2.5)
plt.show()
 
#  Lm plot - regression per industry (first 4 industries)
top4 = df[df["Industry"].isin(df["Industry"].unique()[:4])]
sns.lmplot(data=top4, x="Investment Amount (USD)", y="Valuation (USD)",
           col="Industry", col_wrap=2, height=3.5, scatter_kws={"alpha": 0.3})
plt.show()
 
#  Heatmap with pivot table - avg valuation, industry vs country
pivot = df.pivot_table(index="Industry", columns="Country",
                       values="Valuation (USD)", aggfunc="mean")
sns.heatmap(pivot, annot=True, fmt=".2e", cmap="YlGnBu")
plt.title("12. Heatmap (Pivot Table)")
plt.tight_layout()
plt.show()
 
#  Clustermap - groups similar rows and columns together
sns.clustermap(pivot, cmap="viridis", standard_scale=1, figsize=(8, 6))
plt.show()
 
#  Scatter plot with size - bubble chart
sns.scatterplot(data=df.sample(500, random_state=1), x="Investment Amount (USD)",
                y="Valuation (USD)", size="Growth Rate (%)", hue="Industry", alpha=0.6)
plt.legend(bbox_to_anchor=(1.02, 1), loc="upper left", fontsize=7)
plt.title("14. Bubble Chart")
plt.tight_layout()
plt.show()
 
#  Point plot - average valuation by number of funding rounds
sns.pointplot(data=df, x="Funding Rounds", y="Valuation (USD)")
plt.title("15. Point Plot")
plt.show()