import numpy as np

a = np.array([1,2,3,4])
b = np.array([5,6,7,8])

c = np.vstack((a,b))

print(c)
'''
[[1 2 3 4]
 [5 6 7 8]]
'''
print(c.shape)
'''
(2, 4)
'''

d = np.hstack((a,b))
print(d)
'''
[1 2 3 4 5 6 7 8]
'''


a0 = np.array([1,2,3,4])
a = a0[np.newaxis]

b = np.array([5,6,7,8])[np.newaxis]
at = a.T

print('-----------')
print(a0)
print(a0.shape)

print(a)
print(a.shape)

print(at)
print(at.shape)
print('-----------')

'''
[[1]
 [2]
 [3]
 [4]]
'''
c = np.hstack((a.T,b.T))
print(c)
'''
[[1 5]
 [2 6]
 [3 7]
 [4 8]]
 '''