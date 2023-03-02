# bool values => True or False #

print(10>9)
print(10<9)

age = 18
if age >= 16:
    print("You are eligible to cast vote.")
else:
    print("You are not eligible to cast vote.")

# Evaluate Values & Variables #
a = "Hello"
b = 15

print(bool(a))                  # returns True
print(bool(b))                  # returns True
print(bool("test"))             # returns True
print(bool(['apple','ball']))   # returns True
print(bool(False))              # returns False
print(bool(None))               # returns False
print(bool(''))                 # returns False
print(bool(0))                  # returns False
print(bool(()))                 # returns False
print(bool({}))                 # returns False
print(bool([]))                 # returns False

#  if you have an object that is made from a class with a __len__ function that returns 0 or False: #
class myclass():
    def __len__(self):
        return 0

myobj = myclass()
print(bool(myobj))

# Function returning boolean #
def testFnc():
    return True

print(testFnc())

# Check instance #

t = 1000
print(isinstance(t, int))