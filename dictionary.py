# Dictionary #
# Dictionaries are used to store data values in key:value pairs.

thisdict = {
    "name": "Anil",
    "age" : 25
}

print(thisdict)
print(type(thisdict))
print(thisdict["name"])

# As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.
# Changable
# No duplicates allowed (overwrite value)

print(len(thisdict)) # key:value pair count

mydict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}

print(mydict)
print(type(mydict))

mydict2 = dict(name="Anil",role="Dev")
print(mydict2)

# Access Dictionary #
print(mydict2["name"])
print(mydict2.get("name"))
print(mydict2.keys())   # dict_keys(['name','role'])
print(mydict2.values())   # dict_values(['Anil','Dev'])

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
x = car.values()
print(x) #before the change
car["color"] = "red"
print(x) #after the change

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
x = car.items()
print(x) #before the change
car["year"] = 2020
print(x) #after the change

if "model" in car:
    print("model key exist")

# Change Dictionary #

demodict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

demodict["year"] = 2012
print(demodict)

demodict.update({"model":"Macleran"})
print(demodict)

demodict["type"] = "Sports"
print(demodict)

# Remove items #

mydic = {
    "type": "tropical",
    "name": "Mango",
    "season" : "summer"
}

print(mydic) # before pop
mydic.pop("season")
print(mydic) # after pop
mydic.popitem() # The popitem() method removes the last inserted item 

mydic.clear() # empties the dictionary