<div align="center">

# 🐼 Pandas — Data Analysis and Manipulation

### DataFrames • Data Cleaning • Filtering • Indexing • Real-World CSV Files

![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458?style=for-the-badge&logo=pandas&logoColor=white)
![Status](https://img.shields.io/badge/Focus-Hands--On%20Practice-blue?style=for-the-badge)

**A practical collection of Pandas scripts for loading, inspecting, selecting, filtering, and summarizing real-world tabular datasets.**

</div>

---

## 📚 Contents

- [Overview](#-overview)
- [Objectives](#-objectives)
- [Files and Datasets](#-files-and-datasets)
- [Pandas Concepts](#-pandas-concepts)
- [Workflow](#-workflow)
- [Setup](#-setup)
- [Run the Scripts](#-run-the-scripts)
- [Examples](#-examples)
- [Data Quality and Improvements](#-data-quality-and-improvements)
- [Learning Outcomes](#-learning-outcomes)
- [Author](#-author)

## 🔎 Overview

This folder contains Python practice scripts using **Pandas**, a widely used Python library for working with structured data. Pandas provides the `Series` and `DataFrame` objects, making it easier to inspect CSV files, select columns, filter rows, calculate summaries, and prepare data for visualization or machine learning.

The examples use real-estate, restaurant, and startup-investment datasets. They demonstrate common data-analysis operations and build a foundation for more advanced exploratory data analysis (EDA).

## 🎯 Objectives

- Load CSV files with `pd.read_csv()`.
- Understand DataFrame rows, columns, shapes, and data types.
- Inspect datasets with `head()`, `tail()`, `info()`, and `describe()`.
- Select one or several columns.
- Select rows and columns with `.loc[]`.
- Filter records using conditions.
- Explore real-estate listings and startup information.
- Learn how to identify data-quality issues before analysis.
- Prepare structured data for plotting and machine-learning workflows.

## 🗂️ Files and Datasets

| File | Description |
|---|---|
| `RealEstate-USA.csv` | Property listings containing fields such as price, beds, baths, location, and house size. |
| `RealEstate-USA.py` | Practice with DataFrame inspection, summary statistics, column selection, row selection, and conditional filtering. |
| `Real_Estate_Sales_2001-2022_GL-Short.csv` | Real-estate sales data for additional exploration. |
| `Real_Estate_Sales.py` | Script associated with real-estate sales analysis. |
| `FastFoodRestaurants_fixed_comma.csv` | Restaurant dataset used for tabular-data practice. |
| `FastFoodRestaurants_fixed_comma.py` | Script associated with restaurant data. |
| `startup_growth_investment_data.csv` | Startup information such as country, industry, funding rounds, growth, and valuation. |
| `startup_growth_investment_data.py` | Demonstrates selecting and filtering startup records and columns. |

Exact fields and row counts should be verified against the CSV version in the repository.

## 🧠 Pandas Concepts

### 1. Reading and inspecting data

```python
import pandas as pd

df = pd.read_csv("RealEstate-USA.csv")

print(df.head())
print(df.shape)
print(df.dtypes)
df.info()
print(df.describe())
```

- `head()` shows the first records.
- `tail()` shows the last records.
- `shape` returns the number of rows and columns.
- `dtypes` shows each column's data type.
- `info()` summarizes column types and non-null values.
- `describe()` provides summary statistics for applicable columns.

### 2. Selecting columns

```python
prices = df["price"]
price_and_beds = df[["price", "bed"]]
```

A single column usually returns a Series, while selecting a list of columns returns a DataFrame.

### 3. Selecting rows with `.loc[]`

```python
# Select a row by index label
print(df.loc[1])

# Select multiple row labels
print(df.loc[[1, 3]])

# Filter properties by a condition
affordable = df.loc[df["price"] < 50000]
print(affordable)
```

Remember: `.loc[]` is label-based. Its slicing behavior differs from position-based indexing with `.iloc[]`.

### 4. Conditional filtering

```python
uk_startups = startups.loc[startups["Country"] == "UK"]
```

Filters can be combined with parentheses and bitwise operators such as `&` and `|` when multiple conditions are required.

### 5. Summary statistics and data quality

Pandas provides convenient methods such as `mean()`, `median()`, `value_counts()`, `isna().sum()`, `drop_duplicates()`, and `groupby()`. Always inspect the dataset and business context before deciding how to handle missing values or unusual records.

## 🔄 Typical Workflow

1. Load the source CSV.
2. Inspect dimensions, columns, data types, and sample records.
3. Check missing values and duplicate rows.
4. Select the fields relevant to the analysis.
5. Filter rows using meaningful conditions.
6. Calculate summaries and group-level statistics.
7. Validate the results and document assumptions.
8. Export cleaned data or continue to Seaborn and machine learning.

## ⚙️ Setup

Recommended: Python 3.10 or later.

```bash
python -m venv .venv
```

Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

Install dependencies:

```bash
python -m pip install --upgrade pip
pip install pandas numpy
```

For notebook-based exploration, you can also install Jupyter:

```bash
pip install jupyter
```

## ▶️ Run the Scripts

From the repository root:

```bash
python "3. pandas/RealEstate-USA.py"
python "3. pandas/startup_growth_investment_data.py"
```

**Path note:** Scripts may use either a local filename or a folder-prefixed path. If you see `FileNotFoundError`, make the CSV path consistent with your current working directory. Running from the repository root may require paths such as `3. pandas/RealEstate-USA.csv`; running inside the folder may require only `RealEstate-USA.csv`.

## 📌 Example: A simple analysis

```python
import pandas as pd

df = pd.read_csv("RealEstate-USA.csv")

print("Rows and columns:", df.shape)
print("Missing values by column:")
print(df.isna().sum())

print("Median price:", df["price"].median())

affordable = df.loc[df["price"] < 200000, ["city", "price", "bed", "bath"]]
print(affordable.head(10))
```

Use column names exactly as they appear in the file; capitalization and spaces matter.

## ⚠️ Data Quality and Improvements

- Some datasets can contain missing values, duplicated rows, inconsistent categories, or invalid types.
- A condition's printed description should match the actual comparison; for example, `price < 50000` means less than 50,000, not greater than 50,000.
- `describe()` without parentheses refers to the method itself; call `describe()` to calculate the summary.
- Avoid printing entire large DataFrames when a sample or summary is sufficient.
- Check the meaning and currency of price fields before interpreting their values.
- Document whether missing values are dropped, imputed, or intentionally retained.

## 🚀 Future Improvements

- [ ] Add reusable cleaning functions and validation checks.
- [ ] Use `groupby()` and `agg()` for more detailed analysis.
- [ ] Practice joins, merges, reshaping, and pivot tables.
- [ ] Add charts with Matplotlib and Seaborn.
- [ ] Add automated tests for important transformations.
- [ ] Add a requirements file and document dataset sources.
- [ ] Export cleaned datasets into a clearly named output folder.

## 🎓 Learning Outcomes

This folder provides practice in DataFrame inspection, indexing, filtering, descriptive statistics, and data-quality awareness. Pandas is a key bridge between raw data collection and visualization or machine learning.

## 👨‍💻 Author

**Muhammad Azhar**  
Python • Data Analysis • Data Science • Machine Learning

- GitHub: [@azhar-data](https://github.com/azhar-data)
- Repository: [Nexskill_project](https://github.com/azhar-data/Nexskill_project)

---

<div align="center">Built through hands-on Python and data analysis practice.</div>
