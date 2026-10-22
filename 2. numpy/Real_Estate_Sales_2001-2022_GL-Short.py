
import numpy as np
 
# 1. LOAD THE DATA
year, town, assessed, sale, ratio, ptype = np.genfromtxt('numpy/Real_Estate_Sales_2001-2022_GL-Short.csv', delimiter=',', usecols=(1,3,5,6,7,8), unpack=True, skip_header=1, invalid_raise=False, dtype=None, encoding='utf-8')
 
print("Real Estate Year: ", year)
print("Real Estate Town: ", town)
print("Real Estate Assessed Value: ", assessed)
print("Real Estate Sale Amount: ", sale)
print("Real Estate Sales Ratio: ", ratio)
print("Real Estate Property Type: ", ptype)
 
print("Real Estate Sale Amount data type: ", sale.dtype)
print("Real Estate Town data type: ", town.dtype)
print("Real Estate total sales: ", sale.size)
 
 
# 2. STATISTICS OPERATIONS (sale amount)
print("Real Estate Sale mean: " , np.mean(sale))
print("Real Estate Sale average: " , np.average(sale))
print("Real Estate Sale median: " , np.median(sale))
print("Real Estate Sale std: " , np.std(sale))
print("Real Estate Sale variance: " , np.var(sale))
print("Real Estate Sale min : " , np.min(sale))
print("Real Estate Sale max : " , np.max(sale))
print("Real Estate Sale range (max - min): " , np.ptp(sale))
print("Real Estate Sale sum: " , np.sum(sale))
print("Real Estate Sale percentile - 3: " , np.percentile(sale,3))
print("Real Estate Sale percentile - 25: " , np.percentile(sale,25))
print("Real Estate Sale percentile - 50: " , np.percentile(sale,50))
print("Real Estate Sale percentile - 75: " , np.percentile(sale,75))
print("Real Estate Sale percentile - 97: " , np.percentile(sale,97))
 
# index of the smallest and biggest value
print("Real Estate Sale argmin (index of min): " , np.argmin(sale))
print("Real Estate Sale argmax (index of max): " , np.argmax(sale))
print("Real Estate cheapest sale town and type: " , town[np.argmin(sale)], ptype[np.argmin(sale)])
print("Real Estate most expensive sale town and type: " , town[np.argmax(sale)], ptype[np.argmax(sale)])
 
 
# 3. STATISTICS OPERATIONS (assessed value and sales ratio)
print("Real Estate Assessed mean: " , np.mean(assessed))
print("Real Estate Assessed median: " , np.median(assessed))
print("Real Estate Assessed std: " , np.std(assessed))
print("Real Estate Assessed min : " , np.min(assessed))
print("Real Estate Assessed max : " , np.max(assessed))
 
print("Real Estate Ratio mean: " , np.mean(ratio))
print("Real Estate Ratio median: " , np.median(ratio))
print("Real Estate Ratio std: " , np.std(ratio))
print("Real Estate Ratio min : " , np.min(ratio))
print("Real Estate Ratio max : " , np.max(ratio))
 
# correlation between assessed value and sale amount
print("Real Estate Assessed - Sale correlation matrix: " , np.corrcoef(assessed, sale))
print("Real Estate Assessed - Sale covariance matrix: " , np.cov(assessed, sale))
 
 
# 4. MATHS OPERATIONS
print("Real Estate Sale square: " , np.square(sale))
print("Real Estate Sale sqrt: " , np.sqrt(sale))
print("Real Estate Sale abs: " , np.abs(sale))
print("Real Estate Ratio round (2 decimals): " , np.round(ratio, 2))
print("Real Estate Ratio floor: " , np.floor(ratio))
print("Real Estate Ratio ceil: " , np.ceil(ratio))
 
 
# 5. BASIC ARITHMETIC (sale and assessed)
addition = sale + assessed
subtraction = sale - assessed
multiplication = sale * assessed
division = assessed / sale
 
print("Real Estate Sale - assessed - Addition:", addition)
print("Real Estate Sale - assessed - Subtraction (profit over assessed):", subtraction)
print("Real Estate Sale - assessed - Multiplication:", multiplication)
print("Real Estate Assessed / Sale - Division (same idea as Sales Ratio):", division)
 
# arithmetic with a single number (broadcasting)
print("Real Estate Sale + 1000: ", sale + 1000)
print("Real Estate Sale * 2: ", sale * 2)
print("Real Estate Sale in thousands: ", sale / 1000)
 
# 10 percent tax on every sale
tax = sale * 0.10
print("Real Estate 10 percent tax on each sale: ", tax)
print("Real Estate Sale plus 10 percent tax: ", sale + tax)
 
 
# 6. TRIGONOMETRIC, EXPONENTIAL AND LOGARITHM FUNCTIONS

salePie = (sale / 1000000) + 1
 
sine_values = np.sin(salePie)
cosine_values = np.cos(salePie)
tangent_values = np.tan(salePie)
 
print("Real Estate Sale - scaled - Sine values:", sine_values)
print("Real Estate Sale - scaled - Cosine values:", cosine_values)
print("Real Estate Sale - scaled - Tangent values:", tangent_values)
 
print("Real Estate Sale - scaled - Exponential values:", np.exp(salePie))
 
log_array = np.log(salePie)
log10_array = np.log10(salePie)
print("Real Estate Sale - scaled - Natural logarithm values:", log_array)
print("Real Estate Sale - scaled - Base-10 logarithm values:", log10_array)
 
# log of the real sale amount (very common for prices)
print("Real Estate Sale natural log: ", np.log(sale))
print("Real Estate Sale log10: ", np.log10(sale))
 
# degrees and radians
print("Real Estate Ratio in radians: ", np.radians(ratio))
print("Real Estate Ratio radians back to degrees: ", np.degrees(np.radians(ratio)))
 
# hyperbolic functions
print("Real Estate Sale - scaled - Hyperbolic Sine values:", np.sinh(salePie))
print("Real Estate Sale - scaled - Hyperbolic Cosine values:", np.cosh(salePie))
print("Real Estate Sale - scaled - Hyperbolic Tangent values:", np.tanh(salePie))
print("Real Estate Sale - scaled - Inverse Hyperbolic Sine values:", np.arcsinh(salePie))
print("Real Estate Sale - scaled - Inverse Hyperbolic Cosine values:", np.arccosh(salePie))
 
 
# 7. SORTING, CUMULATIVE AND DIFFERENCE
print("Real Estate Sale sorted (small to big): ", np.sort(sale))
print("Real Estate Sale sorted (big to small): ", np.sort(sale)[::-1])
 
order = np.argsort(sale)
print("Real Estate Towns sorted by sale amount: ", town[order])
print("Real Estate Top 5 most expensive towns: ", town[order][::-1][:5])
print("Real Estate Top 5 most expensive sale amounts: ", sale[order][::-1][:5])
print("Real Estate Top 5 cheapest sale amounts: ", sale[order][:5])
 
print("Real Estate Sale cumulative sum: ", np.cumsum(sale))
print("Real Estate Sale difference between neighbours: ", np.diff(sale))
 
 
# 8. BOOLEAN FILTERING AND np.where
expensive = sale > np.median(sale)
print("Real Estate sales above the median (True/False): ", expensive)
print("Real Estate sales above the median (count): ", np.sum(expensive))
 
million = sale >= 1000000
print("Real Estate sales of 1 million or more (count): ", np.sum(million))
print("Real Estate sales of 1 million or more (towns): ", town[million])
print("Real Estate sales of 1 million or more (amounts): ", sale[million])
 
# two conditions together: & means AND, | means OR
cheap_residential = (sale < 200000) & (ptype == "Residential")
print("Real Estate Residential sales under 200000 (count): ", np.sum(cheap_residential))
 
# np.where gives the index positions that match
print("Real Estate index positions where sale is above 2 million: ", np.where(sale > 2000000))
 
# np.where with three arguments: pick one value or another
price_level = np.where(sale > np.median(sale), "High", "Low")
print("Real Estate price level (High or Low): ", price_level)
 
# sold for MORE than the assessed value (sales ratio below 1) or LESS
sold_above = ratio < 1
print("Real Estate sold above assessed value (count): ", np.sum(sold_above))
print("Real Estate sold below assessed value (count): ", np.sum(~sold_above))
print("Real Estate percent sold above assessed value: ", np.mean(sold_above) * 100)
 
# ratio above 1 can be a foreclosure or a special sale
print("Real Estate towns with ratio above 1: ", town[ratio > 1])
 
 
# 9. COUNTING TEXT DATA (town and property type)
unique_type, type_counts = np.unique(ptype, return_counts=True)
print("Real Estate unique property types: ", unique_type)
print("Real Estate counts per property type: ", type_counts)
 
unique_town, town_counts = np.unique(town, return_counts=True)
print("Real Estate number of unique towns: ", unique_town.size)
 
# top 5 towns by number of sales
top = np.argsort(town_counts)[::-1][:5]
for t, c in zip(unique_town[top], town_counts[top]):
    print("Real Estate top town by sales count - ", t, ":", c)
 
# mean sale amount for each property type
for p in unique_type:
    print("Real Estate property type", p, "mean sale: ", np.mean(sale[ptype == p]))
    print("Real Estate property type", p, "median sale: ", np.median(sale[ptype == p]))
    print("Real Estate property type", p, "max sale: ", np.max(sale[ptype == p]))
 
# mean sale amount for each of the top 5 towns
for t in unique_town[top]:
    print("Real Estate town", t, "mean sale: ", np.mean(sale[town == t]))
 
# town with the highest average sale
town_mean = np.array([np.mean(sale[town == t]) for t in unique_town])
print("Real Estate town with the highest average sale: ", unique_town[np.argmax(town_mean)], np.max(town_mean))
print("Real Estate town with the lowest average sale: ", unique_town[np.argmin(town_mean)], np.min(town_mean))
 
# Residential only
res = (ptype == "Residential")
print("Real Estate Residential sales (count): ", np.sum(res))
print("Real Estate Residential mean sale: ", np.mean(sale[res]))
print("Real Estate Residential mean ratio: ", np.mean(ratio[res]))
 
 
# 10. YEAR AND ASSESSED VALUE CHECKS
print("Real Estate unique list years: ", np.unique(year))
print("Real Estate min year: ", np.min(year))
print("Real Estate max year: ", np.max(year))
 
# how much did the sale go above the assessed value, in percent
gain_percent = ((sale - assessed) / assessed) * 100
print("Real Estate gain over assessed value (percent): ", gain_percent)
print("Real Estate mean gain over assessed value (percent): ", np.mean(gain_percent))
print("Real Estate biggest gain over assessed value (percent): ", np.max(gain_percent))
print("Real Estate biggest gain town: ", town[np.argmax(gain_percent)])
 
# price per 1 unit of assessed value
print("Real Estate sale divided by assessed: ", np.round(sale / assessed, 2))
 
 
# 11. 2 DIMENSIONAL ARRAY
D2AssessedSale = np.array([assessed,
                           sale])
 
print("Real Estate Assessed Plus Sale - 2 dimentional array - ", D2AssessedSale)
 
# check the dimension of the array
print("Real Estate 2D array - dimension: ", D2AssessedSale.ndim)
 
# return total number of elements
print("Real Estate 2D array - total number of elements: ", D2AssessedSale.size)
 
# return a tuple that gives size of array in each dimension
print("Real Estate 2D array - shape: ", D2AssessedSale.shape)
 
# check the data type of the array
print("Real Estate 2D array - data type: ", D2AssessedSale.dtype)
 
# statistics on the 2D array: axis=1 works along each row, axis=0 along each column
print("Real Estate 2D array - mean of each row (assessed, sale): ", np.mean(D2AssessedSale, axis=1))
print("Real Estate 2D array - max of each row (assessed, sale): ", np.max(D2AssessedSale, axis=1))
print("Real Estate 2D array - min of each row (assessed, sale): ", np.min(D2AssessedSale, axis=1))
print("Real Estate 2D array - sum of each column (assessed + sale): ", np.sum(D2AssessedSale, axis=0))
 
 
# 12. SLICING AND INDEXING
# Slicing array
D2Slice = D2AssessedSale[0:1:1, 1:5:1]
print("Real Estate 2D array - slice D2AssessedSale[0:1:1, 1:5:1] : ", D2Slice)
D2Slice2 = D2AssessedSale[:1, 4:15:4]
print("Real Estate 2D array - slice D2AssessedSale[:1, 4:15:4] : ", D2Slice2)
 
# first 5 and last 5 values
print("Real Estate first 5 sale amounts: ", sale[:5])
print("Real Estate last 5 sale amounts: ", sale[-5:])
print("Real Estate every 10th sale amount: ", sale[::10])
print("Real Estate first 5 towns: ", town[:5])
 
# Indexing array
print("Real Estate 2D array - index D2Slice[0, 1] : ", D2Slice[0, 1])
print("Real Estate 2D array - index D2Slice2[0, 2] : ", D2Slice2[0, 2])
print("Real Estate 2D array - index D2AssessedSale[1, 0] (sale amount of first row): ", D2AssessedSale[1, 0])
 
 
# 13. LOOPING THROUGH AN ARRAY
# nditer - when we do not need the index values (first 5 values only)
count = 0
for elem in np.nditer(D2AssessedSale):
    print(elem)
    count = count + 1
    if count == 5:
        break
 
# ndenumerate - when we need the index values (first 5 values only)
count = 0
for index, elem in np.ndenumerate(D2AssessedSale):
    print(index, elem)
    count = count + 1
    if count == 5:
        break
 
 
# 14. RESHAPE, FLATTEN, TRANSPOSE
total = D2AssessedSale.size
D2Reshape = np.reshape(D2AssessedSale, (1, total))
print("Real Estate 2D array - np.reshape(D2AssessedSale, (1, total)) : ", D2Reshape)
print("Real Estate 2D array - reshape : Size ", D2Reshape.size)
print("Real Estate 2D array - reshape : ndim ", D2Reshape.ndim)
print("Real Estate 2D array - reshape : shape ", D2Reshape.shape)
 
# flatten makes the array 1 dimensional
print("Real Estate 2D array - flatten : ", D2AssessedSale.flatten())
 
# transpose swaps rows and columns: (2, N) becomes (N, 2)
transposed = D2AssessedSale.T
print("Real Estate 2D array - transpose : ", transposed)
print("Real Estate 2D array - transpose : shape ", transposed.shape)
 
 
# 15. JOINING AND SPLITTING ARRAYS
# stack assessed and sale as columns
stacked = np.column_stack((assessed, sale))
print("Real Estate column_stack (assessed, sale): ", stacked)
print("Real Estate column_stack shape: ", stacked.shape)
 
# join two arrays one after another
joined = np.concatenate((assessed[:5], sale[:5]))
print("Real Estate concatenate first 5 assessed + first 5 sale: ", joined)
 
# split an array into 5 equal parts (first 10 values only)
parts = np.split(sale[:10], 5)
print("Real Estate split first 10 sale amounts into 5 parts: ", parts)
 
 
# 16. HISTOGRAM AND LINSPACE
# count how many sales fall in each price bin
counts, edges = np.histogram(sale, bins=5)
print("Real Estate Sale histogram - counts: ", counts)
print("Real Estate Sale histogram - bin edges: ", edges)
 
# sales under 1 million only
under_million = sale[sale < 1000000]
counts, edges = np.histogram(under_million, bins=5)
print("Real Estate Sale (under 1 million) histogram - counts: ", counts)
print("Real Estate Sale (under 1 million) histogram - bin edges: ", edges)
 
# 5 evenly spaced numbers from min to max sale
print("Real Estate linspace from min to max sale: ", np.linspace(np.min(sale), np.max(sale), 5))
 
# normalize sale to the range 0 to 1
sale_norm = (sale - np.min(sale)) / (np.max(sale) - np.min(sale))
print("Real Estate Sale normalized (0 to 1): ", sale_norm)
 
# standardize sale (z-score): mean 0 and std 1
sale_z = (sale - np.mean(sale)) / np.std(sale)
print("Real Estate Sale z-score: ", sale_z)
print("Real Estate Sale z-score mean (close to 0): ", np.round(np.mean(sale_z), 6))
print("Real Estate Sale z-score std (close to 1): ", np.round(np.std(sale_z), 6))
 
 
# 17. OUTLIERS
# values more than 3 standard deviations from the mean
outliers = np.abs(sale_z) > 3
print("Real Estate sale outliers (count): ", np.sum(outliers))
print("Real Estate sale outliers (values): ", sale[outliers])
print("Real Estate sale outliers (towns): ", town[outliers])
 
# outliers with the IQR rule
q1 = np.percentile(sale, 25)
q3 = np.percentile(sale, 75)
iqr = q3 - q1
iqr_outliers = (sale < q1 - 1.5 * iqr) | (sale > q3 + 1.5 * iqr)
print("Real Estate IQR outliers (count): ", np.sum(iqr_outliers))
print("Real Estate IQR outliers (values): ", sale[iqr_outliers])
 
# check for missing values
print("Real Estate missing sale values: ", np.sum(np.isnan(sale)))
print("Real Estate missing assessed values: ", np.sum(np.isnan(assessed)))
print("Real Estate missing ratio values: ", np.sum(np.isnan(ratio)))
 
 
print()
