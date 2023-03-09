# While loop #
x = 10
i = 1
while i <= 10:
    print(i)
    i += 1

i = 1
while i < 10:
    print(i)
    if(i == 5):
        break
    i += 1

i = 0
while i < 10:
    i += 1
    if(i == 5):
        continue
    print(i)

i = 1
while i < 6:
  print(i)
  i += 1
else: # executes once in false statement
  print("i is no longer less than 6")

# for loop #
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

for x in "banana":
   print(x)

for x in fruits:
    if x == "banana":
        break
    print(x)

for x in fruits:
    if x == "banana":
        continue
    print(x)

for x in range(6):
   print(x)

for x in range(2,6):
   print(x)

for x in range(1,10,2): # last paramater is increment for range
   print(x)
else:
  print("Finally finished!") # not executed if stopped by break


# Nested loop #

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)

# pass statement #
for x in [2,4,6,8]:
   pass