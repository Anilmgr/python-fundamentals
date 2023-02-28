import random

x = 1       # int 
y = 5.5     # float
z = 1j      # complex

# Type conversion #

# int to float
a = float(x)
print(type(a))

# float to int
b = int(y)
print(type(b))

# int to complex
c = complex(x)
print(type(c))

# Using random module #

# returns random number between 1-100
print (random.randrange(1,100))