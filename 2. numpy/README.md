<div align="center">

# 🔢 NumPy — Numerical Computing with Python

### Arrays • Vectorized Operations • Statistics • Real-World Datasets

![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-Numerical%20Computing-013243?style=for-the-badge&logo=numpy&logoColor=white)
![Status](https://img.shields.io/badge/Focus-Learning%20%26%20Practice-blue?style=for-the-badge)

**A hands-on collection of Python scripts that practice NumPy fundamentals through restaurant and real-estate datasets.**

</div>

---

## 📚 Contents

- [Overview](#-overview)
- [Learning Objectives](#-learning-objectives)
- [Datasets and Scripts](#-datasets-and-scripts)
- [Concepts Practiced](#-concepts-practiced)
- [Workflow](#-workflow)
- [Installation](#-installation)
- [Run the Examples](#-run-the-examples)
- [Code Examples](#-code-examples)
- [Data Quality Notes](#-data-quality-notes)
- [Future Improvements](#-future-improvements)
- [Author](#-author)

## 🔎 Overview

This folder demonstrates how **NumPy** can load, store, inspect, and calculate statistics on structured data without relying on a full DataFrame workflow. The examples use restaurant and real-estate CSV files to make array operations practical and understandable.

NumPy is a foundational library for numerical computing in Python. It provides efficient multidimensional arrays, mathematical functions, aggregation, indexing, and tools for working with missing numerical values. These skills are useful in data analysis, scientific computing, and machine learning.

## 🎯 Learning Objectives

- Import and use NumPy.
- Read CSV data using `np.genfromtxt()`.
- Work with arrays and structured arrays.
- Select columns and inspect data types.
- Calculate mean, median, standard deviation, variance, minimum, maximum, range, and percentiles.
- Find the positions of minimum and maximum values.
- Explore correlation and covariance between numerical variables.
- Handle missing numeric values with NaN-aware functions.
- Practice basic mathematical and array operations.
- Understand how raw data can be prepared for later analysis.

## 🗂️ Datasets and Scripts

| File | Purpose |
|---|---|
| `FastFoodRestaurants_fixed_comma.csv` | Restaurant data used to practice extracting location-related fields and numerical analysis. |
| `FastFoodRestaurants_fixed_comma.py` | Loads restaurant fields such as latitude, longitude, name, and province; calculates statistics and relationships. |
| `RealEstate-USA.csv` | Property listings dataset used to practice numerical analysis on price, beds, baths, house size, and related fields. |
| `RealEstate-USA.py` | Loads real-estate data into a NumPy structured array and explores prices, measurements, and locations. |
| `Real_Estate_Sales_2001-2022_GL-Short.csv` | Real-estate sales dataset for additional practice. |
| `Real_Estate_Sales_2001-2022_GL-Short.py` | Script associated with the real-estate sales dataset. |
| `startup_growth_investment_data.csv` | Startup and investment dataset for numerical-analysis practice. |
| `startup_growth_investment_data.py` | Script associated with the startup dataset. |

Dataset column names and available records can vary by file version. Inspect each CSV before assuming a particular schema.

## 🧠 Concepts Practiced

### Loading structured CSV data

`np.genfromtxt()` can read delimited data, infer or accept data types, and represent missing numerical values as `np.nan`. When a dataset includes both text and numbers, a structured array can preserve named fields.

### Descriptive statistics

Examples use operations such as:

- `np.mean()` and `np.average()`
- `np.median()`
- `np.std()` and `np.var()`
- `np.min()`, `np.max()`, and `np.ptp()`
- `np.percentile()`
- `np.argmin()` and `np.argmax()`

These functions summarize distributions and help identify extreme observations.

### Correlation and covariance

`np.corrcoef()` calculates correlation coefficients, while `np.cov()` estimates covariance. They describe statistical relationships between numerical variables; correlation alone does not prove causation.

### NaN-aware calculations

When numeric columns contain missing values represented as NaN, functions such as `np.nanmean()`, `np.nanmedian()`, and `np.nansum()` can avoid treating NaNs as ordinary values. They do not replace the need to investigate why values are missing.

## 🔄 Typical Workflow

1. Read a CSV file.
2. Inspect array shape, field names, and data types.
3. Select the columns relevant to the question.
4. Check for missing, invalid, or inconsistent values.
5. Calculate descriptive statistics.
6. Compare variables and investigate unusual values.
7. Record findings before moving to visualization or machine learning.

## ⚙️ Installation

Recommended: Python 3.10 or later.

Create and activate a virtual environment if desired, then install NumPy:

```bash
python -m venv .venv
```

Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

Install the dependency:

```bash
python -m pip install --upgrade pip
pip install numpy
```

## ▶️ Run the Examples

Open a terminal in the repository and enter the folder:

```bash
cd "2. numpy"
```

Then run a script, for example:

```bash
python FastFoodRestaurants_fixed_comma.py
python RealEstate-USA.py
```

**Path note:** Some scripts may refer to paths such as `numpy/RealEstate-USA.csv`. If you run a script from inside this folder and see a file-not-found error, change the path to the local filename (for example, `RealEstate-USA.csv`) or run the script from the directory expected by the code. Keep the CSV and its script in the intended relative locations.

## 💡 Code Examples

### Basic statistics

```python
import numpy as np

prices = np.array([120000, 180000, 250000, 310000], dtype=float)

print("Mean:", np.mean(prices))
print("Median:", np.median(prices))
print("Minimum:", np.min(prices))
print("Maximum:", np.max(prices))
print("Standard deviation:", np.std(prices))
```

### Handling missing numeric values

```python
import numpy as np

values = np.array([10.0, 20.0, np.nan, 40.0])

print("Mean ignoring NaN:", np.nanmean(values))
print("Missing values:", np.isnan(values).sum())
```

## ⚠️ Data Quality Notes

- Confirm that columns intended for arithmetic are numeric.
- CSV files containing commas inside text fields must be properly quoted; otherwise, columns can shift during parsing.
- Check for missing values before using ordinary functions such as `np.mean()`.
- Numeric codes for categories should not automatically be interpreted as meaningful quantities.
- Statistics depend on the data that was actually loaded and cleaned.

## 🚀 Future Improvements

- [ ] Add unit tests for data loading and numerical calculations.
- [ ] Compare NumPy results with equivalent Pandas summaries.
- [ ] Add clear handling for invalid rows and missing values.
- [ ] Create reusable functions for repeated statistical operations.
- [ ] Add Matplotlib charts for distributions and relationships.
- [ ] Document each dataset's source and license.
- [ ] Add a requirements file for reproducible setup.

## 🎓 Learning Outcomes

This folder builds a foundation in array-based computation, descriptive statistics, missing-value handling, and structured numerical data. These are core skills for later work with Pandas, data visualization, feature engineering, and machine learning.

## 👨‍💻 Author

**Muhammad Azhar**  
Python • Data Analysis • Data Science • Machine Learning

- GitHub: [@azhar-data](https://github.com/azhar-data)
- Repository: [Nexskill_project](https://github.com/azhar-data/Nexskill_project)

---

<div align="center">Made for hands-on learning and continuous improvement.</div>
