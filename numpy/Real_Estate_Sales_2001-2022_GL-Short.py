import numpy as np

np.set_printoptions(threshold=np.inf, linewidth=np.inf)


SerialNumber,ListYear,DateRecorded,Town,Address,AssessedValue,SaleAmount,SalesRatio,PropertyType,ResidentialType,NonUseCode,AssessorRemarks,Oremarks,Location =np.genfromtxt(r"numpy\Real_Estate_Sales_2001-2022_GL-Short.csv",delimiter=",",usecols=(0,1,2,3,4,5,6,7,8,9,10,11,12,13),dtype=None,unpack=True,skip_header=1,invalid_raise=False,comments=None)
print(SerialNumber)
print(ListYear)
print(DateRecorded)
print(Town)
print(Location)
print(Address)
print(AssessedValue)
print(SaleAmount)


print(type(SaleAmount))
print(Address.dtype)
print(PropertyType)
print(Oremarks)

