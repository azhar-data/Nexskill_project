<div align="center">

# 📊 Seaborn — Statistical Data Visualization

### Explore Distributions • Compare Categories • Discover Relationships

![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Seaborn](https://img.shields.io/badge/Seaborn-Statistical%20Visualization-4C72B0?style=for-the-badge)
![Matplotlib](https://img.shields.io/badge/Matplotlib-Plotting-11557C?style=for-the-badge)

**A hands-on collection of Seaborn visualizations built around real-estate and startup-investment data.**

</div>

---

## 📚 Contents

- [Overview](#-overview)
- [Objectives](#-objectives)
- [Datasets and Scripts](#-datasets-and-scripts)
- [Visualizations Covered](#-visualizations-covered)
- [Real-Estate Analysis](#-real-estate-analysis)
- [Startup Analysis](#-startup-analysis)
- [Setup](#-setup)
- [Run the Examples](#-run-the-examples)
- [How to Read the Charts](#-how-to-read-the-charts)
- [Limitations and Improvements](#-limitations-and-improvements)
- [Author](#-author)

## 🔎 Overview

**Seaborn** is a Python data-visualization library built on Matplotlib. It makes it easier to create attractive statistical charts directly from Pandas DataFrames, including distribution plots, category comparisons, relationship plots, and heatmaps.

This folder applies Seaborn to two broad themes: real-estate listings and startup growth/investment. The scripts demonstrate how visualizations can help answer questions that are difficult to understand from raw tables alone.

## 🎯 Objectives

- Load CSV datasets with Pandas.
- Explore distributions and unusual observations.
- Compare numerical values across categories.
- Visualize relationships between investment, valuation, and growth.
- Practice common Seaborn plot types and chart customization.
- Use Matplotlib to set titles, labels, layouts, and output files.
- Understand how charts support exploratory data analysis (EDA).

## 🗂️ Datasets and Scripts

| File | Purpose |
|---|---|
| `RealEstate-USA.csv` | Property listings used to explore price, house size, bedroom counts, and city-level differences. |
| `RealEstate-USA.py` | Creates missing-value, distribution, bedroom-count, price-comparison, and city-level plots. |
| `startup_growth_investment_data.csv` | Startup records with fields such as industry, country, growth rate, investment amount, valuation, and investor counts. |
| `startup_growth_investment_data.py` | Demonstrates multiple Seaborn plots for startup growth and investment data. |
| `FastFoodRestaurants_fixed_comma.csv` | Restaurant data for further visualization practice. |
| `FastFoodRestaurants_fixed_comma.py` | Script associated with restaurant visualizations. |
| `Real_Estate_Sales_2001-2022_GL-Short.csv` | Additional real-estate sales data. |
| `k.py` | Additional practice script; inspect its contents before running. |

## 📈 Visualizations Covered

| Plot | Main use |
|---|---|
| `histplot` | Understand the distribution of a numerical variable. |
| `countplot` | Count observations in each category. |
| `boxplot` | Compare medians, spread, and potential outliers across groups. |
| `violinplot` | Compare distributions across categories. |
| `boxenplot` | Examine distribution tails, especially with larger samples. |
| `stripplot` | Display individual observations across categories. |
| `kdeplot` | Estimate a smooth distribution or density. |
| `ecdfplot` | Show the proportion of observations at or below each value. |
| `regplot` / `lmplot` | Explore a relationship and fit a regression trend. |
| `jointplot` | Compare two variables with a joint plot and marginal distributions. |
| `pairplot` | Explore pairwise relationships among multiple numeric columns. |
| `catplot` | Create categorical plots with a consistent interface. |
| `displot` | Create distribution plots, including faceted views. |
| `heatmap` | Visualize a matrix, such as missingness or a pivot table. |
| `barplot` | Compare an aggregate, such as mean or median, across categories. |

Not every chart is appropriate for every dataset. Choose plot types based on the question and the structure of the data.

## 🏠 Real-Estate Analysis

The real-estate script demonstrates how to:

- Inspect dataset dimensions and missing values.
- Remove a field that is entirely empty in the loaded dataset.
- Create a price-per-square-foot feature for exploratory use.
- Group bedroom counts for clearer plots.
- Inspect price distributions using a logarithmic scale.
- Compare listings and median prices across selected cities.
- Save selected charts to image files.

The script uses filtering thresholds to make some charts easier to read. Such thresholds should be documented and checked carefully because filtering changes the records included in the visualization. A price-per-square-foot calculation can also be undefined when house size is missing or zero.

## 🚀 Startup Growth and Investment Analysis

The startup script uses plots to explore questions such as:

- How are growth rates distributed?
- Do growth-rate distributions differ across industries?
- How does valuation vary by industry?
- Is there an apparent relationship between investment amount and valuation?
- How do valuation distributions vary across countries?
- How do industry and country intersect in aggregate comparisons?

The script demonstrates histograms, violin plots, boxen plots, strip plots, KDE and ECDF plots, regression plots, joint plots, pair plots, categorical plots, faceted distributions, and heatmaps built from pivot tables.

A visible trend is not proof of causation. Interpret plots alongside sample sizes, missingness, outliers, and the definitions of the dataset's fields.

## 🔄 Suggested Workflow

1. Load data with Pandas.
2. Inspect data types, dimensions, and missing values.
3. Select a focused question.
4. Choose a chart that fits the variable types.
5. Add readable titles, labels, and sensible axis scales.
6. Investigate outliers and category imbalance.
7. Save useful charts and summarize what they show.
8. Avoid causal claims unless supported by an appropriate study design.

## ⚙️ Setup

Recommended: Python 3.10 or later.

```bash
python -m venv .venv
```

Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

Install the required libraries:

```bash
python -m pip install --upgrade pip
pip install pandas numpy matplotlib seaborn
```

## ▶️ Run the Examples

From the repository root:

```bash
python "4. Seaborn/startup_growth_investment_data.py"
python "4. Seaborn/RealEstate-USA.py"
```

**Path note:** Some scripts currently reference paths such as `seaBorn/RealEstate-USA.csv`. If you receive a file-not-found error, update the path to the correct relative location. From the repository root, use `4. Seaborn/RealEstate-USA.csv`; from inside the folder, use `RealEstate-USA.csv`. The scripts open chart windows and may save selected real-estate charts to PNG files.

## 💡 Small Example

```python
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("RealEstate-USA.csv")

sns.set_theme(style="whitegrid")
sns.scatterplot(data=df, x="house_size", y="price", alpha=0.4)
plt.title("House Size vs. Listed Price")
plt.xlabel("House Size")
plt.ylabel("Listed Price")
plt.tight_layout()
plt.show()
```

Adjust the column names to match the dataset. For heavily skewed values, a logarithmic axis may improve readability, but it should be clearly labelled.

## 🧭 How to Read the Charts

- Check axis labels, units, and scale before interpreting a chart.
- Look for skewness and long tails in distributions.
- Compare medians and spreads, not just averages.
- Treat outliers as observations to investigate, not automatically as errors.
- Be cautious when categories have very different sample sizes.
- Remember that aggregation can hide variation within a group.
- A regression line describes an estimated association, not necessarily a causal effect.

## 🚀 Limitations and Improvements

- [ ] Standardize CSV paths and use paths relative to the script.
- [ ] Add a dedicated output directory for saved charts.
- [ ] Add data-source citations and definitions for units.
- [ ] Validate missing and zero values before derived calculations.
- [ ] Save high-resolution figures with consistent dimensions.
- [ ] Add captions describing each chart's main finding.
- [ ] Create a small dashboard for interactive filtering.
- [ ] Use sampled data thoughtfully for pair plots and dense scatter plots.
- [ ] Add requirements.txt for reproducible installation.

## 🎓 Learning Outcomes

This folder builds practical skill in statistical visualization, exploratory analysis, chart selection, and communicating patterns in data. Seaborn works especially well with Pandas and Matplotlib and is useful for preparing datasets for further machine-learning work.

## 👨‍💻 Author

**Muhammad Azhar**  
Python • Data Analysis • Data Science • Machine Learning

- GitHub: [@azhar-data](https://github.com/azhar-data)
- Repository: [Nexskill_project](https://github.com/azhar-data/Nexskill_project)

---

<div align="center">Turning raw data into readable visual insights.</div>
