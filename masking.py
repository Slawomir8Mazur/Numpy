import numpy as np

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