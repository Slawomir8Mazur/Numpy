import numpy as np


table1 = np.arange(25)
#print(table1[:12].reshape(3,4))     #reshape doesn't modify the object
table1 = table1.reshape(5,5)
print(table1)

redmark_table = table1[:, 1::2]
yellow_mark = table1[4,:]
blue_mark = table1[1::2, 0:3:2]
print(redmark_table)
print(yellow_mark)
print(blue_mark)

redmark_table1 = redmark_table[:,:].copy()

print(redmark_table1.flags['OWNDATA'])
print(table1.data)
