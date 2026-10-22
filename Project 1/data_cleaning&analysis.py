import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#load data from csv file
df=pd.read_csv('Project 1/University_Entrepreneurship_Feasibility_Dataset1.csv')
print(df)

df.head(10)
df.tail(10)

#check the data type
print(df.dtypes)
print(df.shape)

#duplicate rows remove
df=df.drop_duplicates()
print("Duplicate rows (ignoring the ID)  :", df.drop(columns="ID").duplicated().sum())

print(df)

#decribe the data
print(df.describe())
print(df.info())

#check null value
missing = df.isnull().sum()
print("Columns with missing values:", (missing > 0).sum())
print("Total missing cells        :", missing.sum())

#Remove columns that carry no learning information.

df=df.drop(columns=['ID'])

#Check the target column for typos or odd spellings
print(df["Feasibility_Status"].value_counts())

# Define inputs (X) and target (y).

y = df["Feasibility_Status"]
X = df.drop(columns=["Feasibility_Status", "Feasibility_Score"])
print("X shape:", X.shape, "| y shape:", y.shape)

key_features = ["Market_Potential", "Profitability_Estimation", "Innovation_Capability",
                "Financial_Risk", "Leadership_Ability", "Technical_Skills"]
# data viszulation 
#Target distribution
status_map = {"Not_Feasible": 0, "Partially_Feasible": 1, "Fully_Feasible": 2}
class_names = list(status_map.keys())
fig, ax = plt.subplots()
sns.countplot(data=df, x="Feasibility_Status", order=class_names, palette="Blues_r", ax=ax)
for bar in ax.patches:
    ax.annotate(int(bar.get_height()), (bar.get_x() + bar.get_width() / 2, bar.get_height()),
                ha="center", va="bottom")
plt.show()

#Distribution of the score
fig, ax = plt.subplots()
sns.histplot(df["Feasibility_Score"], bins=40, kde=True, color="#1f5fbf", ax=ax)
plt.show()

#Histograms of important features
fig, axes = plt.subplots(2, 3, figsize=(14, 7))
for ax, col in zip(axes.ravel(), key_features):
    sns.histplot(df[col], bins=30, kde=True, color="#2f7de1", ax=ax)
    ax.set_title(col)
plt.tight_layout()
plt.show()


