import numpy as np

a = np.arange(25). reshape(5,5)
print(a)

mask = ([0,1,2,3], [1,2,3,4])
print(mask, end='\n\n')

mask_div_by_3 = mask % 3 == 0

print(mask_div_by_3)

print(a[mask])

print(a[mask_div_by_3])