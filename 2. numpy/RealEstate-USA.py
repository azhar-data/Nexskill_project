
import numpy as np

# ==========================================
# 1. LOAD THE DATA - NUMPY ONLY
# ==========================================

filename = "numpy/RealEstate-USA.csv"

data = np.genfromtxt(
    filename,
    delimiter=",",
    names=True,
    dtype=[
        ("brokered_by", "f8"),
        ("status", "U30"),
        ("price", "f8"),
        ("bed", "f8"),
        ("bath", "f8"),
        ("acre_lot", "f8"),
        ("street", "f8"),
        ("city", "U100"),
        ("state", "U30"),
        ("zip_code", "f8"),
        ("house_size", "f8"),
        ("prev_sold_date", "U30")
    ],
    encoding="utf-8",
    autostrip=True,
    missing_values="",
    filling_values={
        "brokered_by": np.nan,
        "status": "",
        "price": np.nan,
        "bed": np.nan,
        "bath": np.nan,
        "acre_lot": np.nan,
        "street": np.nan,
        "city": "",
        "state": "",
        "zip_code": np.nan,
        "house_size": np.nan,
        "prev_sold_date": ""
    }
)

# Extract columns as NumPy arrays
price = data["price"]
bed = data["bed"]
bath = data["bath"]
acre_lot = data["acre_lot"]
house_size = data["house_size"]
city = data["city"]
state = data["state"]
status = data["status"]
year = data["prev_sold_date"]

print("Prices:", price)
print("Bedrooms:", bed)
print("Bathrooms:", bath)
print("House sizes:", house_size)
print("Cities:", city)
print("States:", state)
print("Price dtype:", price.dtype)
print("Total properties:", price.size)
print("Dataset shape:", data.shape)


# ==========================================
# 2. PRICE STATISTICS
# ==========================================

print("\n--- PRICE STATISTICS ---")

print("Mean:", np.nanmean(price))
print("Average:", np.nanmean(price))
print("Median:", np.nanmedian(price))
print("Standard deviation:", np.nanstd(price))
print("Variance:", np.nanvar(price))
print("Minimum:", np.nanmin(price))
print("Maximum:", np.nanmax(price))
print("Range:", np.nanmax(price) - np.nanmin(price))
print("Total listed value:", np.nansum(price))

print("Percentile 3:", np.nanpercentile(price, 3))
print("Percentile 25:", np.nanpercentile(price, 25))
print("Percentile 50:", np.nanpercentile(price, 50))
print("Percentile 75:", np.nanpercentile(price, 75))
print("Percentile 97:", np.nanpercentile(price, 97))

print("Minimum price index:", np.nanargmin(price))
print("Maximum price index:", np.nanargmax(price))

smallest = np.nanargmin(price)
biggest = np.nanargmax(price)

print("Cheapest property:", city[smallest], state[smallest])
print("Cheapest price:", price[smallest])

print("Most expensive property:", city[biggest], state[biggest])
print("Most expensive price:", price[biggest])


# ==========================================
# 3. STATISTICS: BEDROOMS, BATHROOMS, SIZE
# ==========================================

print("\n--- BEDROOMS ---")
print("Mean:", np.nanmean(bed))
print("Median:", np.nanmedian(bed))
print("Std:", np.nanstd(bed))
print("Min:", np.nanmin(bed))
print("Max:", np.nanmax(bed))

print("\n--- BATHROOMS ---")
print("Mean:", np.nanmean(bath))
print("Median:", np.nanmedian(bath))
print("Std:", np.nanstd(bath))
print("Min:", np.nanmin(bath))
print("Max:", np.nanmax(bath))

print("\n--- HOUSE SIZE ---")
print("Mean:", np.nanmean(house_size))
print("Median:", np.nanmedian(house_size))
print("Std:", np.nanstd(house_size))
print("Min:", np.nanmin(house_size))
print("Max:", np.nanmax(house_size))
print("25th percentile:", np.nanpercentile(house_size, 25))
print("75th percentile:", np.nanpercentile(house_size, 75))

print("\n--- LOT SIZE ---")
print("Mean:", np.nanmean(acre_lot))
print("Median:", np.nanmedian(acre_lot))
print("Min:", np.nanmin(acre_lot))
print("Max:", np.nanmax(acre_lot))

# Correlation between price and house size
valid = np.isfinite(price) & np.isfinite(house_size)

print("Price-size correlation:",
      np.corrcoef(price[valid], house_size[valid]))

print("Price-size covariance:",
      np.cov(price[valid], house_size[valid]))

# Correlation matrix
numeric = np.column_stack((price, bed, bath, acre_lot, house_size))
valid = np.all(np.isfinite(numeric), axis=1)

print("Correlation matrix:")
print(np.round(np.corrcoef(numeric[valid], rowvar=False), 3))


# ==========================================
# 4. MATHEMATICAL OPERATIONS
# ==========================================

print("\n--- MATHEMATICAL OPERATIONS ---")

print("Price square:", np.square(price))
print("Price square root:", np.sqrt(price))
print("Absolute price:", np.abs(price))
print("Rounded house size:", np.round(house_size))
print("Floor house size:", np.floor(house_size))
print("Ceil house size:", np.ceil(house_size))

print("Price in thousands:", price / 1000)
print("Price in millions:", price / 1000000)
print("Square root of house size:", np.sqrt(house_size))


# ==========================================
# 5. BASIC ARITHMETIC
# ==========================================

print("\n--- ARITHMETIC ---")

print("Price + 10000:", price + 10000)
print("Price - 10000:", price - 10000)
print("Price * 2:", price * 2)
print("Price / 2:", price / 2)

price_per_sqft = np.divide(
    price,
    house_size,
    out=np.full(price.shape, np.nan),
    where=np.isfinite(house_size) & (house_size > 0)
)

print("Price per square foot:", price_per_sqft)
print("Mean price per square foot:", np.nanmean(price_per_sqft))

price_per_bedroom = np.divide(
    price,
    bed,
    out=np.full(price.shape, np.nan),
    where=np.isfinite(bed) & (bed > 0)
)

print("Price per bedroom:", price_per_bedroom)

print("House size + 100:", house_size + 100)
print("House size * 2:", house_size * 2)


# ==========================================
# 6. TRIGONOMETRIC, EXPONENTIAL, LOGARITHM
# ==========================================

print("\n--- ADVANCED MATH ---")

scaled_price = price / 1000000 + 1

print("Sine:", np.sin(scaled_price))
print("Cosine:", np.cos(scaled_price))
print("Tangent:", np.tan(scaled_price))
print("Exponential:", np.exp(scaled_price))

print("Natural logarithm:", np.log(price))
print("Base-10 logarithm:", np.log10(price))

print("Sinh:", np.sinh(scaled_price))
print("Cosh:", np.cosh(scaled_price))
print("Tanh:", np.tanh(scaled_price))
print("Arcsinh:", np.arcsinh(scaled_price))
print("Arccosh:", np.arccosh(scaled_price))

# Mathematical practice only; these functions do not
# directly explain real-estate market behaviour.


# ==========================================
# 7. SORTING, CUMULATIVE SUM, DIFFERENCE
# ==========================================

print("\n--- SORTING ---")

print("Prices ascending:", np.sort(price))
print("Prices descending:", np.sort(price)[::-1])

order = np.argsort(price)

print("Cities sorted by price:", city[order])
print("Top 5 expensive cities:", city[order][-5:][::-1])
print("Top 5 prices:", price[order][-5:][::-1])
print("Lowest 5 prices:", price[order][:5])

size_order = np.argsort(np.where(np.isfinite(house_size),
                                 house_size, -np.inf))

print("Largest house sizes:", house_size[size_order][-5:][::-1])

print("Cumulative sum of first 10 prices:",
      np.nancumsum(price[:10]))

print("Differences between first 10 prices:",
      np.diff(price[:10]))


# ==========================================
# 8. BOOLEAN FILTERING AND NP.WHERE
# ==========================================

print("\n--- FILTERING ---")

high_price = price > np.nanmedian(price)

print("Above median:", high_price)
print("Above median count:", np.sum(high_price))

expensive = price >= 500000
affordable = price < 100000

print("Properties >= $500,000:", np.sum(expensive))
print("Expensive property cities:", city[expensive])

print("Properties < $100,000:", np.sum(affordable))
print("Affordable property cities:", city[affordable])

many_bedrooms = bed >= 4
large_houses = house_size >= 2000

print("Properties with 4+ bedrooms:", np.sum(many_bedrooms))
print("Properties >= 2,000 sq ft:", np.sum(large_houses))

large_and_expensive = (house_size >= 2000) & (price >= 500000)

print("Large and expensive properties:",
      np.sum(large_and_expensive))

print("Indexes above $500,000:", np.where(price > 500000))

price_level = np.where(
    price >= np.nanmedian(price), "High", "Low"
)

print("Price levels:", price_level)

millionaire_properties = price >= 1000000

print("Properties >= $1 million:",
      np.sum(millionaire_properties))

print("Percentage >= $1 million:",
      np.mean(millionaire_properties[np.isfinite(price)]) * 100)


# ==========================================
# 9. COUNTING CITIES, STATES AND STATUS
# ==========================================

print("\n--- CATEGORICAL ANALYSIS ---")

unique_cities, city_counts = np.unique(city, return_counts=True)
unique_states, state_counts = np.unique(state, return_counts=True)
unique_status, status_counts = np.unique(status, return_counts=True)

print("Unique cities:", unique_cities)
print("City counts:", city_counts)

print("Unique states:", unique_states)
print("State counts:", state_counts)

print("Property statuses:", unique_status)
print("Status counts:", status_counts)

# Most common city and state
print("Most common city:",
      unique_cities[np.argmax(city_counts)],
      np.max(city_counts))

print("Most common state:",
      unique_states[np.argmax(state_counts)],
      np.max(state_counts))

# Price statistics by city
for c in unique_cities:
    mask = (city == c) & np.isfinite(price)

    if np.any(mask):
        print("City:", c)
        print("Count:", np.sum(mask))
        print("Mean price:", np.mean(price[mask]))
        print("Median price:", np.median(price[mask]))

# Price statistics by state
for s in unique_states:
    mask = (state == s) & np.isfinite(price)

    if np.any(mask):
        print("State:", s)
        print("Count:", np.sum(mask))
        print("Mean price:", np.mean(price[mask]))

city_means = np.array([
    np.mean(price[(city == c) & np.isfinite(price)])
    for c in unique_cities
])

print("City with highest mean price:",
      unique_cities[np.argmax(city_means)],
      np.max(city_means))

print("City with lowest mean price:",
      unique_cities[np.argmin(city_means)],
      np.min(city_means))


# ==========================================
# 10. PROPERTY STATUS ANALYSIS
# ==========================================

print("\n--- PROPERTY STATUS ---")

for s in unique_status:
    mask = (status == s) & np.isfinite(price)

    if np.any(mask):
        print("Status:", s)
        print("Count:", np.sum(mask))
        print("Mean price:", np.mean(price[mask]))
        print("Median price:", np.median(price[mask]))


# ==========================================
# 11. TWO-DIMENSIONAL ARRAY
# ==========================================

print("\n--- 2D ARRAY ---")

D2PriceSize = np.array([price, house_size])

print("2D array:", D2PriceSize)
print("Dimensions:", D2PriceSize.ndim)
print("Total elements:", D2PriceSize.size)
print("Shape:", D2PriceSize.shape)
print("Data type:", D2PriceSize.dtype)

print("Mean of rows:", np.nanmean(D2PriceSize, axis=1))
print("Maximum of rows:", np.nanmax(D2PriceSize, axis=1))
print("Minimum of rows:", np.nanmin(D2PriceSize, axis=1))
print("Sum of columns:", np.nansum(D2PriceSize, axis=0))


# ==========================================
# 12. SLICING AND INDEXING
# ==========================================

print("\n--- SLICING ---")

print("Slice 1:", D2PriceSize[0:1, 1:5])
print("Slice 2:", D2PriceSize[:1, 4:15:4])

print("First 5 prices:", price[:5])
print("Last 5 prices:", price[-5:])
print("Every 10th price:", price[::10])

print("First 5 cities:", city[:5])
print("Last 5 cities:", city[-5:])

print("First property price:", D2PriceSize[0, 0])
print("First property house size:", D2PriceSize[1, 0])


# ==========================================
# 13. LOOPING THROUGH ARRAYS
# ==========================================

print("\n--- LOOPING ---")

count = 0

for elem in np.nditer(D2PriceSize):
    print(elem)
    count += 1

    if count == 5:
        break

count = 0

for index, elem in np.ndenumerate(D2PriceSize):
    print(index, elem)
    count += 1

    if count == 5:
        break


# ==========================================
# 14. RESHAPE, FLATTEN, TRANSPOSE
# ==========================================

print("\n--- ARRAY TRANSFORMATIONS ---")

total = D2PriceSize.size
D2Reshape = D2PriceSize.reshape(1, total)

print("Reshaped array:", D2Reshape)
print("Size:", D2Reshape.size)
print("Dimensions:", D2Reshape.ndim)
print("Shape:", D2Reshape.shape)

# Split into rows dynamically instead of assuming
# a fixed number of records.
D2Grid = np.array_split(price, 20)

print("Number of groups:", len(D2Grid))
print("First group mean:", np.nanmean(D2Grid[0]))

print("Flattened array:", D2PriceSize.flatten())

transposed = D2PriceSize.T

print("Transposed shape:", transposed.shape)
print("First 5 rows of transpose:", transposed[:5])


# ==========================================
# 15. JOINING AND SPLITTING
# ==========================================

print("\n--- JOIN AND SPLIT ---")

stacked = np.column_stack((price, house_size))

print("Stacked price and size:", stacked)
print("Stacked shape:", stacked.shape)

joined = np.concatenate((price[:5], house_size[:5]))

print("Joined arrays:", joined)

parts = np.array_split(price[:10], 5)

print("Price split into 5 parts:", parts)

groups = np.array_split(price, 5)

for g in groups:
    print("Group size:", g.size)
    print("Group mean:", np.nanmean(g))


# ==========================================
# 16. HISTOGRAM, LINSPACE, NORMALIZATION
# ==========================================

print("\n--- DISTRIBUTION ---")

valid_price = price[np.isfinite(price)]

counts, edges = np.histogram(valid_price, bins=5)

print("Price histogram counts:", counts)
print("Price histogram edges:", edges)

valid_bed = bed[np.isfinite(bed)]

counts, edges = np.histogram(valid_bed, bins=np.arange(0, 9))

print("Bedroom histogram counts:", counts)
print("Bedroom histogram edges:", edges)

print("5 equally spaced prices:",
      np.linspace(np.min(valid_price), np.max(valid_price), 5))

price_norm = (price - np.nanmin(price)) / (
    np.nanmax(price) - np.nanmin(price)
)

print("Normalized price:", price_norm)

price_z = (price - np.nanmean(price)) / np.nanstd(price)

print("Price z-scores:", price_z)
print("Z-score mean:", np.nanmean(price_z))
print("Z-score std:", np.nanstd(price_z))


# ==========================================
# 17. OUTLIERS AND MISSING VALUES
# ==========================================

print("\n--- OUTLIERS ---")

price_z = (price - np.nanmean(price)) / np.nanstd(price)

outliers = np.abs(price_z) > 3

print("Z-score outlier count:", np.sum(outliers))
print("Outlier cities:", city[outliers])
print("Outlier prices:", price[outliers])

q1, q3 = np.nanpercentile(price, [25, 75])
iqr = q3 - q1

lower = q1 - 1.5 * iqr
upper = q3 + 1.5 * iqr

iqr_outliers = (price < lower) | (price > upper)

print("IQR lower bound:", lower)
print("IQR upper bound:", upper)
print("IQR outlier count:", np.sum(iqr_outliers))
print("IQR outlier cities:", city[iqr_outliers])
print("IQR outlier prices:", price[iqr_outliers])

print("\n--- MISSING VALUES ---")

print("Missing broker IDs:", np.isnan(data["brokered_by"]).sum())
print("Missing prices:", np.isnan(price).sum())
print("Missing bedrooms:", np.isnan(bed).sum())
print("Missing bathrooms:", np.isnan(bath).sum())
print("Missing lot sizes:", np.isnan(acre_lot).sum())
print("Missing house sizes:", np.isnan(house_size).sum())

print("Missing cities:", np.sum(city == ""))
print("Missing states:", np.sum(state == ""))
print("Missing statuses:", np.sum(status == ""))
print("Missing sold dates:", np.sum(year == ""))

# Median imputation using NumPy only
bed_filled = np.where(np.isnan(bed), np.nanmedian(bed), bed)
bath_filled = np.where(np.isnan(bath), np.nanmedian(bath), bath)

lot_filled = np.where(
    np.isnan(acre_lot), np.nanmedian(acre_lot), acre_lot
)

size_filled = np.where(
    np.isnan(house_size), np.nanmedian(house_size), house_size
)

print("Missing bedrooms after filling:", np.isnan(bed_filled).sum())
print("Missing bathrooms after filling:", np.isnan(bath_filled).sum())
print("Missing lot sizes after filling:", np.isnan(lot_filled).sum())
print("Missing house sizes after filling:", np.isnan(size_filled).sum())

# Duplicate and unique values
print("Unique cities:", np.unique(city).size)
print("Unique states:", np.unique(state).size)
print("Unique property statuses:", np.unique(status).size)

# Final summary
print("\n--- FINAL SUMMARY ---")

print("Total properties:", price.size)
print("Average price:", np.nanmean(price))
print("Median price:", np.nanmedian(price))
print("Minimum price:", np.nanmin(price))
print("Maximum price:", np.nanmax(price))
print("Average house size:", np.nanmean(house_size))
print("Average bedrooms:", np.nanmean(bed))
print("Average bathrooms:", np.nanmean(bath))
print("IQR outlier count:", np.sum(iqr_outliers))
