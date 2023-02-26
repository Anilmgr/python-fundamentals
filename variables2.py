myvar = "Anil" # lower case
my_var = "Anil" # sanke case
_my_var = "Anil"
myVar = "Anil" # camel case
MyVar = "Anil" # pascal case
MYVAR = "Anil" # upper case
myvar2 = "Anil"

x, y, z = 5, 10, 15 # assinging multiple values to multiple variables
print(x)
print(y)
print(z)

p = q = r = 5 # assinging single value to multiple variables
print(p)
print(q)
print(r)

fruits = ['apple', 'banana', 'cherry']
a, b, c = fruits # unpacking collection
print(a)
print(b)
print(c)
print(a,b,c)

def testFunc():
    global n # defining global varibale 
    n = "RocK You"
    print("We will " + n)

testFunc()

print("We will " + n)