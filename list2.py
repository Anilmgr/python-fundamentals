# List Comprehension #
fruits = ["apple", "banana", "cherry", "mango", "papaya"]

# newlist = [expression for item in iterable if condition == True]

filteredList = [x for x in fruits if "a" in x] 
print(filteredList)

filteredList2 = [x.upper() for x in fruits if x != "apple"]
print(filteredList2) 

filteredList3 = [ x if x != "banana" else "orange" for x in fruits]
print(filteredList3)

# List Sort #
numList = [5,2,3,1,4]
numList.sort()
print(numList) #Ascending
numList.sort(reverse=True)
print(numList) #Descendig

def myfunc(n):
    return abs(n-5)
thisList = [7,5,4,15,3]
thisList.sort(key=myfunc)
print(thisList)

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key=str.lower)
print(thislist)

upOrder = ["ant","apple",'animal']
upOrder.reverse()
print(upOrder)

# Copy List #
oldList = ["cat","dog","cow"]
print(oldList)
# newList = oldList will only be reference to oldList
newList = oldList.copy()
newList = list(oldList)
print(newList)

# Join List #
listA = ["sprite", "coke", "fanta"]
listB = ["dew", "pepsi", "7up"]
listC = ["frooti", "real", "mirinda"]
listD = listA + listB
print(listD)

for x in listB:
    listA.append(x)
print(listA)

listB.extend(listC)
print(listB)

# List Methods #
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
remove()	Removes the item with the specified value
reverse()	Reverses the order of the list
sort()	    Sorts the list
'''
