import numpy as np

## search ##
arr = np.array([1,2,3,4,5,6,7])
x = np.where(arr == 4) # where(condition)
y = np.where(arr%2 == 0)
z = np.searchsorted(arr, 2)
q = np.searchsorted(arr, 2, side='right')
r = np.searchsorted(arr, [2,4,6])
print(x)
print(y)
print(z)
print(q)
print(r)
## end search ##

## sort ##
arr = np.array([3,1,5,6,2,4])
print(np.sort(arr))

arr = np.array(['cat', 'apple', 'dog'])
print(np.sort(arr))

arr = np.array([[3,1,5],[6,2,4]])
print(np.sort(arr))
## end sort ##

## filter ##
arr = np.array([1,2,3,4,5,6,7,8])
x = [False,True,True,False,True,True,False,True]
newarr = arr[x]
print(newarr)

filter_arr = []
for x in arr:
    filter_arr.append(x%2==0)

newarr = arr[filter_arr]
print(newarr)

y = arr%2 == 1
newarr = arr[y]
print(newarr)
## end filter ##