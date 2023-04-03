from numpy import random

x = random.rand()                   # 0-1
print(x)

y = random.randint(100, size=(5))   # 0-100, size => array
print(y)

z = random.randint(100, size=(3, 5)) # 0-100, 2-D
print(z)

print(random.rand(5))
print(random.rand(3,5))

print(random.choice([1,3,5,7], size=(2,2)))