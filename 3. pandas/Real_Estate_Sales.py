import pandas as pd 
df=pd.read_csv('Real_Estate_Sales_2001-2022_GL-Short.csv',delimiter=',')
print(df)

print(df.dtypes)
print(df.shape)
print()

print(df.info())
print(len(df))
print()

print('First three rows:')
print(df.head(3))
print()

print('Last ten rows:')
print(df.tail(10))
print()

print('statics of the rows:')
print(df.describe())
print()

Serial_Number=df['Serial Number']
print(Serial_Number)
print()

OPM_remarks_Location=df[['OPM remarks','Location']]
print(OPM_remarks_Location)
print()

second_row=df.loc[1]
print('select a single row using .loc :')
print(second_row)
print()

second_row2=df.loc[1:90]
print('select a slice of rows using .loc :')
print(second_row2)
print()

second_row3=df.loc[[1,3,9]]
print('select a multiple colums using .loc :')
print(second_row3)
print()

second_row4=df.loc[df['Serial Number']==2020177]
print('conditional selecting using .loc :')
print(second_row4)
print()

second_row5=df.loc[df['Serial Number']==2020177,'Serial Number':'Location']
print('select a cobination of rows and colums:')
print(second_row5)
print()

second_row6=df.loc[:1,'Location']
print('select a single colums using .loc :')
print(second_row6)
print()

second_row7=df.loc[:3,['Serial Number','Location']]
print('select a multiple of colums using .loc :')
print(second_row7)
print()

second_row8=df.loc[:6,'Serial Number':'Location']
print('select a slice of colums using .loc :')
print(second_row8)
print()

print("# Case 2 : using .loc with index_col - starts here")
# Case 2 : using .loc with index_col - starts here
# Second cycle - with index_col as property_id
# Why Second cycle - Note Index - , index_col='property_id'

second_row=df.iloc[1]
print('select a single row using .iloc :')
print(second_row)
print()

second_row=df.iloc[1:80]
print('Select a slice of rows using .iloc :')
print(second_row2)
print()

second_row3=df.iloc[[1,8]]
print('select a multiple rows using .iloc :')
print(second_row3)
print()

second_row4=df.iloc[:,2]
print('select a single colum using .iloc :')
print(second_row4)
print()

second_row5=df.iloc[:,1:9]
print('Select a slice of colums using .iloc :')
print(second_row5)
print()

second_row6=df.iloc[:,[2,9]]
print('select a multiple colums using .iloc :')
print(second_row6)
print()

second_row7=df.iloc[[1,4,9],2:5]
print('Select a combined row and colums using .iloc :')
print(second_row7)
print()

second_row8=df.iloc[[1,3,4],[2,9]]
print('select a combined of rows and colums using :')
print(second_row8)
print()

print('End here')

print('Next Run')
print()

#add new line
df.loc[len(df.index)]=[1,2,3,4,5,6,7,89,14,13,19,10,13,12]
print(df)
print()
print()

df.drop(1,axis=0,inplace=True)
print(df)
print()

df.drop(index=2,inplace=True)
print(df)
print()

df.drop([3,4],axis=0,inplace=True)
print(df)
print()

df.drop('OPM remarks',axis=1,inplace=True)
print(df)
print()

df.drop(columns=['Location','Town'],inplace=True)
print(df)
print()

df.rename(columns={'Serial Number':'changed_Serial_Number'},inplace=True)
print(df)
print()

df.rename(mapper={'Assessor Remarks':'changed_Assessor_Remarks','changed_Serial_Number':'Serial Number'},axis=1,inplace=True)
print(df)
print()

#second_rows=df.query(" `Serial Number`==20058 or `List Year` >2020")
second_rows=df.query("`Serial Number`==20058 or `List Year` >2020")
print(second_rows.to_string())
print()

print(len(second_rows))
print()

sorted_df=df.sort_values(by='Serial Number')
print(sorted_df.to_string(index=False))

df1=df.sort_values(by=['Sale Amount','Address'])
print(df1.to_string(index=False))



"""
Reference: https://www.geeksforgeeks.org/python-pandas-dataframe-to_string/
Explanation: This code creates a DataFrame from a dictionary with three columns (Weight, Name, Age), structures it into a tabular format using pd.DataFrame() and converts it into a fully visible string representation with df.to_string().

Syntax
DataFrame.to_string(buf=None, columns=None, col_space=None, header=True, index=True, na_rep=’NaN’, formatters=None, float_format=None, sparsify=None, index_names=True, justify=None, max_rows=None, max_cols=None, show_dimensions=False, decimal=’.’, line_width=None)


Parameters:

buf: Buffer to write the output string to (e.g., a file). Defaults to None, which means the output is returned as a string.
columns: Specifies a subset of columns to include in the output. If None, all columns are printed.
col_space: Defines the minimum width of each column.
header: Whether to print column names. Can also accept a list of column name aliases.
index: Whether to include index labels. Default is True.
na_rep: String representation for missing values (NaN). Default is ‘NaN’.
formatters: Dictionary or list of functions to apply to columns for formatting their output.
float_format: Formatter function to apply specifically to floating-point numbers.
sparsify: Controls hierarchical index formatting. If False, prints every multi-index key at each row.
index_names: Whether to print index names. Default is True.
justify: Alignment of column headers (‘left’, ‘right’, ‘center’, ‘justify’ or ‘justify-all’).
max_rows: Maximum number of rows to display. If exceeded, truncates output.
max_cols: Maximum number of columns to display. If exceeded, truncates output.
show_dimensions: If True, displays the shape (rows x columns) of the DataFrame.
decimal: Specifies the character for decimal separation (e.g., ‘,’ for European formatting).
line_width: Defines the maximum character width of a row before wrapping text."""



#Pandas groupby
#In Pandas, the groupby operation lets us group data based on specific columns. This means we can divide a DataFrame into smaller groups based on the values in these columns.

# group the DataFrame by the location_id column and
# calculate the sum of price for each category
grouped=df.groupby('Sale Amount')['Address'].sum()
print(grouped.to_string())
print(len(grouped))


df_cleaned=df.dropna()
print('cleaned data :\n',df_cleaned)
print()

df.fillna('o',inplace=True)
print(df)

data = [2, 4, 6, 8]
# create Pandas array using data
array1 = pd.array(data)
print(array1)
"""<IntegerArray>
[2, 4, 6, 8]
Length: 4, dtype: Int64"""


# creating a pandas.array of integers
int_array = pd.array([1, 2, 3, 4, 5], dtype='int')
print(int_array)
print()
