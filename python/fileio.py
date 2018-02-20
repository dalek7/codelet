# based on https://stackoverflow.com/a/28440249
import numpy as np

a = np.array([1, 2, 3, 4])
np.savetxt('test1.txt', a, fmt='%d')
b = np.loadtxt('test1.txt', dtype=int)

print(a)
print(b)
print(a == b)


a = np.array([1.1, 2.5, 3.0, 4])
np.savetxt('test1.txt', a, fmt='%f')
b = np.loadtxt('test1.txt', dtype=float)

print(a)
print(b)
print(a == b)
