# https://stackoverflow.com/a/26553855

import numpy

arr = numpy.zeros((50,100,25))
new_arr = arr.reshape(-1, arr.shape[-1])

print(arr.shape)
print(new_arr.shape)

'''
(50, 100, 25)
(5000, 25)
'''