# Steps: load -> clean -> visualise -> encode -> scale -> train models -> tune SVR

 
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
 
# 1. LOAD DATA
# Read the diamonds dataset (53,940 rows, 11 columns) from the csv file
df = pd.read_csv('Project 1/10-diamonds.csv')
print(df)
 
# NOTE: these two lines do nothing in a .py script because the result is not printed.
# (They only show output in Jupyter/Colab.) Wrap them in print() to see the output.
df.head(10)
df.tail(10)
 
# 2. BASIC INSPECTION
# Check the data type of each column and the shape (rows, columns)
print(df.dtypes)
print(df.shape)
 
# Remove duplicate rows

df = df.drop_duplicates()
 
# Statistical summary (mean, std, min, max...) and column info
print(df.describe())
print(df.info())
 
# 3. MISSING VALUES
# Count null values per column
missing = df.isnull().sum()
print("Columns with missing values:", (missing > 0).sum())
print("Total missing cells        :", missing.sum())
 
# Drop the useless index column that came from the csv file
df.drop("Unnamed: 0", axis=1, inplace=True)
 
# 4. REMOVE INVALID DIAMONDS

print(df[df["x"] == 0])
print(len(df[df["x"] == 0]), len(df[df["y"] == 0]), len(df[df["z"] == 0]))
 
# Drop all rows where x, y or z is 0
df = df.drop(df[df["x"] == 0].index)
df = df.drop(df[df["y"] == 0].index)
df = df.drop(df[df["z"] == 0].index)
print(df.describe())
 
# 5. VISUALISATION (to find outliers)

sns.pairplot(df)
plt.show()
 
# SLOW: each scatterplot below draws ~54k points with a colour (hue) for every point.

sns.scatterplot(data=df, x=df.carat, y=df.depth, hue=df.price)
plt.show()
 
sns.scatterplot(data=df, x=df.table, y=df.price, hue=df.price)
plt.show()
 
sns.scatterplot(data=df, x=df.x, y=df.depth, hue=df.price)
plt.show()
 
sns.scatterplot(data=df, x=df.x, y=df.price, hue=df.price)
plt.show()
 
sns.scatterplot(data=df, x=df.z, y=df.price, hue=df.price)
plt.show()
 
sns.scatterplot(data=df, x=df.z, y=df.price, hue=df.price)
plt.show()
 
# 6. REMOVE OUTLIERS
# Based on the plots, keep only realistic values.
df = df[(df["z"] < 10) & (df["z"] > 2)]          # height between 2 and 10 mm
df = df[df["y"] < 20]                            # width below 20 mm
df = df[(df["table"] < 75) & (df["table"] > 40)] # table % between 40 and 75
df = df[(df["depth"] < 75) & (df["depth"] > 45)] # depth % between 45 and 75
 
# Plot again to confirm the outliers are gone
sns.scatterplot(data=df, x=df.z, y=df.price, hue=df.price)
plt.show()
 
# SLOW again: a second full pairplot
sns.pairplot(df)
plt.show()
 
# Count of each category (cut, color, clarity).
df.cut.value_counts(), df.color.value_counts(), df.clarity.value_counts()
 
# 7. SPLIT FEATURES / TARGET
x = df.drop("price", axis=1)  # input features
y = df["price"]               # target we want to predict
 
# 75% train, 25% test. random_state keeps the split the same every run.
from sklearn.model_selection import train_test_split
xtrain, xtest, ytrain, ytest = train_test_split(x, y, test_size=0.25, random_state=15)
 
# 8. ENCODE CATEGORICAL COLUMNS
# Models need numbers, so convert text columns (cut, color, clarity) into integers.
from sklearn.preprocessing import LabelEncoder
 
label_enc = LabelEncoder()
 
for col in ["cut", "color", "clarity"]:
    # fit on train only, then apply the same mapping to test (avoids data leakage)
    xtrain[col] = label_enc.fit_transform(xtrain[col])
    xtest[col] = label_enc.transform(xtest[col])
 
print(xtrain)
 
# 9. FEATURE SCALING
# Standardise features (mean 0, std 1). This is essential for SVR.
from sklearn.preprocessing import StandardScaler
 
scale = StandardScaler()
 
xtrain_scale = scale.fit_transform(xtrain)  # learn mean/std from train and apply
xtest_scale = scale.transform(xtest)        # apply the same values to test
 
# 10. MODEL 1: LINEAR REGRESSION
# NOTE: LogisticRegression is imported but never used (it is for classification, not regression)
from sklearn.linear_model import LinearRegression, LogisticRegression
 
linear_model = LinearRegression()
linear_model.fit(xtrain_scale, ytrain)
ypred = linear_model.predict(xtest_scale)
 
# Evaluation metrics: R2 (higher is better), the rest (lower is better)
from sklearn.metrics import (r2_score, mean_absolute_error,
                             mean_squared_error, mean_absolute_percentage_error)
print("R2   :", r2_score(ytest, ypred))
print("MAE  :", mean_absolute_error(ytest, ypred))
print("MSE  :", mean_squared_error(ytest, ypred))
print("RMSE :", np.sqrt(mean_squared_error(ytest, ypred)))
print("MAPE :", mean_absolute_percentage_error(ytest, ypred))
 
# 11. MODEL 2: XGBOOST
# Gradient boosted trees, usually very accurate and fast on tabular data
from xgboost import XGBRegressor
 
xgb_model = XGBRegressor()
xgb_model.fit(xtrain_scale, ytrain)
 
ypred = xgb_model.predict(xtest_scale)
print("R2   :", r2_score(ytest, ypred))
print("MAE  :", mean_absolute_error(ytest, ypred))
print("MSE  :", mean_squared_error(ytest, ypred))
print("RMSE :", np.sqrt(mean_squared_error(ytest, ypred)))
print("MAPE :", mean_absolute_percentage_error(ytest, ypred))
 
# 12. MODEL 3: SVR (Support Vector Regression)
# SLOW: SVR training time grows roughly with the square of the number of rows.
# With ~40k training rows even ONE fit takes a while (minutes).
from sklearn.svm import SVR
 
svr = SVR()
svr.fit(xtrain_scale, ytrain)
ypred = svr.predict(xtest_scale)
print("R2   :", r2_score(ytest, ypred))
print("MAE  :", mean_absolute_error(ytest, ypred))
print("MSE  :", mean_squared_error(ytest, ypred))
print("RMSE :", np.sqrt(mean_squared_error(ytest, ypred)))
print("MAPE :", mean_absolute_percentage_error(ytest, ypred))
 
# Actual vs predicted prices (the closer to a straight diagonal line, the better)
plt.scatter(ytest, ypred)
plt.show()
 
# 13. HYPERPARAMETER TUNING: GRIDSEARCHCV ON SVR

param = {
    "kernel": ["rbf", "linear"],
    "C": [0.1, 1, 10, 100, 1000],
    "gamma": [1, 0.1, 0.001]
}
from sklearn.model_selection import GridSearchCV
grid = GridSearchCV(estimator=SVR(), param_grid=param, n_jobs=-1, verbose=3)
grid.fit(xtrain_scale, ytrain)
 
# Best parameters and best cross-validation R2 score
print(grid.best_params_)
print(grid.best_score_)
 
# Predict on test data using the best model found
ypred = grid.predict(xtest_scale)
 
print("R2   :", r2_score(ytest, ypred))
print("MAE  :", mean_absolute_error(ytest, ypred))
print("MSE  :", mean_squared_error(ytest, ypred))
print("RMSE :", np.sqrt(mean_squared_error(ytest, ypred)))
print("MAPE :", mean_absolute_percentage_error(ytest, ypred))
plt.scatter(ytest, ypred)
plt.show()
