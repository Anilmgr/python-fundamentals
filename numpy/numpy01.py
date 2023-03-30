import numpy as np

x = np.array([11,22,33,44,55])
y = np.array([[1,2,3],[4,5,6]])
z = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])

print(x[0], x[1]) # accessing 1-D
print(y[0,0], y[1,0]) # accessing 2-D
print(y[1,-1]) # negatie indexing
print(z[0,1,2]) # accessing 3-D

# Array Slicing

print(x[0:2])
print(x[2:])
print(x[:3])
print(x[-3:-1])
print(x[0:5:2]) # step

print(y[0,0:2])
print(y[0:2,0:2])

# numpy array data types
'''
i - integer
b - boolean
u - unsigned integer
f - float
c - complex float
m - timedelta
M - datetime
O - object
S - string
U - unicode string
V - fixed chunk of memory for other type ( void )
'''

arr = np.array([11,22,33,44])
arr1 = np.array([11,22,33,44], dtype="S")
arr2 = np.array([1.1,2.2,3.3,4.4])
print(arr.dtype)
print(arr1.dtype)

newarr2 = arr2.astype("i")
print(arr2.dtype)
print(newarr2)
print(newarr2.dtype)
