# Create Class #
# use the class keyword

class MyClass:
    x = 5
    y = 7

myObj = MyClass()
print(myObj.x)
print(myObj.y)

class MyClass2:
    def __init__(self,name,age): # constructor
        self.name = name
        self.age = age

    def __str__(self): # string representation
        return f"{self.name}({self.age})"
    
    def info(self):
        print("Name: "+self.name)
        print("Age: {}".format(self.age))
    
myObj2 = MyClass2("Anil",25)
print(myObj2.name)
print(myObj2.age)
print(myObj2)
myObj2.info()


# The self Parameter #

class MyClass3:
    def __init__(ggobj, name, age):
        ggobj.name = name
        ggobj.age = age
    
    def myfunc(abc):
        print("My name is ",abc.name)

obj1 = MyClass3("Anil",25)
obj1.myfunc()

# modify property
obj1.name = "Jhon"
obj1.myfunc()

# delete property | object
del obj1.age
del obj1

# pass statement #
'''
class definitions cannot be empty, but if you for some reason have a class
definition with no content, put in the pass statement to avoid getting an error.
'''
class Person:
    pass