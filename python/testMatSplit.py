import numpy as np

X1 = np.array([  [ 1., -1.,  2.],
                 [ 2.,  0.,  0.],
                 [ 0.,  1., -1.],
                 [ -1., 0., -1.5]
                 ])

X1_0 = X1[:,0][np.newaxis].T
X1_1 = X1[:, 1:3]

X1recon = np.hstack((X1_0, X1_1))

print(X1)
print('=============')
print(X1_0)
print('++')
print(X1_1)
print('=')
print(X1recon)

#X_train2 = X_train[:,0:2]
#print(X_train2)
