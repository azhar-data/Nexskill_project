import numpy as np
v1,v2,v3,v4=np.genfromtxt(r"RealEstate-USA.csv",delimiter=",",usecols=(0,4,8,9),unpack=True,dtype=None,skip_header=1)
print(v1)
print(v2)
print(v3)
print(v4)

print(np.min(v2))
print(np.max(v1))
print(np.size(v2))
