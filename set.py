# Sets are used to store multiple items in a single variable. #
# A set is a collection which is unordered, unchangeable*, and unindexed. #
# No duplicates #
# Once a set is created, you cannot change its items, but you can remove items and add new items. #

myset = {"apple","banana", "payapa", "orange"}
print(myset)
print(type(myset))
print(len(myset))

set1 = {"abc", 34, True, 40, "male"}
print(set1)
thisset = set(("apple","banana", "cherry"))
print(thisset)

# Access | Loop #
for x in thisset: 
    print(x)

# Once a set is created, you cannot change its items, but you can add new items.
# Add item to set #
thisset.add("orange")
print(thisset)

set11 = {1, 3, 5}
set22 = { 6, 7, 4}
iter = [9,4,2]
set11.update(set22)
print(set11)
set22.update(iter)
print(set22)

# Remove Set #

demoset = { "apple", "ball", "cherry" }
demoset.remove("ball") # Note: If the item to remove does not exist, remove() will raise an error.
demoset.discard("ball") # Note: If the item to remove does not exist, discard() will NOT raise an error.
print(demoset)

# You can also use the pop() method to remove an item, but this method will remove a random item, so you cannot be sure what item that gets removed.
popset = {1,5,2,6}
popset.pop()
print(popset)

popset.clear() # Empty set
print(popset)

# Join Set #
setOne = {1,4,2,3}
setTwo = {"app", "web"}

setThree = setOne.union(setTwo)
print(setThree)

setTwo.update(setThree)
print(setTwo)

setOne1 = {1,4,2,3, "app"}
setTwo2 = {"app", "web"}
setTwo2.intersection_update(setOne1) # update and return duplicate items only
print(setTwo2)

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.intersection(y) # return duplicate items only
print(z)

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.symmetric_difference(y) # remove duplicates && return non duplicate items only
print(z)

# Set Methods #
'''
Method	                            Description
add()	                            Adds an element to the set
clear()	                            Removes all the elements from the set
copy()	                            Returns a copy of the set
difference()	                    Returns a set containing the difference between two or more sets
difference_update()	                Removes the items in this set that are also included in another, specified set
discard()	                        Remove the specified item
intersection()	                    Returns a set, that is the intersection of two other sets
intersection_update()	            Removes the items in this set that are not present in other, specified set(s)
isdisjoint()	                    Returns whether two sets have a intersection or not
issubset()	                        Returns whether another set contains this set or not
issuperset()	                    Returns whether this set contains another set or not
pop()	                            Removes an element from the set
remove()	                        Removes the specified element
symmetric_difference()	            Returns a set with the symmetric differences of two sets
symmetric_difference_update()	    inserts the symmetric differences from this set and another
union()	                            Return a set containing the union of sets
update()	                        Update the set with the union of this set and others
'''