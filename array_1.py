# Note: Python does not have built-in support for Arrays, but Python Lists can be used instead. #

fruits = ["apple", "banana", "cherry", "mango", "orange"]

# Access
print(fruits[0])

# Modify
fruits[0] = "papaya"
print(fruits[0])

# len
print(len(fruits))

# append 
fruits.append("pineapple")
print(fruits)

# pop | remove
fruits.pop(1) # remove element of idx=1
print(fruits)
fruits.remove("cherry")
print(fruits)

# loop array
for x in fruits:
    print(x)

# Methods #
# Python has a set of built-in methods that you can use on lists/arrays.
'''
Method	    Description
append()	Adds an element at the end of the list
clear()	    Removes all the elements from the list
copy()	    Returns a copy of the list
count()	    Returns the number of elements with the specified value
extend()	Add the elements of a list (or any iterable), to the end of the current list
index()	    Returns the index of the first element with the specified value
insert()	Adds an element at the specified position
pop()	    Removes the element at the specified position
remove()	Removes the first item with the specified value
reverse()	Reverses the order of the list
sort()	    Sorts the list
'''
