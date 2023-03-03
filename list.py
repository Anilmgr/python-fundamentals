'''
================= Python Collections (Arrays) =========================
There are four collection data types in the Python programming language:

List is a collection which is ordered and changeable. Allows duplicate members.
Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
Dictionary is a collection which is ordered** and changeable. No duplicate members.
'''
# LIST #

fruitList = ["cherry", "banana", "grapes", "orange"]
print(fruitList)

# Properties #

# 1. Changable
fruitList[0] = "apple"
print(fruitList)

# 2. Allow Duplicates
foodList = ["momo", "pizza", "momo"]
print(foodList)

# Length #
print(len(fruitList))       # Returnns 4

# Type #
print(type(fruitList))      # Returns <class 'list'>

# List items = Data Types

list1 = [1,2,3,4]
list2 = ["item1", "item2", "item3"]
list3 = [True, False, True]

list4 = [1, "item", False, "male"]

# List constructor #
thislist = list(("gmail.com", "yahoo.com", "outlook.com"))
print(thislist)