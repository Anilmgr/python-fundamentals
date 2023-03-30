import numpy as np
 
arr = np.array([1,2,3,4,5])

cparr = arr.copy() # copy and create new array
vwarr = arr.view() # reference array

print(cparr.base)   #None
print(vwarr.base)   #Original array

print(cparr)
print(vwarr)

arr[0] = 6

print(cparr)
print(vwarr)

x = np.array([[1,2,3,4],[5,6,7,8]])
y = np.array([1,2,3,5], ndmin=5)
print(x.shape)
print(y.shape)

# 1-D to 2-D
z = np.array([1,2,3,4,5,6,7,8])
zn = z.reshape(2,4)
print(zn)

a = np.array([[1,2,3,4],[5,6,7,8]])
an = a.reshape(-1) # flatening
print(an)
