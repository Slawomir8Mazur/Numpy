import numpy as np
#Bitwise operators:
# & and
# | or
# ^ xor
# ~ not

#Fancy indexing -> using a mask -> variable[mask] -> mask is array of the same size as variable     #OWNDATA True
#Slicing -> variable[:,::2]                                                                         #OWNDATA False
#Fancy indexing creates a copy, slicing creates a view(operates on the same object

var = np.arange(-30,80,10)
print(var)
mask = var < 30
print(mask)

print(var[mask])
print(var[var<0])

#negatives stores copy of var with negative values altered to 0
negatives = var.copy()
negatives[negatives<0] = 0
print(negatives)
print(var)

#np.nonzero(var) - return tuple with positions of nonzero values in var
print(np.nonzero(mask))
print(np.nonzero((var<-10) | (var>20)))
print((var<-10) | (var>20))