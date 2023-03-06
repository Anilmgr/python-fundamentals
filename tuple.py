# A tuple is a collection which is ordered and unchangeable.
mytuple = ("apple", "banana", "cherry")
print(mytuple)
print(type(mytuple))

tuple1 = ("abc", 34, True, 40, "male")
print(tuple1)

tuple2 = tuple((1,2,3,4))
print(tuple2)

# Accessing tuple #

mytuple1 = ("apple", "ball", "cat", "dog", "elephant")
print(mytuple1[1])
print(mytuple1[-1])
print(mytuple1[0:3])
print(mytuple1[-3:-1])

# Check if exist #
if "apple" in mytuple1:
    print("Yes, there is apple")

# Update tuple #
x = ("apple", "ball", "cat")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x)

# 1. Convert into a list: #
thistuple = ("apple", "ball", "cat")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)
print(thistuple)

# 2. Add tuple to a tuple: # 
thistuple = ("apple", "ball", "cat")
y = ("orange",)
thistuple += y
print(thistuple)

# Cannot remove items

# Unpack Tuples #
fruits = ("apple", "banana", "cherry", "papaya")
(green, yellow, red, orange) = fruits
(f1, *f2, f3) = fruits  # If the number of variables is less than the number of values, you can add an * to the variable name and the values will be assigned to the variable as a list:
print(green)
print(yellow)
print(red)
print(orange)

print(f1)
print(f2)
print(f3)

# Loop Tuples #
for x in fruits:
    print(x)

for i in range(len(fruits)):
    print(fruits[i])

idx = 0
while idx < len(fruits):
    print(fruits[idx])
    idx+=1

# Join Tuple #
tuple111 = ("a", "b" , "c")
tuple222 = (1, 2, 3)

tuple333 = tuple111 + tuple222
print(tuple333)
print(tuple333 * 2) # multiply content

# Tuple Methods #
'''
Method	Description
count()	Returns the number of times a specified value occurs in a tuple
index()	Searches the tuple for a specified value and returns the position of where it was found
'''