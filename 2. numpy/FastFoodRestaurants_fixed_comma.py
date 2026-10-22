
import numpy as np
# 1. LOAD THE DATA

lat, long, name, province = np.genfromtxt('numpy/FastFoodRestaurants_fixed_comma.csv', delimiter=',', usecols=(4,5,6,8), unpack=True, skip_header=1, invalid_raise=False, dtype=None, encoding='utf-8')
 
print("Fast Food Latitude: ", lat)
print("Fast Food Longitude: ", long)
print("Fast Food Name: ", name)
print("Fast Food Province: ", province)
 
print("Fast Food Latitude data type: ", lat.dtype)
print("Fast Food Name data type: ", name.dtype)
print("Fast Food total restaurants: ", lat.size)
 
 
# 2. STATISTICS OPERATIONS (latitude)
print("Fast Food Latitude mean: " , np.mean(lat))
print("Fast Food Latitude average: " , np.average(lat))
print("Fast Food Latitude median: " , np.median(lat))
print("Fast Food Latitude std: " , np.std(lat))
print("Fast Food Latitude variance: " , np.var(lat))
print("Fast Food Latitude min : " , np.min(lat))
print("Fast Food Latitude max : " , np.max(lat))
print("Fast Food Latitude range (max - min): " , np.ptp(lat))
print("Fast Food Latitude sum: " , np.sum(lat))
print("Fast Food Latitude percentile - 3: " , np.percentile(lat,3))
print("Fast Food Latitude percentile - 25: " , np.percentile(lat,25))
print("Fast Food Latitude percentile - 50: " , np.percentile(lat,50))
print("Fast Food Latitude percentile - 75: " , np.percentile(lat,75))
print("Fast Food Latitude percentile - 97: " , np.percentile(lat,97))
 
# index of the smallest and biggest value
print("Fast Food Latitude argmin (index of min): " , np.argmin(lat))
print("Fast Food Latitude argmax (index of max): " , np.argmax(lat))
print("Fast Food Restaurant with the smallest latitude: " , name[np.argmin(lat)], province[np.argmin(lat)])
print("Fast Food Restaurant with the biggest latitude: " , name[np.argmax(lat)], province[np.argmax(lat)])
 
 
# 3. STATISTICS OPERATIONS (longitude)
print("Fast Food Longitude mean: " , np.mean(long))
print("Fast Food Longitude median: " , np.median(long))
print("Fast Food Longitude std: " , np.std(long))
print("Fast Food Longitude min : " , np.min(long))
print("Fast Food Longitude max : " , np.max(long))
print("Fast Food Longitude percentile - 25: " , np.percentile(long,25))
print("Fast Food Longitude percentile - 75: " , np.percentile(long,75))
 
# correlation between latitude and longitude
print("Fast Food Lat - Long correlation matrix: " , np.corrcoef(lat, long))
print("Fast Food Lat - Long covariance matrix: " , np.cov(lat, long))
 
 
# 4. MATHS OPERATIONS
print("Fast Food Latitude square: " , np.square(lat))
print("Fast Food Latitude sqrt of abs: " , np.sqrt(np.abs(lat)))
print("Fast Food Longitude abs: " , np.abs(long))
print("Fast Food Latitude round (1 decimal): " , np.round(lat, 1))
print("Fast Food Latitude floor: " , np.floor(lat))
print("Fast Food Latitude ceil: " , np.ceil(lat))
 
 
# 5. BASIC ARITHMETIC (long and lat)
addition = long + lat
subtraction = long - lat
multiplication = long * lat
division = long / lat
 
print("Fast Food Long - lat - Addition:", addition)
print("Fast Food Long - lat - Subtraction:", subtraction)
print("Fast Food Long - lat - Multiplication:", multiplication)
print("Fast Food Long - lat - Division:", division)
 
# arithmetic with a single number (broadcasting)
print("Fast Food Latitude + 10: ", lat + 10)
print("Fast Food Latitude * 2: ", lat * 2)
 
 
# 6. TRIGONOMETRIC, EXPONENTIAL AND LOGARITHM FUNCTIONS
# abs() and +1 keep every value 1 or bigger, so log and arccosh work without nan
latPie = (np.abs(lat) / np.pi) + 1
 
sine_values = np.sin(latPie)
cosine_values = np.cos(latPie)
tangent_values = np.tan(latPie)
 
print("Fast Food Latitude - div - pie  - Sine values:", sine_values)
print("Fast Food Latitude - div - pie  - Cosine values:", cosine_values)
print("Fast Food Latitude - div - pie  - Tangent values:", tangent_values)
 
print("Fast Food Latitude - div - pie  - Exponential values:", np.exp(latPie))
 
log_array = np.log(latPie)
log10_array = np.log10(latPie)
print("Fast Food Latitude - div - pie  - Natural logarithm values:", log_array)
print("Fast Food Latitude - div - pie  - Base-10 logarithm values:", log10_array)
 
# degrees and radians
print("Fast Food Latitude in radians: ", np.radians(lat))
print("Fast Food Latitude radians back to degrees: ", np.degrees(np.radians(lat)))
 
# hyperbolic functions
print("Fast Food Latitude - div - pie  - Hyperbolic Sine values:", np.sinh(latPie))
print("Fast Food Latitude - div - pie  - Hyperbolic Cosine values:", np.cosh(latPie))
print("Fast Food Latitude - div - pie  - Hyperbolic Tangent values:", np.tanh(latPie))
print("Fast Food Latitude - div - pie  - Inverse Hyperbolic Sine values:", np.arcsinh(latPie))
print("Fast Food Latitude - div - pie  - Inverse Hyperbolic Cosine values:", np.arccosh(latPie))
 
 
# 7. SORTING, CUMULATIVE AND DIFFERENCE
print("Fast Food Latitude sorted (small to big): ", np.sort(lat))
print("Fast Food Latitude sorted (big to small): ", np.sort(lat)[::-1])
 
# argsort gives the index order, we can use it to sort the names too
order = np.argsort(lat)
print("Fast Food Names sorted by latitude: ", name[order])
 
print("Fast Food Latitude cumulative sum: ", np.cumsum(lat))
print("Fast Food Latitude difference between neighbours: ", np.diff(lat))
 
 
# 8. BOOLEAN FILTERING AND np.where
north = lat > np.median(lat)
print("Fast Food restaurants north of the median latitude (True/False): ", north)
print("Fast Food restaurants north of the median latitude (count): ", np.sum(north))
 
west = long < -100
print("Fast Food restaurants west of longitude -100 (count): ", np.sum(west))
print("Fast Food restaurants west of longitude -100 (names): ", name[west])
 
# two conditions together: & means AND, | means OR
north_west = (lat > 40) & (long < -100)
print("Fast Food restaurants with lat > 40 AND long < -100 (count): ", np.sum(north_west))
 
# np.where gives the index positions that match
print("Fast Food index positions where lat is above 60: ", np.where(lat > 60))
 
# np.where with three arguments: pick one value or another
region = np.where(lat > 38, "North", "South")
print("Fast Food region (North or South): ", region)
 
# keep only the coordinates that are inside the USA (rough box)
usa = (lat > 24) & (lat < 50) & (long > -125) & (long < -66)
print("Fast Food restaurants inside the USA box (count): ", np.sum(usa))
print("Fast Food restaurants outside the USA box (count): ", np.sum(~usa))
lat_usa = lat[usa]
long_usa = long[usa]
print("Fast Food USA latitude mean: ", np.mean(lat_usa))
print("Fast Food USA longitude mean: ", np.mean(long_usa))
 
 
# 9. COUNTING TEXT DATA (province and name)
unique_prov, prov_counts = np.unique(province, return_counts=True)
print("Fast Food unique provinces: ", unique_prov)
print("Fast Food number of unique provinces: ", unique_prov.size)
print("Fast Food counts per province: ", prov_counts)
 
# top 5 provinces
top = np.argsort(prov_counts)[::-1][:5]
for p, c in zip(unique_prov[top], prov_counts[top]):
    print("Fast Food top province - ", p, ":", c)
 
unique_names, name_counts = np.unique(name, return_counts=True)
print("Fast Food number of unique restaurant names: ", unique_names.size)
 
# top 5 restaurant names
top = np.argsort(name_counts)[::-1][:5]
for n, c in zip(unique_names[top], name_counts[top]):
    print("Fast Food top restaurant - ", n, ":", c)
 
# mean latitude for one restaurant name
mcd = (name == "McDonald's")
print("Fast Food McDonald's count: ", np.sum(mcd))
print("Fast Food McDonald's mean latitude: ", np.mean(lat[mcd]))
print("Fast Food McDonald's mean longitude: ", np.mean(long[mcd]))
 
# mean latitude for each of the top 5 provinces
for p in unique_prov[np.argsort(prov_counts)[::-1][:5]]:
    print("Fast Food province", p, "mean latitude: ", np.mean(lat[province == p]))
 
 
# 10. DISTANCE FROM THE CENTER
# simple distance in degrees (not kilometers) from the middle of the USA data
center_lat = np.mean(lat_usa)
center_long = np.mean(long_usa)
distance = np.sqrt((lat_usa - center_lat) ** 2 + (long_usa - center_long) ** 2)
 
print("Fast Food distance from center - mean: ", np.mean(distance))
print("Fast Food distance from center - min: ", np.min(distance))
print("Fast Food distance from center - max: ", np.max(distance))
 
 
# 11. 2 DIMENSIONAL ARRAY
D2LongLat = np.array([long,
                      lat])
 
print("Fast Food Long Plus Lat - 2 dimentional array - ", D2LongLat)
 
# check the dimension of the array
print("Fast Food 2D array - dimension: ", D2LongLat.ndim)
 
# return total number of elements
print("Fast Food 2D array - total number of elements: ", D2LongLat.size)
 
# return a tuple that gives size of array in each dimension
print("Fast Food 2D array - shape: ", D2LongLat.shape)
 
# check the data type of the array
print("Fast Food 2D array - data type: ", D2LongLat.dtype)
 
# statistics on the 2D array: axis=1 works along each row, axis=0 along each column
print("Fast Food 2D array - mean of each row (long, lat): ", np.mean(D2LongLat, axis=1))
print("Fast Food 2D array - max of each row (long, lat): ", np.max(D2LongLat, axis=1))
print("Fast Food 2D array - min of each row (long, lat): ", np.min(D2LongLat, axis=1))
print("Fast Food 2D array - sum of each column (long + lat): ", np.sum(D2LongLat, axis=0))
 
 
# 12. SLICING AND INDEXING
# Slicing array
D2Slice = D2LongLat[0:1:1, 1:5:1]
print("Fast Food 2D array - slice D2LongLat[0:1:1, 1:5:1] : ", D2Slice)
D2Slice2 = D2LongLat[:1, 4:15:4]
print("Fast Food 2D array - slice D2LongLat[:1, 4:15:4] : ", D2Slice2)
 
# first 5 and last 5 values
print("Fast Food first 5 latitudes: ", lat[:5])
print("Fast Food last 5 latitudes: ", lat[-5:])
print("Fast Food every 1000th latitude: ", lat[::1000])
 
# Indexing array
print("Fast Food 2D array - index D2Slice[0, 1] : ", D2Slice[0, 1])
print("Fast Food 2D array - index D2Slice2[0, 2] : ", D2Slice2[0, 2])
print("Fast Food 2D array - index D2LongLat[1, 0] (latitude of first restaurant): ", D2LongLat[1, 0])
 
 
# 13. LOOPING THROUGH AN ARRAY
# nditer - when we do not need the index values (first 5 values only)
count = 0
for elem in np.nditer(D2LongLat):
    print(elem)
    count = count + 1
    if count == 5:
        break
 
# ndenumerate - when we need the index values (first 5 values only)
count = 0
for index, elem in np.ndenumerate(D2LongLat):
    print(index, elem)
    count = count + 1
    if count == 5:
        break
 
 
# 14. RESHAPE, FLATTEN, TRANSPOSE
total = D2LongLat.size
D2Reshape = np.reshape(D2LongLat, (1, total))
print("Fast Food 2D array - np.reshape(D2LongLat, (1, total)) : ", D2Reshape)
print("Fast Food 2D array - reshape : Size ", D2Reshape.size)
print("Fast Food 2D array - reshape : ndim ", D2Reshape.ndim)
print("Fast Food 2D array - reshape : shape ", D2Reshape.shape)
 
# flatten makes the array 1 dimensional
print("Fast Food 2D array - flatten : ", D2LongLat.flatten())
 
# transpose swaps rows and columns: (2, N) becomes (N, 2)
transposed = D2LongLat.T
print("Fast Food 2D array - transpose : ", transposed)
print("Fast Food 2D array - transpose : shape ", transposed.shape)
 
 
# 15. JOINING AND SPLITTING ARRAYS
# stack lat and long as columns
stacked = np.column_stack((lat, long))
print("Fast Food column_stack (lat, long): ", stacked)
print("Fast Food column_stack shape: ", stacked.shape)
 
# join two arrays one after another
joined = np.concatenate((lat[:5], long[:5]))
print("Fast Food concatenate first 5 lat + first 5 long: ", joined)
 
# split an array into 5 equal parts (first 10 values only)
parts = np.split(lat[:10], 5)
print("Fast Food split first 10 latitudes into 5 parts: ", parts)
 
 
# 16. HISTOGRAM AND LINSPACE
# count how many restaurants fall in each latitude bin
counts, edges = np.histogram(lat_usa, bins=5)
print("Fast Food USA latitude histogram - counts: ", counts)
print("Fast Food USA latitude histogram - bin edges: ", edges)
 
# 5 evenly spaced numbers from min to max latitude
print("Fast Food linspace from min to max latitude: ", np.linspace(np.min(lat), np.max(lat), 5))
 
# normalize latitude to the range 0 to 1
lat_norm = (lat - np.min(lat)) / (np.max(lat) - np.min(lat))
print("Fast Food Latitude normalized (0 to 1): ", lat_norm)
 
# standardize latitude (z-score): mean 0 and std 1
lat_z = (lat - np.mean(lat)) / np.std(lat)
print("Fast Food Latitude z-score: ", lat_z)
print("Fast Food Latitude z-score mean (close to 0): ", np.round(np.mean(lat_z), 6))
print("Fast Food Latitude z-score std (close to 1): ", np.round(np.std(lat_z), 6))
 
 
# 17. OUTLIERS
# values more than 3 standard deviations from the mean
outliers = np.abs(lat_z) > 3
print("Fast Food latitude outliers (count): ", np.sum(outliers))
print("Fast Food latitude outliers (values): ", lat[outliers])
print("Fast Food latitude outliers (names): ", name[outliers])
 
# check for missing values
print("Fast Food missing latitude values: ", np.sum(np.isnan(lat)))
print("Fast Food missing longitude values: ", np.sum(np.isnan(long)))
 
 
print()