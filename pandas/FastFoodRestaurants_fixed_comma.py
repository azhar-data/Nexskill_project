import pandas as pd 



df=pd.read_csv('FastFoodRestaurants_fixed_comma.csv',delimiter=",")


print(df)
print(type(df))

print("Dtypes value:",df.dtypes)
print("info value:",df.info())

print("First ten lines")
print(df.head(10))

print("last 2 lines")
print(df.tail(2))

print("decrsibe the statics value of the number:",df.describe())
#count rows and colums in the file
print("the Rows and colums shape:",df.shape)
print()

address=df['address']
print('Acess the nme of colum :df')
print(address)
print()


city_key=df[['city','keys']]
print('Access the multiple colum usin: df:')
print(city_key)
print()


first_row=df.loc[1]
print('seleting the single row using .loc :')
print(first_row)
print()

first_row2=df.loc[[1,3]]
print('selecting a mulitple row using .loc:')
print(first_row2)
print()

first_row3=df.loc[1:7]
print('selecting a slice of the row using .loc:')
print(first_row3)
print()

first_row4=df.loc[df['city']=='Massena']
print('condit selection of row using .loc :')
print(first_row4)
print()

first_row5=df.loc[:5,'address']
print('selecting a single colum of using .loc :')
print(first_row5)
print()

first_row6=df.loc[:,['address','city']]
print('selecting a multipel colum using .loc')
print(first_row6)
print()

first_row7=df.loc[:1,'address':'name']
print('selecting a slice of the colum using .loc')
print(first_row7)
print()

first_row8=df.loc[df['city']=='Massena','keys':'name']
print('seleting a muliple rows or colums using .loc :')
print(first_row8)
print()

#=====================================================================
# Case 1 : using .loc - default case - ends here
#=====================================================================

print(' Case 1 : using .loc - default case - ends here')

df_index_col=pd.read_csv('FastFoodRestaurants_fixed_comma.csv',delimiter=',')
print(df_index_col)
print()

print(df_index_col.dtypes)
print(df_index_col.info())

print(df_index_col.shape)
print(df_index_col.describe)

first_row=df_index_col.loc[1000]
print('select a single colum using .loc :')
print(first_row)
print()

first_row2=df_index_col.loc[[32,67]]
print('seleting a multiple colum using .loc')
print(first_row2)
print()

first_row3=df_index_col.loc[1:9999]
print('selecting a slice of rows using .loc')
print(first_row3)
print()

first_row4=df_index_col.loc[df_index_col['address']==4182]
print('selecting a single colum using .loc :')
print(first_row4)
print()

first_row5=df_index_col.loc[:90909,'name']
print('selecting a single colum using .loc')
print(first_row5)
print()


first_row6=df_index_col.loc[:67,['address','keys']]
print('selecting a multiple colum using .loc')
print(first_row6)
print()

first_row7=df_index_col.loc[:12,'city':'name']
print('selecting a slice of colum using .loc :')
print(first_row7)
print()


first_row8=df_index_col.loc[df_index_col['address']=='530 Clinton Ave','keys':'name']
print('combined rows and colums selection using .loc:')
print(first_row8)
print()



#case 3 using .iloc
second_row=df_index_col.iloc[0]
print(second_row)
print()

second_row2=df.iloc[[1,4,9]]
print('selecting a multiple rows using .iloc :')
print(second_row2)
print()

second_row3=df_index_col.iloc[2:9]
print('selecting a slice of rows using .iloc')
print(second_row3)
print()

second_row4=df_index_col.iloc[:,6]
print('selecting a single colum using .iloc')
print(second_row4)
print()

second_row5=df_index_col.iloc[:,[4,5]]
print('selecting a multiple colum using .iloc')
print(second_row5)
print()

second_row6=df_index_col.iloc[:,2:5]
print('selecting a slice of colum using .iloc:')
print(second_row6)
print()

second_row7=df_index_col.iloc[[1,5,10],1:6]
print('selecting a combien rows and colums using .iloc')
print(second_row7)
print()

print('.iloc method are he end of the program now the next part are start:')

print('Run the next part')

df.loc[len(df.index)]=['205 W Church St','Batesburg','US','us/sc/batesburg/205wchurchst/-791445730',33.91335,-81.5333,'Wendy',29006,'SC','http://www.wendys.com']
print('modified new line ')
print(df)


df.drop(1, axis=0,inplace=True)

df.drop(index=2,inplace=True)

df.drop([4,7],axis=0,inplace=True)

print("Modified DataFrame - Remove Rows:")
print(df)

df.drop('name',axis=1,inplace=True)
print(df)

df.drop(columns='address',inplace=True)
print(df)

df.drop(['country','city'],axis=1,inplace=True)

print("Modified DataFrame")
print(df)

df.rename(index={3:8},inplace=True)

df.rename(mapper={10:11,20:100},axis=0,inplace=True)
print("Modified DataFrame")
print(df)

df.rename(columns={'websites':'websites_name_changed'},inplace=True)

df.rename(columns={'keys':'keys_changed'},inplace=True)
print(df)

#query() to Select Data
#The query() method in Pandas allows you to select data using a more SQL-like syntax.

# select the rows where the age is greater than 25



df['postalCode'] = pd.to_numeric(df['postalCode'], errors='coerce')
selected_rows = df.query('province == "KY" or postalCode > 190')
print(selected_rows.to_string())
print(len(selected_rows))

print(df['postalCode'].isnull().sum())

sorted_df=df.sort_values(by='postalCode')
print(sorted_df.to_string(index=True))


df1=df.sort_values(by=['postalCode','province'])
print(df1.to_string(index=False))
print(sorted_df.head())   # index (0,1,2...) bhi dikhega


#Pandas groupby
#In Pandas, the groupby operation lets us group data based on specific columns. This means we can divide a DataFrame into smaller groups based on the values in these columns.

# group the DataFrame by the location_id column and
# calculate the sum of price for each category
grouped=df.groupby('postalCode')['province'].sum()

print(grouped.to_string())
print('grouped :',len(grouped))


#df_cleaned=df.dropna()
#print('cleaned Data :\n',df_cleaned)

# filling NaN values with 0
df.info()
df["postalCode"] = df["postalCode"].fillna(0)
df["websites_name_changed"] = df["websites_name_changed"].fillna("Unknown")
df.fillna(0, inplace=True)

print("\nData after filling NaN with 0:\n", df)

data=[1,3,5,7]
#create array
array1=pd.array(data)
print(array1)


int_array=pd.array([1,2,3,4,5,6,7,8],dtype='int')
print(int_array)
print()
print('End')