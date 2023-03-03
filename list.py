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

########################################################################################################

myList = ["dell", "acer", "asus", "msi", "apple"]

# Access List item
print(myList[0], myList[3], myList[-1])
print(myList[1:3])          # Range start:1 end:3 excludes 3
print(myList[:4])
print(myList[2:])
print(myList[-4:-1])

# item exist
if "dell" in myList:
    print("Got dell item in list")

# Change item value
myList1 = ["apple", "banana", "cherry"]
myList1[1] = "mango"
print(myList1)      # Returns ['apple', 'mango', 'cherry']


myList2 = ["dell","acer","apple"]
myList2[1:3] = ["asus","msi"]
# myList2[1:2] = ["asus","msi"]     # Appends value if value is more than replace
# myList2[0:3] = ["asus","msi"]     # Remove values if value is less than replace
print(myList2)      # Returns ['dell','asus', 'msi']

# Add List Items #
# append item
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)     # Returns ['apple','banana','cherry', 'orange']

# insert item
thislist.insert(2, "grapes")
print(thislist)      # Returns ['apple', 'banana', 'grapes', 'cherry', 'orange']

# extend list
fList1 = ["apple", "mango"]
fList2 = ["orange", "cherry"]
fList1.extend(fList2)
print(fList1)

mylist = ["apple", "banana", "cherry"]
mytuple = ("kiwi", "orange")
mylist.extend(mytuple)      # Add Any Iterable
print(mylist)


# Remove Item from List #

demoList = ["apple","dell", "asus", "acer", "hp"]
demoList.remove("hp")
print(demoList)         # Returns ['apple', 'dell', 'asus', 'acer']

demoList.pop(1)
print(demoList)         # Returns ['apple', 'asus', 'acer']

demoList.pop()
print(demoList)         # Returns ['apple', 'asus']

demoList = ["apple","dell", "asus", "acer", "hp"]
del demoList[0]
print(demoList)         # Returns ['dell', 'asus', 'acer', 'hp']

# del demoList          # delete entire list set undefined

demoList.clear()        # Empty the list
print(demoList)         # Returns []

# Loop Lists #
brandList = ["apple","oneplus","samsung","xiaomi"]

for brand in brandList:
    print(brand)

for i in range(len(brandList)):
    print(brandList[i])

idx = 0
while(idx < len(brandList)):
    print(brandList[idx])
    idx += 1

# Looping using list comprehension
[print(x) for x in brandList]