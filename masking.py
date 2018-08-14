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
print(var[var<0], end='\n\n')

#Fancy indexing
var_fan = np.array([[k, k+1, k+2, k+3] for k in range(0, 16, 4)])
var_fan2 = np.arange(25).reshape(5,5)
print(var_fan2, end='\n\n')

print(var_fan2[[1,2,3,4], [0,1,2,3]])
print(var_fan2[[3], [0,2,4]])
print(var_fan2[mask[:5], mask[:5]], end='\n\n')


#negatives stores copy of var with negative values altered to 0
negatives = var.copy()
negatives[negatives<0] = 0
print(negatives)
print(var)

#np.nonzero(var) - return tuple with positions of nonzero values in var
mask = (var<-10) | (var>20)
print(np.nonzero(mask))