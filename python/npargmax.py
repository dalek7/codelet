# https://docs.scipy.org/doc/numpy/reference/generated/numpy.argmax.html

import numpy as np
a = np.arange(6).reshape(2,3)
print(a)
v1 = np.argmax(a)
v2 = np.argmax(a, axis=0)
v3 = np.argmax(a, axis=1)

print(v1)
print(v2)
print(v3)

'''
[[0 1 2]
 [3 4 5]]
5
[1 1 1]
[2 2]
'''