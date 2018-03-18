import numpy as np

arr1 = np.loadtxt('../data/data1.csv', delimiter=',' , dtype='float', usecols=(0,2,4))

print(arr1)