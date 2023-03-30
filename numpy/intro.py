## Numerical Python NumPy
# working with arrays. | ndarray
# offers functions for working in domain of linear algebra, fourier transform, and matrices.

import numpy as np

print(np.__version__) #check numpy version

# array

x = np.array([1,3,4,5])

print(x)
print(type(x))

# dimensions 0-D, 1-D, 2-D...

d0 = np.array(20)
d1 = np.array([2,4,6,7])
d2 = np.array([[1,2,3],[4,5,6]])
d3 = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])

print(d0)
print(d0.ndim)
print(d1)
print(d1.ndim)
print(d2)
print(d2.ndim)
print(d3)
print(d3.ndim)

# higher dimension

hd = np.array([1,2,3,4], ndmin=5)

print(hd)
print(hd.ndim)