import numpy as np

## Joining ## 
arr1 = np.array([1,2,3,4])
arr2 = np.array([5,6,7,8])
arr = np.concatenate((arr1,arr2)) # 1-D
print(arr)

arr1 = np.array([[1,2,3],[4,5,6]])
arr2 = np.array([[7,8,9],[10,11,12]])
arr = np.concatenate((arr1, arr2), axis=1) # 2-D
print(arr)

arr1 = np.array([1,2,3,4])
arr2 = np.array([5,6,7,8])
arr = np.stack((arr1,arr2)) # 1-D Stack function
print(arr)
arr = np.hstack((arr1,arr2)) # 1-D hstack function horizontal row
print(arr)
arr = np.vstack((arr1,arr2)) # 1-D hstack function vertical column
print(arr)
arr = np.dstack((arr1,arr2)) # 1-D hstack function height depth
print(arr)
## End Joining ## 

## Splitting ##
arr = np.array([1,2,3,4,5,6])
newarr = np.array_split(arr,3) # 1-D split
print(newarr)

arr = np.array([[1,2],[3,4],[5,6],[7,8],[9,10],[11,12]])
newarr = np.array_split(arr,3) # 2-D split
print(newarr)

newarr = np.array_split(arr, 3, axis = 1)
print(newarr)

arr = np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12],[13,14,15],[16,17,18]])
newarr = np.hsplit(arr, 3)
print(newarr)

## End Splitting ##

