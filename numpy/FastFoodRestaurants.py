import numpy as np

np.set_printoptions(threshold=np.inf, linewidth=np.inf)

address, latitude , longitude , name, = np.genfromtxt(r"numpy\FastFoodRestaurants_fixed_comma.csv",
                                                                delimiter=',',
                                                                usecols=(0, 4, 5, 6),
                                                                unpack=True,
                                                                dtype=('U100', 'f8', 'f8', 'U100'),   # force correct types
                                                                encoding='utf-8',
                                                                skip_header=1,
                                                                invalid_raise=False)

print(address)
print(latitude)
print(longitude)
print(name)

cleaned_longitude = longitude[~np.isnan(longitude)]
# Zameen.com price  - statistics operations
print("US Food Restaurant DataSet longitude mean:", np.nanmean(longitude))
print("US Food Restaurant DataSet longitude average:", np.nanmean(longitude))  # same as mean
print("US Food Restaurant DataSet longitude std:", np.nanstd(longitude))
print("US Food Restaurant DataSet longitude median: ",np.nanmedian(longitude))
print("US Food Restaurant DataSet longitude percentile - 25:", np.percentile(cleaned_longitude, 25))
print("US Food Restaurant DataSet longitude percentile - 75:", np.percentile(cleaned_longitude, 75))
print("US Food Restaurant DataSet longitude percentile - 3:", np.percentile(cleaned_longitude, 3))
print("US Food Restaurant DataSet longitude max:", np.nanmax(longitude))
print("US Food Restaurant DataSet longitude min:", np.nanmin(longitude))

print("cos of the value",np.cos(latitude))
