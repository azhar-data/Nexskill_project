
import numpy as np
 
# 1. LOAD THE DATA

name, industry, rounds, invest, valuation, investors, country, yearf, growth = np.genfromtxt('numpy/startup_growth_investment_data.csv', delimiter=',', usecols=(0,1,2,3,4,5,6,7,8), unpack=True, skip_header=1, dtype=None, encoding='utf-8')
 
print("Startup Name: ", name)
print("Startup Industry: ", industry)
print("Startup Funding Rounds: ", rounds)
print("Startup Investment Amount: ", invest)
print("Startup Valuation: ", valuation)
print("Startup Number of Investors: ", investors)
print("Startup Country: ", country)
print("Startup Year Founded: ", yearf)
print("Startup Growth Rate: ", growth)
 
print("Startup Investment data type: ", invest.dtype)
print("Startup Funding Rounds data type: ", rounds.dtype)
print("Startup Industry data type: ", industry.dtype)
print("Startup total startups: ", invest.size)
 
 
# 2. STATISTICS OPERATIONS (investment amount)
print("Startup Investment mean: " , np.mean(invest))
print("Startup Investment average: " , np.average(invest))
print("Startup Investment median: " , np.median(invest))
print("Startup Investment std: " , np.std(invest))
print("Startup Investment variance: " , np.var(invest))
print("Startup Investment min : " , np.min(invest))
print("Startup Investment max : " , np.max(invest))
print("Startup Investment range (max - min): " , np.ptp(invest))
print("Startup Investment sum: " , np.sum(invest))
print("Startup Investment percentile - 3: " , np.percentile(invest,3))
print("Startup Investment percentile - 25: " , np.percentile(invest,25))
print("Startup Investment percentile - 50: " , np.percentile(invest,50))
print("Startup Investment percentile - 75: " , np.percentile(invest,75))
print("Startup Investment percentile - 97: " , np.percentile(invest,97))
 
# index of the smallest and biggest value
print("Startup Investment argmin (index of min): " , np.argmin(invest))
print("Startup Investment argmax (index of max): " , np.argmax(invest))
print("Startup with the smallest investment: " , name[np.argmin(invest)], industry[np.argmin(invest)], country[np.argmin(invest)])
print("Startup with the biggest investment: " , name[np.argmax(invest)], industry[np.argmax(invest)], country[np.argmax(invest)])
 
 
# 3. STATISTICS OPERATIONS (valuation, growth, rounds, investors)
print("Startup Valuation mean: " , np.mean(valuation))
print("Startup Valuation median: " , np.median(valuation))
print("Startup Valuation std: " , np.std(valuation))
print("Startup Valuation min : " , np.min(valuation))
print("Startup Valuation max : " , np.max(valuation))
 
print("Startup Growth Rate mean: " , np.mean(growth))
print("Startup Growth Rate median: " , np.median(growth))
print("Startup Growth Rate std: " , np.std(growth))
print("Startup Growth Rate min : " , np.min(growth))
print("Startup Growth Rate max : " , np.max(growth))
print("Startup Growth Rate percentile - 25: " , np.percentile(growth,25))
print("Startup Growth Rate percentile - 75: " , np.percentile(growth,75))
 
print("Startup Funding Rounds mean: " , np.mean(rounds))
print("Startup Funding Rounds min : " , np.min(rounds))
print("Startup Funding Rounds max : " , np.max(rounds))
 
print("Startup Number of Investors mean: " , np.mean(investors))
print("Startup Number of Investors min : " , np.min(investors))
print("Startup Number of Investors max : " , np.max(investors))
 
# correlation between investment and valuation
print("Startup Investment - Valuation correlation matrix: " , np.corrcoef(invest, valuation))
print("Startup Investment - Valuation covariance matrix: " , np.cov(invest, valuation))
 
# correlation matrix of 5 numeric columns (each row is one variable)
numeric = np.array([rounds, invest, valuation, investors, growth])
print("Startup correlation matrix (rounds, invest, valuation, investors, growth): ")
print(np.round(np.corrcoef(numeric), 3))
 
 
# 4. MATHS OPERATIONS
print("Startup Growth Rate square: " , np.square(growth))
print("Startup Growth Rate sqrt: " , np.sqrt(growth))
print("Startup Growth Rate abs: " , np.abs(growth))
print("Startup Growth Rate round (0 decimals): " , np.round(growth))
print("Startup Growth Rate floor: " , np.floor(growth))
print("Startup Growth Rate ceil: " , np.ceil(growth))
print("Startup Investment sqrt: " , np.sqrt(invest))
print("Startup Investment in millions: " , invest / 1000000)
print("Startup Investment in billions: " , invest / 1000000000)
 
 
# 5. BASIC ARITHMETIC (valuation and investment)
addition = valuation + invest
subtraction = valuation - invest
multiplication = valuation * invest
division = valuation / invest
 
print("Startup Valuation - investment - Addition:", addition)
print("Startup Valuation - investment - Subtraction (value created):", subtraction)
print("Startup Valuation - investment - Multiplication:", multiplication)
print("Startup Valuation / investment - Division (valuation multiple):", division)
 
# arithmetic with a single number (broadcasting)
print("Startup Growth Rate + 10: ", growth + 10)
print("Startup Growth Rate * 2: ", growth * 2)
print("Startup Growth Rate as a fraction (divide by 100): ", growth / 100)
 
# investment per investor and per funding round
invest_per_investor = invest / investors
invest_per_round = invest / rounds
print("Startup Investment per investor: ", invest_per_investor)
print("Startup Investment per funding round: ", invest_per_round)
 
# startup age (the data is from 2023)
age = 2023 - yearf
print("Startup age in years: ", age)
print("Startup mean age: ", np.mean(age))
 
 
# 6. TRIGONOMETRIC, EXPONENTIAL AND LOGARITHM FUNCTIONS
# investment amounts are very big, so we scale them first (billions) and add 1
# every value is 1 or bigger, so log and arccosh work without nan
investPie = (invest / 1000000000) + 1
 
sine_values = np.sin(investPie)
cosine_values = np.cos(investPie)
tangent_values = np.tan(investPie)
 
print("Startup Investment - scaled - Sine values:", sine_values)
print("Startup Investment - scaled - Cosine values:", cosine_values)
print("Startup Investment - scaled - Tangent values:", tangent_values)
 
print("Startup Investment - scaled - Exponential values:", np.exp(investPie))
 
log_array = np.log(investPie)
log10_array = np.log10(investPie)
print("Startup Investment - scaled - Natural logarithm values:", log_array)
print("Startup Investment - scaled - Base-10 logarithm values:", log10_array)
 
# log of the real investment and valuation (very common for money values)
print("Startup Investment natural log: ", np.log(invest))
print("Startup Valuation log10: ", np.log10(valuation))
 
# degrees and radians (growth rate used like an angle just for practice)
print("Startup Growth Rate in radians: ", np.radians(growth))
print("Startup Growth Rate radians back to degrees: ", np.degrees(np.radians(growth)))
 
# hyperbolic functions
print("Startup Investment - scaled - Hyperbolic Sine values:", np.sinh(investPie))
print("Startup Investment - scaled - Hyperbolic Cosine values:", np.cosh(investPie))
print("Startup Investment - scaled - Hyperbolic Tangent values:", np.tanh(investPie))
print("Startup Investment - scaled - Inverse Hyperbolic Sine values:", np.arcsinh(investPie))
print("Startup Investment - scaled - Inverse Hyperbolic Cosine values:", np.arccosh(investPie))
 
 
# 7. SORTING, CUMULATIVE AND DIFFERENCE
print("Startup Investment sorted (small to big): ", np.sort(invest))
print("Startup Investment sorted (big to small): ", np.sort(invest)[::-1])
 
# argsort gives the index order, we can use it to sort the names too
order = np.argsort(valuation)
print("Startup Names sorted by valuation: ", name[order])
print("Startup Top 5 highest valuation names: ", name[order][::-1][:5])
print("Startup Top 5 highest valuations: ", valuation[order][::-1][:5])
print("Startup Top 5 lowest valuations: ", valuation[order][:5])
 
# top 5 by growth rate
order_growth = np.argsort(growth)
print("Startup Top 5 growth rate names: ", name[order_growth][::-1][:5])
print("Startup Top 5 growth rates: ", growth[order_growth][::-1][:5])
 
print("Startup first 10 Investment cumulative sum: ", np.cumsum(invest[:10]))
print("Startup first 10 Investment difference between neighbours: ", np.diff(invest[:10]))
 
 
# 8. BOOLEAN FILTERING AND np.where
high_growth = growth > np.median(growth)
print("Startup growth above the median (True/False): ", high_growth)
print("Startup growth above the median (count): ", np.sum(high_growth))
 
fast = growth >= 150
print("Startup growth rate of 150 or more (count): ", np.sum(fast))
print("Startup growth rate of 150 or more (names): ", name[fast])
 
# two conditions together: & means AND, | means OR
fintech_usa = (industry == "Fintech") & (country == "USA")
print("Startup Fintech companies in the USA (count): ", np.sum(fintech_usa))
 
big_and_fast = (invest > np.percentile(invest, 75)) & (growth > 100)
print("Startup top 25 percent investment AND growth above 100 (count): ", np.sum(big_and_fast))
 
young = yearf >= 2015
print("Startup founded in 2015 or later (count): ", np.sum(young))
 
# np.where gives the index positions that match
print("Startup index positions where growth is above 199: ", np.where(growth > 199))
 
# np.where with three arguments: pick one value or another
growth_level = np.where(growth > np.median(growth), "High", "Low")
print("Startup growth level (High or Low): ", growth_level)
 
# unicorn = valuation of 1 billion or more
unicorn = valuation >= 1000000000
print("Startup valuation of 1 billion or more (count): ", np.sum(unicorn))
print("Startup percent with valuation of 1 billion or more: ", np.mean(unicorn) * 100)
 
# valuation bigger than investment means value was created
print("Startup valuation bigger than investment (count): ", np.sum(valuation > invest))
print("Startup valuation smaller than investment (count): ", np.sum(valuation < invest))
 
 
# 9. COUNTING TEXT DATA (industry and country)
unique_ind, ind_counts = np.unique(industry, return_counts=True)
print("Startup unique industries: ", unique_ind)
print("Startup counts per industry: ", ind_counts)
 
unique_cty, cty_counts = np.unique(country, return_counts=True)
print("Startup unique countries: ", unique_cty)
print("Startup counts per country: ", cty_counts)
 
# industry with the most startups
print("Startup industry with the most startups: ", unique_ind[np.argmax(ind_counts)], np.max(ind_counts))
print("Startup country with the most startups: ", unique_cty[np.argmax(cty_counts)], np.max(cty_counts))
 
# stats for each industry
for i in unique_ind:
    mask = (industry == i)
    print("Startup industry", i, "- count: ", np.sum(mask))
    print("Startup industry", i, "- mean investment: ", np.mean(invest[mask]))
    print("Startup industry", i, "- mean valuation: ", np.mean(valuation[mask]))
    print("Startup industry", i, "- mean growth rate: ", np.mean(growth[mask]))
    print("Startup industry", i, "- median growth rate: ", np.median(growth[mask]))
    print("Startup industry", i, "- mean funding rounds: ", np.mean(rounds[mask]))
 
# stats for each country
for c in unique_cty:
    mask = (country == c)
    print("Startup country", c, "- count: ", np.sum(mask))
    print("Startup country", c, "- mean investment: ", np.mean(invest[mask]))
    print("Startup country", c, "- mean valuation: ", np.mean(valuation[mask]))
    print("Startup country", c, "- mean growth rate: ", np.mean(growth[mask]))
 
# best industry and country by mean growth rate
ind_growth = np.array([np.mean(growth[industry == i]) for i in unique_ind])
cty_growth = np.array([np.mean(growth[country == c]) for c in unique_cty])
print("Startup industry with the highest mean growth: ", unique_ind[np.argmax(ind_growth)], np.max(ind_growth))
print("Startup industry with the lowest mean growth: ", unique_ind[np.argmin(ind_growth)], np.min(ind_growth))
print("Startup country with the highest mean growth: ", unique_cty[np.argmax(cty_growth)], np.max(cty_growth))
print("Startup country with the lowest mean growth: ", unique_cty[np.argmin(cty_growth)], np.min(cty_growth))
 
# best industry by mean valuation
ind_val = np.array([np.mean(valuation[industry == i]) for i in unique_ind])
print("Startup industry with the highest mean valuation: ", unique_ind[np.argmax(ind_val)], np.max(ind_val))
 
# AI startups only
ai = (industry == "AI")
print("Startup AI startups (count): ", np.sum(ai))
print("Startup AI mean investment: ", np.mean(invest[ai]))
print("Startup AI mean growth: ", np.mean(growth[ai]))
 
 
# 10. YEAR FOUNDED CHECKS
unique_year, year_counts = np.unique(yearf, return_counts=True)
print("Startup unique years founded: ", unique_year)
print("Startup counts per year founded: ", year_counts)
print("Startup oldest founded year: ", np.min(yearf))
print("Startup newest founded year: ", np.max(yearf))
print("Startup year with the most startups founded: ", unique_year[np.argmax(year_counts)], np.max(year_counts))
 
# mean growth for each year founded
year_growth = np.array([np.mean(growth[yearf == y]) for y in unique_year])
print("Startup mean growth for each year founded: ", np.round(year_growth, 2))
 
# compare startups founded before 2010 with those founded in 2010 or later
old = yearf < 2010
print("Startup founded before 2010 (count): ", np.sum(old))
print("Startup founded before 2010 mean growth: ", np.mean(growth[old]))
print("Startup founded in 2010 or later mean growth: ", np.mean(growth[~old]))
 
 
# 11. 2 DIMENSIONAL ARRAY
D2InvestVal = np.array([invest,
                        valuation])
 
print("Startup Investment Plus Valuation - 2 dimentional array - ", D2InvestVal)
 
# check the dimension of the array
print("Startup 2D array - dimension: ", D2InvestVal.ndim)
 
# return total number of elements
print("Startup 2D array - total number of elements: ", D2InvestVal.size)
 
# return a tuple that gives size of array in each dimension
print("Startup 2D array - shape: ", D2InvestVal.shape)
 
# check the data type of the array
print("Startup 2D array - data type: ", D2InvestVal.dtype)
 
# statistics on the 2D array: axis=1 works along each row, axis=0 along each column
print("Startup 2D array - mean of each row (invest, valuation): ", np.mean(D2InvestVal, axis=1))
print("Startup 2D array - max of each row (invest, valuation): ", np.max(D2InvestVal, axis=1))
print("Startup 2D array - min of each row (invest, valuation): ", np.min(D2InvestVal, axis=1))
print("Startup 2D array - sum of each column (invest + valuation): ", np.sum(D2InvestVal, axis=0))
 
 
# 12. SLICING AND INDEXING
# Slicing array
D2Slice = D2InvestVal[0:1:1, 1:5:1]
print("Startup 2D array - slice D2InvestVal[0:1:1, 1:5:1] : ", D2Slice)
D2Slice2 = D2InvestVal[:1, 4:15:4]
print("Startup 2D array - slice D2InvestVal[:1, 4:15:4] : ", D2Slice2)
 
# first 5 and last 5 values
print("Startup first 5 investments: ", invest[:5])
print("Startup last 5 investments: ", invest[-5:])
print("Startup every 500th investment: ", invest[::500])
print("Startup first 5 names: ", name[:5])
print("Startup last 5 names: ", name[-5:])
 
# Indexing array
print("Startup 2D array - index D2Slice[0, 1] : ", D2Slice[0, 1])
print("Startup 2D array - index D2Slice2[0, 2] : ", D2Slice2[0, 2])
print("Startup 2D array - index D2InvestVal[1, 0] (valuation of first startup): ", D2InvestVal[1, 0])
 
 
# 13. LOOPING THROUGH AN ARRAY
# nditer - when we do not need the index values (first 5 values only)
count = 0
for elem in np.nditer(D2InvestVal):
    print(elem)
    count = count + 1
    if count == 5:
        break
 
# ndenumerate - when we need the index values (first 5 values only)
count = 0
for index, elem in np.ndenumerate(D2InvestVal):
    print(index, elem)
    count = count + 1
    if count == 5:
        break
 
 
# 14. RESHAPE, FLATTEN, TRANSPOSE
total = D2InvestVal.size
D2Reshape = np.reshape(D2InvestVal, (1, total))
print("Startup 2D array - np.reshape(D2InvestVal, (1, total)) : ", D2Reshape)
print("Startup 2D array - reshape : Size ", D2Reshape.size)
print("Startup 2D array - reshape : ndim ", D2Reshape.ndim)
print("Startup 2D array - reshape : shape ", D2Reshape.shape)
 
# a 1D array of 5000 values can be reshaped to 50 rows x 100 columns
D2Grid = np.reshape(growth, (50, 100))
print("Startup growth reshaped to 50 x 100 - shape: ", D2Grid.shape)
print("Startup growth 50 x 100 - mean of each row (first 5): ", np.mean(D2Grid, axis=1)[:5])
 
# flatten makes the array 1 dimensional
print("Startup 2D array - flatten : ", D2InvestVal.flatten())
 
# transpose swaps rows and columns: (2, N) becomes (N, 2)
transposed = D2InvestVal.T
print("Startup 2D array - transpose : ", transposed)
print("Startup 2D array - transpose : shape ", transposed.shape)
 
 
# 15. JOINING AND SPLITTING ARRAYS
# stack investment and valuation as columns
stacked = np.column_stack((invest, valuation))
print("Startup column_stack (invest, valuation): ", stacked)
print("Startup column_stack shape: ", stacked.shape)
 
# join two arrays one after another
joined = np.concatenate((invest[:5], valuation[:5]))
print("Startup concatenate first 5 invest + first 5 valuation: ", joined)
 
# split an array into 5 equal parts (first 10 values only)
parts = np.split(growth[:10], 5)
print("Startup split first 10 growth rates into 5 parts: ", parts)
 
# split all 5000 startups into 5 equal groups and take the mean growth of each group
groups = np.split(growth, 5)
for g in groups:
    print("Startup group of", g.size, "- mean growth: ", np.mean(g))
 
 
# 16. HISTOGRAM AND LINSPACE
# count how many startups fall in each growth bin
counts, edges = np.histogram(growth, bins=5)
print("Startup Growth Rate histogram - counts: ", counts)
print("Startup Growth Rate histogram - bin edges: ", edges)
 
counts, edges = np.histogram(invest, bins=5)
print("Startup Investment histogram - counts: ", counts)
print("Startup Investment histogram - bin edges: ", edges)
 
counts, edges = np.histogram(rounds, bins=np.arange(1, 12))
print("Startup Funding Rounds histogram - counts: ", counts)
print("Startup Funding Rounds histogram - bin edges: ", edges)
 
# 5 evenly spaced numbers from min to max growth rate
print("Startup linspace from min to max growth: ", np.linspace(np.min(growth), np.max(growth), 5))
 
# normalize growth to the range 0 to 1
growth_norm = (growth - np.min(growth)) / (np.max(growth) - np.min(growth))
print("Startup Growth Rate normalized (0 to 1): ", growth_norm)
 
# standardize growth (z-score): mean 0 and std 1
growth_z = (growth - np.mean(growth)) / np.std(growth)
print("Startup Growth Rate z-score: ", growth_z)
print("Startup Growth Rate z-score mean (close to 0): ", np.round(np.mean(growth_z), 6))
print("Startup Growth Rate z-score std (close to 1): ", np.round(np.std(growth_z), 6))
 
 
# 17. OUTLIERS AND MISSING VALUES
# values more than 3 standard deviations from the mean
invest_z = (invest - np.mean(invest)) / np.std(invest)
outliers = np.abs(invest_z) > 3
print("Startup investment outliers - z-score (count): ", np.sum(outliers))
print("Startup investment outliers - z-score (names): ", name[outliers])
 
# outliers with the IQR rule
q1 = np.percentile(valuation, 25)
q3 = np.percentile(valuation, 75)
iqr = q3 - q1
iqr_outliers = (valuation < q1 - 1.5 * iqr) | (valuation > q3 + 1.5 * iqr)
print("Startup valuation IQR outliers (count): ", np.sum(iqr_outliers))
print("Startup valuation IQR outliers (values): ", valuation[iqr_outliers])
print("Startup valuation IQR outliers (names): ", name[iqr_outliers])
 
# check for missing values
print("Startup missing investment values: ", np.sum(np.isnan(invest)))
print("Startup missing valuation values: ", np.sum(np.isnan(valuation)))
print("Startup missing growth values: ", np.sum(np.isnan(growth)))
 
# check for duplicate startup names
unique_names = np.unique(name)
print("Startup unique names: ", unique_names.size)
print("Startup duplicate names: ", name.size - unique_names.size)
 
 
print()