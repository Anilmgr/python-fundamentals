# In Python a function is defined using the def keyword: #

# creating function
def myFunction():
    print("Hello World")

# calling function
myFunction()

# arguments
def nameFunc(name): 
    print("My name is",name)

nameFunc("Anil") 

# arbitrary
def myfunction(*kids):
    print("The youngest child is " + kids[2])

myfunction("Emil", "Tobias", "Linus")

# keyword arguments
def my_function(child3, child2, child1):
  print("The youngest child is " + child3)

my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")

# Arbitrary Keyword Arguments, **kwargs
def myfunc(**kid):
    print("Lastname: "+kid["lname"])

myfunc(fname="Anil", lname="Baral")

# Default Parameter
def countryfunc(country="Nepal"):
    print("Country: "+country)

countryfunc()
countryfunc("India")

# passing list as argument
def showList(items):
    for item in items:
        print(item)

fruits = ["apple", "ball", "cat"]
showList(fruits)

# return value
def sum(x,y):
    return x+y

print(sum(4,5))

# pass statement
'''
function definitions cannot be empty, 
but if you for some reason have a function definition with no content, 
put in the pass statement to avoid getting an error.
'''
def passFunc():
    pass

# Recursion 
def recursionFunc(n):
    if(n > 0):
        result = n + recursionFunc(n - 1)
        print('Result:',result)
    else:
        result = 0
    return result;    

recursionFunc(5)