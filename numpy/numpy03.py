import numpy as np

arr = np.array([1,2,3,4,5])

for x in arr:
    print(x)

arr1 = np.array([[1,2,3],[4,5,6],[7,8,9]])
for x in arr1:
    for y in x:
        print(y)

arr2 = np.array([[[11,22,33],[44,55,66]],[[77,88,99],[21,22,23]]])
for x in np.nditer(arr2):
    print(x)

arr3 = np.array([1,2,3,4])
for idx, x in np.ndenumerate(arr3):
    print(idx, x)

arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
for idx, x in np.ndenumerate(arr):
  print(idx, x)