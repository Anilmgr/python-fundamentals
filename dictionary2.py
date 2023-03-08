# Loop Dictionary #
mydict = {
    "name" : "Anil",
    "age" : 25,
    "email" : "email@gmail.com",
    "married" : False,
    "hobbies" : ["Traveling", "Jamming", "Sports"]
}

for x in mydict:
    print(x)            # return key
    print(mydict[x])    # return value

for x in mydict.values():
    print(x)            # return value

for x in mydict.keys():
    print(x)            # return key

for x, y in mydict.items():
    print(x, y)         # return key, value

# Copy Dictionary #

thisdict = {
    "name": "Jhon",
    "age": 31
}

mydict = thisdict.copy()
print(mydict)

mydict2 = dict(thisdict)
print(mydict2)

# Nested Dictionary #

myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

print(myfamily["child1"]["name"])

# Dictionary methods #
'''
Method	        Description
clear()	        Removes all the elements from the dictionary
copy()	        Returns a copy of the dictionary
fromkeys()	    Returns a dictionary with the specified keys and value
get()	        Returns the value of the specified key
items()	        Returns a list containing a tuple for each key value pair
keys()	        Returns a list containing the dictionary's keys
pop()	        Removes the element with the specified key
popitem()	    Removes the last inserted key-value pair
setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
update()	    Updates the dictionary with the specified key-value pairs
values()	    Returns a list of all the values in the dictionary
'''

