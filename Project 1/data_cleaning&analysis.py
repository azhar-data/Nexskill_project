import numpy as np
import pandas as pd

#load data from csv file
df=pd.read_csv('Project 1/University_Entrepreneurship_Feasibility_Dataset1.csv')
print(df)

#check the data type
print(df.dtypes)
print(df.shape)

#duplicate rows remove
df=df.drop_duplicates()
print(df)

#decribe the data
print(df.describe())
print(df.info())

#check null value
print(df.isna().sum())

#
