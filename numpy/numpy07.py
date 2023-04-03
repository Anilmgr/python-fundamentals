from numpy import random
import numpy as np

## Data distribution ##
# Probability Density Function: A function that describes a continuous probability. i.e. probability of all values in an array.

x = random.choice([3, 5, 7, 9], p=[0.1, 0.3, 0.6, 0.0], size=(100))
y = random.choice([3, 5, 7, 9], p=[0.1, 0.3, 0.6, 0.0], size=(3, 5))
print(x)
print(y)

## Random Permutation ##
# shuffle() method makes changes to the original array.
# permutation() method returns a re-arranged array (and leaves the original array un-changed).

arr = np.array([1, 2, 3, 4, 5])
random.shuffle(arr)
print(arr)

arr1 = np.array([1, 2, 3, 4, 5])
print(random.permutation(arr1))