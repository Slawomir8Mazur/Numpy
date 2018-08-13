import numpy as np

one_dim = np.array([1,2,3])
print(one_dim)

two_dim = np.array([[11,12,13], [21,22,23]])
print(two_dim)

two_dim_2 = two_dim - 1
print(two_dim_2)

print(two_dim.dtype)
print(two_dim.shape)
two_dim[1,2] = 2233
print(two_dim)